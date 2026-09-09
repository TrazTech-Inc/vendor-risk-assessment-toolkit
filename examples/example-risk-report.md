# Vendor Risk Assessment Report -- Completed Example

**Vendor:** CloudWidget Inc
**Assessment Date:** 2026-06-10
**Assessor:** Sarah Chen, Security Lead

*This is a completed example of a vendor risk assessment report. CloudWidget Inc is a fictional SaaS vendor used for illustration purposes. See the accompanying [Example Completed Questionnaire](example-completed-questionnaire.md) for the full questionnaire responses.*

---

## Report Information

| Field | Value |
|-------|-------|
| **Vendor Name** | CloudWidget Inc |
| **Assessment Date** | 2026-06-10 |
| **Assessor Name** | Sarah Chen, Security Lead |
| **Vendor Tier** | [x] Tier 2 - High |
| **Assessment Type** | [x] Initial |
| **Report Status** | [x] Final |

---

## 1. Executive Summary

**Overall Risk Score:** 3.87 / 5.0

**Risk Rating:** [x] Moderate Risk

**Recommendation:** [x] Approve with Conditions

CloudWidget Inc provides a cloud-based project management and workflow automation platform that will be used as our primary project tracking tool. The vendor will access Confidential data, including project documents, customer information in project context, and employee names/emails. The vendor is hosted on AWS with a mature security program relative to its size (185 employees).

Overall, CloudWidget demonstrates a strong security posture with well-documented controls across most domains. The vendor holds a SOC 2 Type II report with one exception (access review timeliness in Q3 2025, since remediated) and is actively pursuing ISO 27001 certification with a target of Q4 2026. Key strengths include comprehensive application security practices, strong access controls with MFA enforcement, and good data protection controls including encryption at rest and in transit.

Two areas warrant attention: (1) the SOC 2 Type II exception, which should be resolved in the next reporting period, and (2) the lack of 24/7 SOC monitoring -- the security team currently monitors during extended business hours with on-call coverage for critical alerts. Neither issue is a blocker for engagement, but both should be tracked for improvement. Approval is recommended with conditions as noted below.

---

## 2. Vendor Overview

| Field | Details |
|-------|---------|
| **Vendor Name** | CloudWidget Inc |
| **Vendor Website** | https://cloudwidget.example.com |
| **Headquarters** | San Francisco, CA, USA |
| **Services Provided** | Cloud-based project management and workflow automation platform |
| **Data Types Accessed/Processed** | Customer names, email addresses, project data (documents, tasks, comments), file attachments, user activity logs |
| **Integration Type** | SaaS platform (web access); SAML SSO integration; API integration (read/write) with our Slack instance |
| **Contract Start Date** | 2026-07-01 (proposed) |
| **Contract End Date** | 2027-06-30 (initial 1-year term) |
| **Business Owner** | Sarah Chen |
| **Primary Vendor Contact** | Alex Rivera, VP of Security, alex.rivera@cloudwidget.example.com |

### 2.1 Tiering Justification

| Tiering Factor | Level | Score |
|---------------|-------|-------|
| Data Access | Confidential (project docs, customer data in context, employee PII) | 3 / 4 |
| Integration Depth | Bidirectional (SAML SSO + read/write API with Slack) | 2 / 4 |
| Business Criticality | Moderate (disruption impacts productivity; alternatives exist but migration is painful) | 2 / 4 |
| **Composite Score** | | **7 / 12** |
| **Assigned Tier** | **Tier 2 - High** | |

No override applied. Composite score of 7 places the vendor in Tier 2 (7-9).

---

## 3. Assessment Methodology

- [x] Security questionnaire completed (date: 2026-05-28)
- [x] SOC 2 Type II report reviewed (report period: April 2025 to March 2026)
- [ ] ISO 27001 certificate reviewed -- N/A, certification in progress
- [x] Penetration test report reviewed (date: February 2026, NCC Group)
- [ ] Architecture/data flow review conducted -- Reviewed via questionnaire; not a separate session
- [ ] Virtual/on-site security assessment conducted -- Not performed (Tier 2; questionnaire + SOC 2 deemed sufficient)
- [x] DPA/contract review completed (date: 2026-06-05)
- [x] BCP/DR plan reviewed (date: via questionnaire response)
- [x] Subprocessor list reviewed (date: 2026-06-01)
- [x] Insurance certificate reviewed (date: 2026-06-01)

---

## 4. Domain Scores

| # | Domain | Weight | Score (1-5) | Weighted Score |
|---|--------|--------|-------------|----------------|
| 1 | Data Protection & Privacy | 25% | 4.0 | 1.00 |
| 2 | Access Control & Authentication | 20% | 4.0 | 0.80 |
| 3 | Infrastructure & Network Security | 15% | 4.0 | 0.60 |
| 4 | Application Security & SDLC | 15% | 4.5 | 0.675 |
| 5 | Incident Response & Business Continuity | 10% | 4.0 | 0.40 |
| 6 | Governance & Compliance | 10% | 3.5 | 0.35 |
| 7 | Third-Party/Subprocessor Management | 5% | 3.5 | 0.175 |
| | **Aggregate Weighted Score** | **100%** | | **3.87 / 5.0** (rounding: 4.00) |

*Note: Individual question scores within each domain were averaged to produce the domain score. Decimal domain scores reflect averaging of question-level scores (e.g., Governance averaged across A1-A6 and H1-H5 questions).*

---

## 5. Detailed Findings

### 5.1 Data Protection & Privacy (Score: 4.0 / 5)

**Strengths:**
- AES-256 encryption at rest using AWS KMS
- TLS 1.2+ enforced with TLS 1.0/1.1 disabled; A+ SSL Labs rating
- Comprehensive data access logging with SIEM integration and 12-month retention
- Clear data residency with EU option
- 30-day data deletion after contract termination
- Standard DPA available and comprehensive

**Weaknesses/Gaps:**
- No customer-managed key (CMK) option (minor -- not required for our use case)
- Privacy program is adequate but lacks a dedicated privacy professional

**Evidence Reviewed:**
- Encryption standards documentation
- SSL Labs scan report
- Data classification policy
- Logging policy and sample log fields
- Data retention policy
- DPA template

---

### 5.2 Access Control & Authentication (Score: 4.0 / 5)

**Strengths:**
- MFA enforced for all users (employees and customers)
- Hardware security keys required for production access
- SAML 2.0 and OIDC SSO with SCIM provisioning
- JIT privileged access with automatic 4-hour revocation
- Quarterly access reviews with documented completion
- Automated deprovisioning within 4 hours of termination

**Weaknesses/Gaps:**
- SSO not available on Starter plan (acceptable for our engagement as we use Business plan)
- No dedicated PAM tool (compensated by effective process controls)

**Evidence Reviewed:**
- Authentication configuration documentation
- MFA enrollment report
- SSO and SCIM documentation
- Privileged access procedures
- Q1 2026 access review completion evidence
- Offboarding playbook

---

### 5.3 Infrastructure & Network Security (Score: 4.0 / 5)

**Strengths:**
- AWS hosting with multi-region architecture and IaC (Terraform)
- Network segmentation with separate AWS accounts per environment
- Weekly vulnerability scanning with defined patching SLAs
- Annual third-party pen test (NCC Group) with all findings remediated
- AWS Shield Advanced for DDoS protection
- CrowdStrike EDR on all endpoints with MDM enforcement

**Weaknesses/Gaps:**
- No 24/7 SOC -- business hours monitoring (8am-8pm PT) with on-call for critical alerts. This is the most significant gap identified in the assessment.

**Evidence Reviewed:**
- Infrastructure architecture overview
- Network architecture diagram
- Vulnerability management policy and patching SLAs
- Pen test executive summary (NCC Group, February 2026)
- DDoS protection documentation
- Endpoint security policy and compliance dashboard
- Security monitoring architecture

---

### 5.4 Application Security & SDLC (Score: 4.5 / 5)

**Strengths:**
- Formal SSDLC with security gates in CI/CD pipeline
- Mandatory peer review with automated SAST (Semgrep) and SCA (Snyk) blocking merges
- SBOM generated quarterly using Syft
- Dedicated secrets manager (AWS Secrets Manager) with pre-commit scanning (TruffleHog)
- Blue-green deployments with automatic rollback
- Strict environment separation with synthetic test data
- API gateway (Kong) with security controls

**Weaknesses/Gaps:**
- Threat modeling not yet systematic (planned for 2026)
- No DAST in CI/CD (quarterly DAST performed separately)

**Evidence Reviewed:**
- SSDLC documentation
- CI/CD pipeline configuration
- Code review policy
- Secrets management policy
- Deployment pipeline documentation
- Environment architecture
- API security documentation

---

### 5.5 Incident Response & Business Continuity (Score: 4.0 / 5)

**Strengths:**
- NIST SP 800-61 aligned IRP with annual tabletop exercises
- 48-hour breach notification commitment with structured communication
- BCP/DR tested annually with 2.5-hour demonstrated RTO (within 4-hour target)
- RPO of 1 hour with cross-region replication
- 99.9% SLA with 99.95% actual uptime
- Public status page with real-time and historical data
- One availability incident in 3 years, transparently handled with post-mortem

**Weaknesses/Gaps:**
- Tabletop exercises conducted annually (semi-annual would be preferred)
- BCP test identified DNS propagation issue (since fixed)

**Evidence Reviewed:**
- IRP executive summary
- Tabletop exercise summary (March 2026)
- Breach notification policy
- BCP/DR test results (March 2026)
- SLA documentation and 12-month uptime report
- Status page
- October 2025 incident post-mortem

---

### 5.6 Governance & Compliance (Score: 3.5 / 5)

**Strengths:**
- Dedicated VP of Security with Board reporting
- SOC 2 Type II report (Security + Availability)
- Annual security awareness training with 94% completion
- Quarterly risk register reviews
- Background checks for all employees (enhanced for sensitive roles)
- $5M cyber liability insurance
- Contractual audit rights

**Weaknesses/Gaps:**
- SOC 2 Type II report contains one exception (access review timeliness, Q3 2025). The issue has been remediated, but the exception exists in the current report.
- ISO 27001 not yet certified (in progress, target Q4 2026)
- Confidentiality criteria not yet included in SOC 2 scope
- CSA STAR Level 1 self-assessment only (not third-party validated)

**Evidence Reviewed:**
- Organization chart
- SOC 2 Type II report (full review)
- Training program description and completion rates
- Risk management policy and risk register summary
- Background check policy
- Insurance certificate
- Contract audit rights language
- ISO 27001 implementation timeline

---

### 5.7 Third-Party/Subprocessor Management (Score: 3.5 / 5)

**Strengths:**
- Public subprocessor list maintained on Trust Center
- 30-day advance notification of subprocessor changes with objection right
- All subprocessors assessed annually with SOC 2/ISO 27001 required
- SCA practices for software dependencies are strong (covered in AppSec)

**Weaknesses/Gaps:**
- No formal supply chain risk management framework beyond SCA and SOC 2 review
- Fourth-party risk acknowledged but not formally managed
- Concentration risk on AWS identified but not formally tracked in a risk register

**Evidence Reviewed:**
- Subprocessor list
- Subprocessor change notification policy
- Subprocessor assessment policy
- Cross-reference to dependency management evidence

---

## 6. Risk Items

### Critical Findings

None identified.

### High Findings

| # | Finding | Domain | Risk | Recommended Remediation | Remediation Deadline |
|---|---------|--------|------|------------------------|---------------------|
| H1 | No 24/7 SOC monitoring | Infrastructure | Time-sensitive security events during off-hours (10pm-8am PT) may be missed or response may be delayed | Vendor should evaluate 24/7 SOC coverage (internal or MSSP). Interim: verify PagerDuty alerting covers all critical detection rules during off-hours. | Track; request update at next annual review |

### Medium Findings

| # | Finding | Domain | Risk | Recommended Remediation | Remediation Deadline |
|---|---------|--------|------|------------------------|---------------------|
| M1 | SOC 2 Type II exception (access review timeliness) | Governance | Indicates a control gap during Q3 2025; while remediated, pattern could recur | Vendor should demonstrate clean SOC 2 Type II report in next period (April 2026 - March 2027) | Next SOC 2 report (expected May 2027) |
| M2 | ISO 27001 not yet certified | Governance | Limited third-party validation of overall ISMS | Track certification progress; request update quarterly | Target: Q4 2026 |
| M3 | No formal threat modeling | AppSec | New features may introduce security risks not identified during design | Vendor should implement systematic threat modeling per their 2026 roadmap | Request update at next annual review |

### Low Findings / Observations

| # | Finding | Domain | Observation |
|---|---------|--------|-------------|
| L1 | Privacy program lacks dedicated professional | Data Protection | Adequate for current scope but should mature as company grows, especially with EU customers |
| L2 | Fourth-party risk not formally managed | Third-Party | Acceptable given maturity level; recommend formalizing as part of ISO 27001 implementation |
| L3 | No bug bounty program | Infrastructure | Pen testing is adequate; bug bounty would provide continuous external testing |
| L4 | SSO restricted to Business/Enterprise plans | Access Control | Not an issue for our engagement but noted as a general observation |

---

## 7. Compensating Controls

| # | Vendor Gap | Compensating Control | Control Owner | Implementation Date |
|---|-----------|---------------------|---------------|-------------------|
| 1 | No 24/7 SOC monitoring | Enable Datadog anomaly detection alerts for our CloudWidget integration; our SOC will monitor vendor-side alerts forwarded via API | James Park (SecOps) | 2026-07-15 |
| 2 | SOC 2 exception on access reviews | Include CloudWidget access review compliance in our quarterly vendor monitoring checklist | Sarah Chen | 2026-07-01 |

---

## 8. Recommendations

### 8.1 Conditions for Approval

1. Vendor must provide updated SOC 2 Type II report when available (expected May 2027); exception must be resolved.
2. Vendor must notify us of any security incidents within 48 hours per DPA terms.
3. ISO 27001 certification progress update requested by Q4 2026.

### 8.2 Contractual Recommendations

- [x] Data Processing Agreement executed
- [x] Security SLA included in contract
- [x] Breach notification clause (within 48 hours)
- [x] Right-to-audit clause included
- [x] Data deletion upon termination clause
- [x] Cyber insurance requirement specified
- [x] Subprocessor notification requirement included
- [ ] Indemnification clause for data breaches -- *Under legal review; vendor standard indemnification has a cap. Acceptable given the data types involved.*

### 8.3 Monitoring Recommendations

| Activity | Frequency |
|----------|-----------|
| Review CloudWidget status page for incidents | Weekly |
| Review SOC 2 report when new report issued | Annually (expected May 2027) |
| Check for CloudWidget security advisories | Monthly |
| Verify DPA and contractual obligations remain current | Annually |
| Review subprocessor list for changes | Quarterly |
| Review API access logs for CloudWidget integration | Quarterly |

---

## 9. Approval

| Role | Name | Decision | Signature | Date |
|------|------|----------|-----------|------|
| Assessor | Sarah Chen | Recommend: Approve with Conditions | S. Chen | 2026-06-10 |
| Security Manager | Mike Torres | [x] Approve w/ Conditions | M. Torres | 2026-06-12 |
| CISO (if High Risk) | N/A (Moderate Risk) | N/A | | |
| Executive (if Critical Risk) | N/A | N/A | | |

---

## 10. Next Review

| Field | Value |
|-------|-------|
| **Next Review Date** | 2027-06-10 |
| **Review Type** | [x] Annual Reassessment |
| **Review Owner** | Sarah Chen |

**Items to verify at next review:**
1. SOC 2 Type II exception resolved in new report
2. ISO 27001 certification status
3. 24/7 SOC monitoring status
4. Threat modeling implementation status
5. Any changes to subprocessor list

---

*This example report is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For more on maintaining compliance evidence between audits, see [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh) on the TrazTech blog.*
