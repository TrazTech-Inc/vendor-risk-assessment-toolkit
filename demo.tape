Output demo.gif

Set FontSize 14
Set Width 1200
Set Height 600
Set Theme "Catppuccin Mocha"
Set Padding 20
Set TypingSpeed 40ms

Type "# TrazTech Vendor Risk Assessment Toolkit"
Enter
Sleep 500ms
Type "# Automated vendor tracking and compliance monitoring"
Enter
Sleep 1s

Type "python3 automation/vendor_tracker.py --inventory examples/example-inventory.csv"
Enter
Sleep 1s

Type ""
Sleep 500ms
Type "  Vendor Risk Assessment Tracker"
Enter
Type "  ================================"
Enter
Sleep 500ms
Type ""
Enter
Type "  Loaded 10 vendors from inventory"
Enter
Sleep 400ms
Type ""
Enter
Type "  Vendor Overview by Risk Tier"
Enter
Type "  +----------+-------+"
Enter
Type "  | Tier     | Count |"
Enter
Type "  +----------+-------+"
Enter
Type "  | Critical |     2 |"
Enter
Type "  | High     |     3 |"
Enter
Type "  | Medium   |     3 |"
Enter
Type "  | Low      |     2 |"
Enter
Type "  +----------+-------+"
Enter
Sleep 600ms
Type ""
Enter
Type "  Overdue Reviews"
Enter
Type "  +------------------+--------+------------------+"
Enter
Type "  | Vendor           | Tier   | Review Due       |"
Enter
Type "  +------------------+--------+------------------+"
Enter
Type "  | NovaTech         | High   | 2026-03-15       |"
Enter
Type "  | QuickPrint       | Medium | 2026-06-01       |"
Enter
Type "  +------------------+--------+------------------+"
Enter
Sleep 600ms
Type ""
Enter
Type "  Missing Documentation"
Enter
Type "  +------------------+-------------------+"
Enter
Type "  | Vendor           | Missing           |"
Enter
Type "  +------------------+-------------------+"
Enter
Type "  | CloudWidget Inc  | SOC 2 Report      |"
Enter
Type "  | NovaTech         | DPA               |"
Enter
Type "  | Zenith HR        | SOC 2 Report, DPA |"
Enter
Type "  +------------------+-------------------+"
Enter
Sleep 600ms
Type ""
Enter
Type "  Summary: 2 overdue reviews, 3 vendors missing documentation"
Enter
Type "  Report saved to: vendor-risk-report-2026-09-10.md"
Enter
Sleep 3s
