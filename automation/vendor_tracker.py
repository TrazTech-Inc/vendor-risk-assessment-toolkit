#!/usr/bin/env python3
"""
Vendor Risk Tracker

Reads a vendor inventory CSV, flags overdue reviews, calculates risk metrics,
and generates a summary markdown report.

Part of the Vendor Risk Assessment Toolkit
Maintained by TrazTech (https://traztech.ca)

Usage:
    python vendor_tracker.py --inventory ../templates/vendor-inventory.csv
    python vendor_tracker.py --inventory ../templates/vendor-inventory.csv --report output.md
    python vendor_tracker.py --inventory ../templates/vendor-inventory.csv --days-warning 30
"""

import csv
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

try:
    import click
    import pandas as pd
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install -r requirements.txt")
    print()
    print("Required packages: pandas, rich, click")
    sys.exit(1)

console = Console()

RISK_COLORS = {
    "Low": "green",
    "Moderate": "yellow",
    "High": "dark_orange",
    "Critical": "red",
    "Unknown": "dim",
}


def parse_date(date_str: str) -> Optional[datetime]:
    """Parse a date string in common formats."""
    if not date_str or pd.isna(date_str):
        return None
    date_str = str(date_str).strip()
    if not date_str:
        return None
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%m-%d-%Y",
        "%d-%m-%Y",
        "%B %d, %Y",
        "%b %d, %Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def get_risk_rating(score: float) -> str:
    """Convert a numeric risk score to a risk rating."""
    if score >= 4.1:
        return "Low"
    elif score >= 3.0:
        return "Moderate"
    elif score >= 2.0:
        return "High"
    elif score >= 1.0:
        return "Critical"
    return "Unknown"


def normalize_yes_no(value: str) -> Optional[bool]:
    """Normalize Y/N/Yes/No values to boolean."""
    if not value or pd.isna(value):
        return None
    value = str(value).strip().upper()
    if value in ("Y", "YES", "TRUE", "1"):
        return True
    if value in ("N", "NO", "FALSE", "0"):
        return False
    return None


def normalize_tier(tier_str: str) -> str:
    """Normalize tier values to a consistent format."""
    if not tier_str or pd.isna(tier_str):
        return "Unknown"
    tier_str = str(tier_str).strip()
    tier_map = {
        "1": "Tier 1",
        "2": "Tier 2",
        "3": "Tier 3",
        "4": "Tier 4",
        "tier 1": "Tier 1",
        "tier 2": "Tier 2",
        "tier 3": "Tier 3",
        "tier 4": "Tier 4",
        "critical": "Tier 1",
        "high": "Tier 2",
        "medium": "Tier 3",
        "low": "Tier 4",
        "tier 1 - critical": "Tier 1",
        "tier 2 - high": "Tier 2",
        "tier 3 - medium": "Tier 3",
        "tier 4 - low": "Tier 4",
    }
    return tier_map.get(tier_str.lower(), tier_str)


def load_inventory(filepath: str) -> pd.DataFrame:
    """Load and validate the vendor inventory CSV."""
    path = Path(filepath)
    if not path.exists():
        console.print(f"[red]Error:[/red] File not found: {filepath}")
        sys.exit(1)

    try:
        df = pd.read_csv(filepath, skipinitialspace=True)
    except Exception as e:
        console.print(f"[red]Error reading CSV:[/red] {e}")
        sys.exit(1)

    # Normalize column names (strip whitespace, handle variations)
    df.columns = df.columns.str.strip()

    # Check for required columns
    required_cols = ["Vendor Name"]
    for col in required_cols:
        if col not in df.columns:
            console.print(
                f"[red]Error:[/red] Required column '{col}' not found in CSV."
            )
            console.print(f"Found columns: {list(df.columns)}")
            sys.exit(1)

    # Drop completely empty rows
    df = df.dropna(how="all")

    if df.empty:
        console.print("[yellow]Warning:[/yellow] No vendor data found in CSV.")
        return df

    return df


def analyze_vendors(df: pd.DataFrame, days_warning: int = 30) -> dict:
    """Analyze vendor inventory and return findings."""
    today = datetime.now()
    warning_date = today + timedelta(days=days_warning)

    findings = {
        "total_vendors": len(df),
        "overdue_reviews": [],
        "upcoming_reviews": [],
        "missing_soc2": [],
        "missing_dpa": [],
        "missing_review_date": [],
        "high_risk_vendors": [],
        "risk_distribution": {"Low": 0, "Moderate": 0, "High": 0, "Critical": 0, "Unknown": 0},
        "tier_distribution": {},
        "vendors_data": [],
    }

    for _, row in df.iterrows():
        vendor_name = str(row.get("Vendor Name", "Unknown")).strip()
        if not vendor_name or vendor_name == "nan":
            continue

        tier = normalize_tier(row.get("Tier", ""))
        risk_score_raw = row.get("Risk Score", None)
        risk_score = None
        if risk_score_raw and not pd.isna(risk_score_raw):
            try:
                risk_score = float(risk_score_raw)
            except (ValueError, TypeError):
                risk_score = None

        risk_rating = get_risk_rating(risk_score) if risk_score else "Unknown"
        findings["risk_distribution"][risk_rating] += 1

        # Track tier distribution
        findings["tier_distribution"][tier] = (
            findings["tier_distribution"].get(tier, 0) + 1
        )

        # Parse dates
        last_review = parse_date(row.get("Last Review Date", ""))
        next_review = parse_date(row.get("Next Review Date", ""))

        # Check for overdue reviews
        if next_review and next_review < today:
            days_overdue = (today - next_review).days
            findings["overdue_reviews"].append(
                {
                    "vendor": vendor_name,
                    "tier": tier,
                    "next_review": next_review.strftime("%Y-%m-%d"),
                    "days_overdue": days_overdue,
                    "risk_score": risk_score,
                }
            )
        elif next_review and next_review <= warning_date:
            days_until = (next_review - today).days
            findings["upcoming_reviews"].append(
                {
                    "vendor": vendor_name,
                    "tier": tier,
                    "next_review": next_review.strftime("%Y-%m-%d"),
                    "days_until": days_until,
                }
            )

        # Check for missing review dates
        if not next_review:
            findings["missing_review_date"].append(
                {"vendor": vendor_name, "tier": tier}
            )

        # Check for missing SOC 2
        soc2 = normalize_yes_no(row.get("SOC 2 Report (Y/N)", ""))
        if soc2 is False and tier in ("Tier 1", "Tier 2"):
            findings["missing_soc2"].append(
                {"vendor": vendor_name, "tier": tier}
            )

        # Check for missing DPA
        dpa = normalize_yes_no(row.get("DPA Signed (Y/N)", ""))
        if dpa is False and tier in ("Tier 1", "Tier 2", "Tier 3"):
            findings["missing_dpa"].append(
                {"vendor": vendor_name, "tier": tier}
            )

        # High/Critical risk vendors
        if risk_rating in ("High", "Critical"):
            findings["high_risk_vendors"].append(
                {
                    "vendor": vendor_name,
                    "tier": tier,
                    "risk_score": risk_score,
                    "risk_rating": risk_rating,
                }
            )

        # Store vendor data for summary table
        findings["vendors_data"].append(
            {
                "vendor": vendor_name,
                "tier": tier,
                "risk_score": risk_score,
                "risk_rating": risk_rating,
                "soc2": soc2,
                "iso27001": normalize_yes_no(row.get("ISO 27001 Certified (Y/N)", "")),
                "dpa": dpa,
                "last_review": last_review,
                "next_review": next_review,
            }
        )

    # Sort overdue reviews by days overdue (most overdue first)
    findings["overdue_reviews"].sort(key=lambda x: x["days_overdue"], reverse=True)
    findings["upcoming_reviews"].sort(key=lambda x: x["days_until"])

    return findings


def print_console_report(findings: dict, days_warning: int) -> None:
    """Print a rich console report of findings."""
    console.print()
    console.print(
        Panel(
            "[bold]Vendor Risk Tracker[/bold]\n"
            "Part of the Vendor Risk Assessment Toolkit\n"
            "Maintained by TrazTech (https://traztech.ca)",
            box=box.DOUBLE,
        )
    )
    console.print()

    # Summary stats
    total = findings["total_vendors"]
    overdue = len(findings["overdue_reviews"])
    upcoming = len(findings["upcoming_reviews"])
    missing_soc2 = len(findings["missing_soc2"])
    missing_dpa = len(findings["missing_dpa"])
    high_risk = len(findings["high_risk_vendors"])

    summary_table = Table(title="Summary", box=box.SIMPLE)
    summary_table.add_column("Metric", style="bold")
    summary_table.add_column("Count", justify="right")
    summary_table.add_column("Status")

    summary_table.add_row("Total Vendors", str(total), "")
    summary_table.add_row(
        "Overdue Reviews",
        str(overdue),
        "[red]ACTION REQUIRED[/red]" if overdue > 0 else "[green]OK[/green]",
    )
    summary_table.add_row(
        f"Reviews Due Within {days_warning} Days",
        str(upcoming),
        "[yellow]UPCOMING[/yellow]" if upcoming > 0 else "[green]OK[/green]",
    )
    summary_table.add_row(
        "Missing SOC 2 (Tier 1-2)",
        str(missing_soc2),
        "[red]ATTENTION[/red]" if missing_soc2 > 0 else "[green]OK[/green]",
    )
    summary_table.add_row(
        "Missing DPA (Tier 1-3)",
        str(missing_dpa),
        "[red]ATTENTION[/red]" if missing_dpa > 0 else "[green]OK[/green]",
    )
    summary_table.add_row(
        "High/Critical Risk Vendors",
        str(high_risk),
        "[dark_orange]MONITOR[/dark_orange]" if high_risk > 0 else "[green]OK[/green]",
    )
    console.print(summary_table)
    console.print()

    # Risk distribution
    risk_table = Table(title="Risk Distribution", box=box.SIMPLE)
    risk_table.add_column("Risk Rating")
    risk_table.add_column("Count", justify="right")
    risk_table.add_column("Percentage", justify="right")
    for rating in ["Low", "Moderate", "High", "Critical", "Unknown"]:
        count = findings["risk_distribution"][rating]
        pct = f"{(count / total * 100):.0f}%" if total > 0 else "0%"
        color = RISK_COLORS.get(rating, "white")
        risk_table.add_row(f"[{color}]{rating}[/{color}]", str(count), pct)
    console.print(risk_table)
    console.print()

    # Tier distribution
    if findings["tier_distribution"]:
        tier_table = Table(title="Tier Distribution", box=box.SIMPLE)
        tier_table.add_column("Tier")
        tier_table.add_column("Count", justify="right")
        for tier in sorted(findings["tier_distribution"].keys()):
            tier_table.add_row(tier, str(findings["tier_distribution"][tier]))
        console.print(tier_table)
        console.print()

    # Overdue reviews
    if findings["overdue_reviews"]:
        console.print("[bold red]OVERDUE REVIEWS[/bold red]")
        overdue_table = Table(box=box.SIMPLE)
        overdue_table.add_column("Vendor", style="bold")
        overdue_table.add_column("Tier")
        overdue_table.add_column("Review Due")
        overdue_table.add_column("Days Overdue", justify="right", style="red")
        overdue_table.add_column("Risk Score", justify="right")
        for v in findings["overdue_reviews"]:
            overdue_table.add_row(
                v["vendor"],
                v["tier"],
                v["next_review"],
                str(v["days_overdue"]),
                f"{v['risk_score']:.1f}" if v["risk_score"] else "N/A",
            )
        console.print(overdue_table)
        console.print()

    # Upcoming reviews
    if findings["upcoming_reviews"]:
        console.print(f"[bold yellow]REVIEWS DUE WITHIN {days_warning} DAYS[/bold yellow]")
        upcoming_table = Table(box=box.SIMPLE)
        upcoming_table.add_column("Vendor", style="bold")
        upcoming_table.add_column("Tier")
        upcoming_table.add_column("Review Due")
        upcoming_table.add_column("Days Until", justify="right", style="yellow")
        for v in findings["upcoming_reviews"]:
            upcoming_table.add_row(
                v["vendor"], v["tier"], v["next_review"], str(v["days_until"])
            )
        console.print(upcoming_table)
        console.print()

    # Missing SOC 2
    if findings["missing_soc2"]:
        console.print("[bold red]TIER 1-2 VENDORS MISSING SOC 2 REPORT[/bold red]")
        for v in findings["missing_soc2"]:
            console.print(f"  - {v['vendor']} ({v['tier']})")
        console.print()

    # Missing DPA
    if findings["missing_dpa"]:
        console.print("[bold red]TIER 1-3 VENDORS MISSING DPA[/bold red]")
        for v in findings["missing_dpa"]:
            console.print(f"  - {v['vendor']} ({v['tier']})")
        console.print()

    # High/Critical risk vendors
    if findings["high_risk_vendors"]:
        console.print("[bold dark_orange]HIGH/CRITICAL RISK VENDORS[/bold dark_orange]")
        risk_vendor_table = Table(box=box.SIMPLE)
        risk_vendor_table.add_column("Vendor", style="bold")
        risk_vendor_table.add_column("Tier")
        risk_vendor_table.add_column("Risk Score", justify="right")
        risk_vendor_table.add_column("Rating")
        for v in findings["high_risk_vendors"]:
            color = RISK_COLORS.get(v["risk_rating"], "white")
            risk_vendor_table.add_row(
                v["vendor"],
                v["tier"],
                f"{v['risk_score']:.1f}",
                f"[{color}]{v['risk_rating']}[/{color}]",
            )
        console.print(risk_vendor_table)
        console.print()

    # Missing review dates
    if findings["missing_review_date"]:
        console.print("[bold yellow]VENDORS MISSING NEXT REVIEW DATE[/bold yellow]")
        for v in findings["missing_review_date"]:
            console.print(f"  - {v['vendor']} ({v['tier']})")
        console.print()


def generate_markdown_report(findings: dict, days_warning: int, output_path: str) -> None:
    """Generate a markdown summary report."""
    today = datetime.now().strftime("%Y-%m-%d")
    total = findings["total_vendors"]

    lines = [
        "# Vendor Risk Tracker Report",
        "",
        f"**Generated:** {today}",
        f"**Total Vendors:** {total}",
        f"**Warning Window:** {days_warning} days",
        "",
        "*Generated by the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca).*",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Metric | Count | Status |",
        "|--------|-------|--------|",
    ]

    overdue = len(findings["overdue_reviews"])
    upcoming = len(findings["upcoming_reviews"])
    missing_soc2 = len(findings["missing_soc2"])
    missing_dpa = len(findings["missing_dpa"])
    high_risk = len(findings["high_risk_vendors"])

    lines.append(
        f"| Overdue Reviews | {overdue} | {'ACTION REQUIRED' if overdue else 'OK'} |"
    )
    lines.append(
        f"| Reviews Due Within {days_warning} Days | {upcoming} | {'UPCOMING' if upcoming else 'OK'} |"
    )
    lines.append(
        f"| Missing SOC 2 (Tier 1-2) | {missing_soc2} | {'ATTENTION' if missing_soc2 else 'OK'} |"
    )
    lines.append(
        f"| Missing DPA (Tier 1-3) | {missing_dpa} | {'ATTENTION' if missing_dpa else 'OK'} |"
    )
    lines.append(
        f"| High/Critical Risk | {high_risk} | {'MONITOR' if high_risk else 'OK'} |"
    )

    # Risk distribution
    lines.extend(
        [
            "",
            "## Risk Distribution",
            "",
            "| Risk Rating | Count | Percentage |",
            "|-------------|-------|------------|",
        ]
    )
    for rating in ["Low", "Moderate", "High", "Critical", "Unknown"]:
        count = findings["risk_distribution"][rating]
        pct = f"{(count / total * 100):.0f}%" if total > 0 else "0%"
        lines.append(f"| {rating} | {count} | {pct} |")

    # Tier distribution
    if findings["tier_distribution"]:
        lines.extend(
            [
                "",
                "## Tier Distribution",
                "",
                "| Tier | Count |",
                "|------|-------|",
            ]
        )
        for tier in sorted(findings["tier_distribution"].keys()):
            lines.append(f"| {tier} | {findings['tier_distribution'][tier]} |")

    # Overdue reviews
    if findings["overdue_reviews"]:
        lines.extend(
            [
                "",
                "## Overdue Reviews",
                "",
                "| Vendor | Tier | Review Due | Days Overdue | Risk Score |",
                "|--------|------|------------|-------------|------------|",
            ]
        )
        for v in findings["overdue_reviews"]:
            score_str = f"{v['risk_score']:.1f}" if v["risk_score"] else "N/A"
            lines.append(
                f"| {v['vendor']} | {v['tier']} | {v['next_review']} | {v['days_overdue']} | {score_str} |"
            )

    # Upcoming reviews
    if findings["upcoming_reviews"]:
        lines.extend(
            [
                "",
                f"## Reviews Due Within {days_warning} Days",
                "",
                "| Vendor | Tier | Review Due | Days Until |",
                "|--------|------|------------|------------|",
            ]
        )
        for v in findings["upcoming_reviews"]:
            lines.append(
                f"| {v['vendor']} | {v['tier']} | {v['next_review']} | {v['days_until']} |"
            )

    # Missing SOC 2
    if findings["missing_soc2"]:
        lines.extend(
            [
                "",
                "## Tier 1-2 Vendors Missing SOC 2 Report",
                "",
            ]
        )
        for v in findings["missing_soc2"]:
            lines.append(f"- **{v['vendor']}** ({v['tier']})")

    # Missing DPA
    if findings["missing_dpa"]:
        lines.extend(
            [
                "",
                "## Tier 1-3 Vendors Missing DPA",
                "",
            ]
        )
        for v in findings["missing_dpa"]:
            lines.append(f"- **{v['vendor']}** ({v['tier']})")

    # High/Critical risk vendors
    if findings["high_risk_vendors"]:
        lines.extend(
            [
                "",
                "## High/Critical Risk Vendors",
                "",
                "| Vendor | Tier | Risk Score | Rating |",
                "|--------|------|------------|--------|",
            ]
        )
        for v in findings["high_risk_vendors"]:
            lines.append(
                f"| {v['vendor']} | {v['tier']} | {v['risk_score']:.1f} | {v['risk_rating']} |"
            )

    # Missing review dates
    if findings["missing_review_date"]:
        lines.extend(
            [
                "",
                "## Vendors Missing Next Review Date",
                "",
            ]
        )
        for v in findings["missing_review_date"]:
            lines.append(f"- **{v['vendor']}** ({v['tier']})")

    # Vendor inventory table
    lines.extend(
        [
            "",
            "## Full Vendor Inventory",
            "",
            "| Vendor | Tier | Risk Score | Rating | SOC 2 | ISO 27001 | DPA | Last Review | Next Review |",
            "|--------|------|------------|--------|-------|-----------|-----|-------------|-------------|",
        ]
    )
    for v in findings["vendors_data"]:
        score_str = f"{v['risk_score']:.1f}" if v["risk_score"] else "N/A"
        soc2_str = "Y" if v["soc2"] else ("N" if v["soc2"] is False else "-")
        iso_str = "Y" if v["iso27001"] else ("N" if v["iso27001"] is False else "-")
        dpa_str = "Y" if v["dpa"] else ("N" if v["dpa"] is False else "-")
        last_str = v["last_review"].strftime("%Y-%m-%d") if v["last_review"] else "-"
        next_str = v["next_review"].strftime("%Y-%m-%d") if v["next_review"] else "-"
        lines.append(
            f"| {v['vendor']} | {v['tier']} | {score_str} | {v['risk_rating']} | "
            f"{soc2_str} | {iso_str} | {dpa_str} | {last_str} | {next_str} |"
        )

    # Footer
    lines.extend(
        [
            "",
            "---",
            "",
            "*For more on vendor risk management, visit [TrazTech](https://traztech.ca). "
            "Free SOC 2 Readiness Checklist: [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*",
            "",
        ]
    )

    # Write report
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    console.print(f"[green]Report saved to:[/green] {output_path}")


@click.command()
@click.option(
    "--inventory",
    "-i",
    required=True,
    type=click.Path(exists=True),
    help="Path to vendor inventory CSV file",
)
@click.option(
    "--report",
    "-r",
    default=None,
    type=click.Path(),
    help="Path to save markdown report (optional)",
)
@click.option(
    "--days-warning",
    "-d",
    default=30,
    type=int,
    help="Number of days ahead to warn about upcoming reviews (default: 30)",
)
@click.option(
    "--quiet",
    "-q",
    is_flag=True,
    help="Suppress console output (useful when only generating a report file)",
)
def main(inventory: str, report: Optional[str], days_warning: int, quiet: bool) -> None:
    """
    Vendor Risk Tracker -- Analyze vendor inventory and flag compliance issues.

    Reads a vendor inventory CSV and checks for:

    \b
    - Overdue vendor reviews
    - Upcoming reviews within the warning window
    - Tier 1-2 vendors missing SOC 2 reports
    - Tier 1-3 vendors missing Data Processing Agreements
    - High and Critical risk vendors
    - Vendors missing next review dates

    Part of the Vendor Risk Assessment Toolkit by TrazTech (https://traztech.ca).
    """
    # Load inventory
    df = load_inventory(inventory)

    if df.empty:
        if not quiet:
            console.print("[yellow]No vendors to analyze.[/yellow]")
        return

    # Analyze
    findings = analyze_vendors(df, days_warning)

    # Console output
    if not quiet:
        print_console_report(findings, days_warning)

    # Markdown report
    if report:
        generate_markdown_report(findings, days_warning, report)

    # Exit code: non-zero if there are overdue reviews or critical/high risk vendors
    overdue_count = len(findings["overdue_reviews"])
    critical_count = findings["risk_distribution"]["Critical"]

    if critical_count > 0:
        sys.exit(2)
    elif overdue_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
