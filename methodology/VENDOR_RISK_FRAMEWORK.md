# Vendor Risk Management Framework

**Version:** 1.0  
**Maintained by:** [TrazTech](https://traztech.ca)  
**Compliance Mapping:** SOC 2 CC9.2 | ISO 27001 A.5.19-A.5.22 | HIPAA 164.308(b) | PCI DSS 12.8

---

## 1. Purpose

This framework establishes a structured, risk-based approach to managing third-party vendor relationships. It defines how vendors are classified, assessed, monitored, and offboarded to ensure that third-party risk is identified, measured, and controlled.

Every organization that handles sensitive data relies on vendors. Each vendor relationship introduces risk: data exposure, operational dependency, compliance gaps, and supply chain vulnerabilities. This framework ensures that risk is proportional to the depth and criticality of each vendor relationship.

This framework is aligned with the methodology TrazTech uses with its clients. For background on maintaining compliance evidence between audit cycles, see [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh) and [Control Drift Between Audits](https://traztech.ca/blog/control-drift-between-audits).

## 2. Scope

This framework applies to all third-party vendors, service providers, contractors, and business partners that:

- Access, process, store, or transmit organizational data
- Provide technology services or infrastructure
- Have network connectivity to organizational systems
- Provide services that, if disrupted, would impact business operations
- Process data on behalf of the organization (data processors under GDPR/PIPEDA)

## 3. Vendor Tiering Methodology

Vendors are classified into four tiers based on a composite assessment of three factors: **data access**, **integration depth**, and **business criticality**.

### 3.1 Tiering Factors

#### Factor 1: Data Access Level

| Level | Description | Examples | Score |
|-------|------------|----------|-------|
| **None** | No access to organizational data | Office furniture supplier, catering | 0 |
| **Public** | Access only to publicly available information | Marketing analytics on public web data | 1 |
| **Internal** | Access to internal, non-sensitive business data | Project management tools with internal docs | 2 |
| **Confidential** | Access to confidential business data (financials, strategy) | Accounting software, ERP systems | 3 |
| **Restricted** | Access to PII, PHI, payment data, or authentication credentials | Cloud infrastructure, HRIS, payment processor | 4 |

#### Factor 2: Integration Depth

| Level | Description | Examples | Score |
|-------|------------|----------|-------|
| **None** | No technical integration | Physical-only services | 0 |
| **API/Data Feed** | Read-only API access or periodic data export | Reporting tools, analytics | 1 |
| **Bidirectional** | Read/write API access, data synchronization | CRM integrations, SSO providers | 2 |
| **Embedded** | Vendor code/agents running in your environment | Monitoring agents, SDKs, plugins | 3 |
| **Infrastructure** | Vendor provides foundational infrastructure | Cloud hosting, DNS, CDN, CI/CD | 4 |

#### Factor 3: Business Criticality

| Level | Description | Examples | Score |
|-------|------------|----------|-------|
| **Negligible** | Disruption has no meaningful impact | Decorative services | 0 |
| **Low** | Disruption is an inconvenience, easy workaround exists | Collaboration tools with alternatives | 1 |
| **Moderate** | Disruption affects productivity, workaround is painful | Email provider, document management | 2 |
| **High** | Disruption significantly impacts operations or revenue | Payment processing, core SaaS application | 3 |
| **Critical** | Disruption halts business operations entirely | Cloud infrastructure, primary database | 4 |

### 3.2 Tier Calculation

Sum the three factor scores (0-12 possible) and map to tiers:

| Composite Score | Tier | Label |
|----------------|------|-------|
| 10-12 | **Tier 1** | Critical |
| 7-9 | **Tier 2** | High |
| 4-6 | **Tier 3** | Medium |
| 0-3 | **Tier 4** | Low |

**Override rule:** Any vendor with a Data Access Level of "Restricted" (score 4) is automatically Tier 1 or Tier 2, regardless of the composite score.

### 3.3 Tier Examples

| Vendor Type | Data Access | Integration | Criticality | Score | Tier |
|-------------|------------|-------------|-------------|-------|------|
| AWS (cloud hosting) | Restricted (4) | Infrastructure (4) | Critical (4) | 12 | Tier 1 - Critical |
| Stripe (payments) | Restricted (4) | Bidirectional (2) | High (3) | 9 | Tier 1 - Critical |
| Okta (SSO/IAM) | Restricted (4) | Embedded (3) | High (3) | 10 | Tier 1 - Critical |
| HubSpot (CRM) | Confidential (3) | Bidirectional (2) | Moderate (2) | 7 | Tier 2 - High |
| Jira (project mgmt) | Internal (2) | API (1) | Moderate (2) | 5 | Tier 3 - Medium |
| Canva (design) | Public (1) | None (0) | Low (1) | 2 | Tier 4 - Low |

## 4. Assessment Requirements by Tier

### 4.1 Assessment Depth

| Requirement | Tier 1 (Critical) | Tier 2 (High) | Tier 3 (Medium) | Tier 4 (Low) |
|-------------|-------------------|---------------|-----------------|--------------|
| Full security questionnaire (70+ questions) | Required | Required |: |: |
| Abbreviated questionnaire (20-30 questions) |: |: | Required |: |
| Self-attestation only |: |: |: | Required |
| SOC 2 Type II report review | Required | Required | Requested |: |
| ISO 27001 certificate review | Required | Required | Requested |: |
| Penetration test report review | Required | Recommended |: |: |
| Architecture/data flow review | Required | Recommended |: |: |
| On-site or virtual security assessment | Recommended |: |: |: |
| Data Processing Agreement (DPA) | Required | Required | If applicable |: |
| Business Continuity Plan review | Required | Recommended |: |: |
| Incident response plan review | Required | Recommended |: |: |
| Insurance certificate (cyber liability) | Required | Recommended |: |: |
| Background check policy verification | Required | Recommended |: |: |
| Subprocessor list review | Required | Required | Requested |: |

### 4.2 Assessment Frequency

| Tier | Initial Assessment | Periodic Reassessment | Trigger-Based Review |
|------|-------------------|-----------------------|---------------------|
| **Tier 1 - Critical** | Before contract signing | Annually | On any material change, breach notification, or SOC 2 report refresh |
| **Tier 2 - High** | Before contract signing | Annually | On breach notification or significant service change |
| **Tier 3 - Medium** | Within 30 days of onboarding | Every 2 years | On breach notification |
| **Tier 4 - Low** | Within 90 days of onboarding | Every 3 years | On breach notification |

**Trigger events** that require out-of-cycle review for any tier:
- Vendor reports a security incident or data breach
- Vendor undergoes a merger, acquisition, or significant ownership change
- Scope of vendor services materially changes (e.g., gains access to new data categories)
- Vendor's SOC 2 report contains new exceptions or qualifications
- Regulatory changes affect the vendor relationship
- Media reports of significant security issues at the vendor

For guidance on scheduling recurring compliance activities like vendor reviews, see [Compliance Calendar: What Actually Recurs](https://traztech.ca/blog/compliance-calendar-what-actually-recurs) on the TrazTech blog.

## 5. Scoring Rubric

Vendors are scored across seven security domains on a 1-5 scale. See [`scoring/risk-scoring-guide.md`](../scoring/risk-scoring-guide.md) for the complete scoring rubric with domain weights and detailed criteria.

### 5.1 Summary Scoring Scale

| Score | Rating | Meaning |
|-------|--------|---------|
| 5 | Excellent | Industry-leading security practices, exceeds requirements |
| 4 | Good | Strong security practices, meets all requirements |
| 3 | Adequate | Acceptable security practices, meets minimum requirements |
| 2 | Below Standard | Gaps exist, compensating controls may be needed |
| 1 | Inadequate | Significant deficiencies, material risk |

### 5.2 Security Domains

1. **Data Protection & Privacy** (Weight: 25%)
2. **Access Control & Authentication** (Weight: 20%)
3. **Infrastructure & Network Security** (Weight: 15%)
4. **Application Security & SDLC** (Weight: 15%)
5. **Incident Response & Business Continuity** (Weight: 10%)
6. **Governance & Compliance** (Weight: 10%)
7. **Third-Party/Subprocessor Management** (Weight: 5%)

### 5.3 Aggregate Risk Score

The weighted aggregate score determines the vendor's risk rating:

| Weighted Score | Risk Rating | Action Required |
|---------------|-------------|-----------------|
| 4.1 - 5.0 | **Low Risk** | Approve; standard monitoring |
| 3.0 - 4.0 | **Moderate Risk** | Approve with conditions; enhanced monitoring |
| 2.0 - 2.9 | **High Risk** | Requires risk acceptance from CISO/VP; compensating controls required |
| 1.0 - 1.9 | **Critical Risk** | Do not approve without executive sign-off and detailed remediation plan |

## 6. Risk Acceptance and Escalation

### 6.1 Approval Authority

| Risk Rating | Approval Authority |
|-------------|-------------------|
| Low Risk | Security team / GRC analyst |
| Moderate Risk | Security manager / Compliance lead |
| High Risk | CISO or VP of Engineering |
| Critical Risk | CISO + CEO/CTO (executive sign-off required) |

### 6.2 Risk Acceptance Requirements

When accepting risk for a vendor scoring below "Moderate Risk":

1. **Document the business justification**: Why is this vendor necessary? Are there alternatives?
2. **Identify compensating controls**: What controls will your organization implement to reduce the residual risk? (e.g., network segmentation, additional logging, data minimization)
3. **Set a remediation timeline**: The vendor must commit to addressing identified deficiencies within a defined period (typically 90 days for High Risk, 30 days for Critical items).
4. **Increase monitoring frequency**: High-risk vendors should be reassessed quarterly until the risk rating improves.
5. **Record the risk acceptance**: Document the acceptance in your risk register with the approver, date, justification, and review date.

### 6.3 Escalation Path

```
Assessor identifies risk
    |
    v
Risk documented in assessment report
    |
    v
[Low/Moderate] --> Approved by security team with standard conditions
    |
[High] --> Escalated to CISO/VP with compensating controls proposal
    |
    v
[Critical] --> Escalated to executive team; vendor engagement paused
                pending executive decision
    |
    v
Risk acceptance documented in risk register
    |
    v
Remediation timeline tracked; vendor reassessed on schedule
```

## 7. Ongoing Monitoring

Between formal assessments, vendors should be monitored for material changes.

### 7.1 Continuous Monitoring Activities

| Activity | Frequency | Tier Applicability |
|----------|-----------|-------------------|
| Review vendor security advisories and status pages | Weekly | Tier 1 |
| Check for vendor breach disclosures (news, breach databases) | Monthly | Tier 1-2 |
| Review vendor SOC 2/ISO 27001 report upon issuance | Upon receipt | Tier 1-2 |
| Verify vendor insurance and certification currency | Annually | Tier 1-2 |
| Review vendor subprocessor list for changes | Quarterly | Tier 1 |
| Monitor vendor uptime/SLA compliance | Monthly | Tier 1-2 |
| Review access logs for vendor accounts | Quarterly | Tier 1-2 |
| Validate DPA and contractual obligations remain current | Annually | Tier 1-3 |

### 7.2 Monitoring Triggers

Any of the following should trigger an immediate review:

- Vendor notifies you of a security incident
- You discover unauthorized data access by the vendor
- Vendor's SOC 2 report is overdue or unavailable
- Vendor announces end-of-life for a product you depend on
- Vendor is acquired or merges with another company
- Significant negative media coverage about vendor security practices

## 8. Vendor Lifecycle

### 8.1 Onboarding

1. Identify vendor tier using the tiering methodology (Section 3)
2. Conduct appropriate assessment (Section 4)
3. Score vendor using the scoring rubric (Section 5)
4. Obtain necessary approvals (Section 6)
5. Execute required agreements (DPA, NDA, SLA, BAA if applicable)
6. Complete the [Vendor Due Diligence Checklist](../templates/vendor-due-diligence-checklist.md)
7. Record vendor in the [Vendor Inventory](../templates/vendor-inventory.csv)
8. Schedule next review date

### 8.2 Ongoing Management

1. Monitor vendor per the ongoing monitoring schedule (Section 7)
2. Conduct periodic reassessments per the assessment frequency (Section 4.2)
3. Track and remediate findings from assessments
4. Update vendor inventory with any changes
5. Review and renew agreements as needed

### 8.3 Offboarding

1. Complete the [Vendor Offboarding Checklist](../templates/vendor-offboarding-checklist.md)
2. Ensure data return or destruction
3. Revoke all access credentials
4. Terminate agreements
5. Update vendor inventory
6. Retain assessment records per your retention policy (minimum 3 years recommended for SOC 2; 6 years for ISO 27001)

## 9. Documentation and Evidence

For each vendor, maintain the following evidence package:

- Completed security questionnaire
- Risk assessment report
- SOC 2 / ISO 27001 reports (as applicable)
- Signed DPA, NDA, and SLA
- Risk acceptance documentation (if applicable)
- Correspondence related to remediation items
- Monitoring records

This evidence is critical for audit readiness. Auditors reviewing SOC 2 CC9.2 or ISO 27001 A.5.19-A.5.22 will expect to see documented vendor assessments, a risk-based methodology, and evidence that the program is operating consistently.

For tips on maintaining evidence quality between audits, see [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh) on the TrazTech blog.

## 10. Framework Compliance Mapping

| Framework | Requirement | How This Framework Addresses It |
|-----------|------------|---------------------------------|
| **SOC 2** | CC9.2 | Vendor risk assessment, monitoring, and management lifecycle |
| **ISO 27001** | A.5.19 | Information security in supplier relationships (tiering, assessment) |
| **ISO 27001** | A.5.20 | Addressing security within supplier agreements (DPA, SLA review) |
| **ISO 27001** | A.5.21 | Managing security in the ICT supply chain (subprocessor review) |
| **ISO 27001** | A.5.22 | Monitoring, review, and change management of supplier services |
| **HIPAA** | 164.308(b) | Business associate contracts and arrangements |
| **HIPAA** | 164.314 | Organizational requirements for BAAs |
| **PCI DSS** | 12.8 | Service provider management policy and procedures |
| **PCI DSS** | 12.9 | Service provider acknowledgment of responsibilities |
| **NIST CSF** | ID.SC-1 | Cyber supply chain risk management processes |
| **NIST CSF** | ID.SC-2 | Supplier identification, prioritization, and assessment |
| **GDPR** | Article 28 | Processor obligations and contractual requirements |
| **GDPR** | Article 32 | Security of processing (vendor security assessment) |

---

*This framework is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For a free SOC 2 readiness checklist, visit [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*
