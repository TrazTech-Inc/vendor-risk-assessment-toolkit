# Vendor Risk Scoring Guide

**Detailed Scoring Rubric for Vendor Security Assessments**

**Version:** 1.0  
**Maintained by:** [TrazTech](https://traztech.ca)  
**Compliance Mapping:** SOC 2 CC9.2, CC3.1-CC3.4 | ISO 27001 A.5.19 | NIST CSF ID.SC

---

## Overview

This guide provides a quantitative framework for scoring vendor security assessments. It defines seven security domains, their relative weights, and detailed scoring criteria for each domain on a 1-5 scale.

The scoring methodology is designed to produce a single aggregate risk score that is:
- **Comparable** across vendors
- **Reproducible** across assessors
- **Actionable** for decision-making

This scoring approach is part of TrazTech's vendor risk management methodology. For more on maintaining consistent compliance evidence, see [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh).

---

## Domain Weights

| # | Domain | Weight | Rationale |
|---|--------|--------|-----------|
| 1 | Data Protection & Privacy | 25% | Highest weight: directly impacts data confidentiality and regulatory compliance |
| 2 | Access Control & Authentication | 20% | Second highest: access controls are the primary barrier to unauthorized data access |
| 3 | Infrastructure & Network Security | 15% | Foundational security layer protecting all other controls |
| 4 | Application Security & SDLC | 15% | Reflects security built into the vendor's product |
| 5 | Incident Response & Business Continuity | 10% | Measures ability to detect, respond to, and recover from incidents |
| 6 | Governance & Compliance | 10% | Organizational maturity and commitment to security |
| 7 | Third-Party/Subprocessor Management | 5% | Supply chain risk; lower weight reflects indirect risk |
| | **Total** | **100%** | |

### Adjusting Weights

These weights reflect a general-purpose risk model. You may adjust them based on:

- **Industry requirements:** If you handle PHI, increase Data Protection weight. If you are in financial services, increase Infrastructure weight.
- **Data sensitivity:** If the vendor handles minimal data, reduce Data Protection weight and redistribute.
- **Integration depth:** If the vendor is deeply embedded in your infrastructure, increase Infrastructure and AppSec weights.

When adjusting weights, ensure they still total 100% and document the rationale for the adjustment.

---

## Scoring Scale

| Score | Rating | Definition |
|-------|--------|------------|
| **5** | Excellent | Industry-leading practices. Exceeds common standards. Demonstrates security maturity through advanced controls, continuous improvement, and proactive risk management. |
| **4** | Good | Strong practices. Meets all standard requirements. Has formalized processes, appropriate tooling, and documentation. Minor improvements possible but no material gaps. |
| **3** | Adequate | Meets minimum acceptable standards. Controls exist and are generally effective, but may lack maturity, automation, or consistency. Acceptable for most vendor relationships. |
| **2** | Below Standard | Notable gaps exist. Some controls are in place but are insufficient, inconsistent, or immature. Compensating controls likely needed. Requires remediation plan. |
| **1** | Inadequate | Significant deficiencies. Controls are absent, ineffective, or severely deficient. Material risk to your organization. Engagement not recommended without major remediation. |

---

## Domain 1: Data Protection & Privacy (Weight: 25%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | AES-256 encryption at rest and TLS 1.3 in transit. HSM-backed key management with automated rotation. Formal data classification scheme enforced technically. Comprehensive privacy program with DPO. Data residency controls and customer-managed key options. Immutable access logs retained 12+ months. Automated data lifecycle management. DPIA process for new processing activities. |
| **4** | AES-256 encryption at rest and TLS 1.2+ in transit. Documented key management with rotation schedule. Data classification policy with handling procedures. Named privacy officer. DPA available and meets GDPR Art. 28. Access logs retained 12 months. Data retention policy enforced. |
| **3** | Encryption at rest and in transit using current standards. Basic key management. Data classification exists but enforcement is manual. Privacy addressed within security program. DPA available. Access logging enabled for most systems. General data retention guidelines. |
| **2** | Encryption at rest or in transit has gaps (e.g., some datastores unencrypted). Key management is informal. Limited data classification. No formal privacy program. DPA missing or incomplete. Partial access logging. No data retention enforcement. |
| **1** | No encryption at rest or using deprecated algorithms. No key management. No data classification. No privacy program or DPO. No DPA available. No access logging. Data retained indefinitely. |

### Key Evidence to Request

- Encryption standards documentation
- Key management procedures
- Data classification policy
- Privacy policy and DPO contact
- DPA template
- Sample access log fields (redacted)
- Data retention policy

---

## Domain 2: Access Control & Authentication (Weight: 20%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | MFA enforced for all users (phishing-resistant for admins). SSO via SAML 2.0/OIDC with no SSO tax. SCIM provisioning. Granular RBAC with custom roles and ABAC. Dedicated PAM solution with JIT access. Quarterly access reviews. Automated deprovisioning within 1 hour of termination. API authentication via OAuth 2.0 with scoped tokens. |
| **4** | MFA enforced for all users. SSO supported (SAML/OIDC). SCIM available. RBAC with custom roles. Privileged access managed with separate accounts and logging. Quarterly access reviews. Deprovisioning within 24 hours. API keys rotatable with rate limiting. |
| **3** | MFA available and encouraged (enforced for admins). SSO supported. Predefined RBAC roles. Separate admin accounts. Semi-annual access reviews. Deprovisioning within 48 hours. API key authentication with rotation. |
| **2** | MFA available but not enforced. SSO limited or paywalled. Basic roles (admin/user). Shared admin accounts exist. Annual access reviews or less. Deprovisioning takes days. Static API keys. |
| **1** | No MFA. No SSO support. No RBAC. Shared accounts. No access reviews. No formal offboarding process. Insecure API authentication. |

### Key Evidence to Request

- Authentication configuration documentation
- MFA enforcement statistics
- SSO integration documentation
- RBAC model and role descriptions
- Access review policy and completion evidence
- Offboarding/termination procedure
- API authentication documentation

---

## Domain 3: Infrastructure & Network Security (Weight: 15%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | Major cloud provider with SOC 2 Type II. Zero-trust network architecture. Micro-segmentation. Continuous vulnerability scanning with critical patches in 24h. Annual third-party pen test + bug bounty program. Enterprise DDoS mitigation. 24/7 SOC with SIEM. EDR on all endpoints. MDM enforced. Host-based IDS/IPS. |
| **4** | Major cloud provider. Network segmentation between environments. Weekly vulnerability scanning with critical patches in 48h. Annual third-party pen test with results shared. DDoS mitigation service. SOC coverage with SIEM. EDR deployed. MDM for company devices. |
| **3** | Reputable hosting provider. Basic network segmentation. Monthly vulnerability scanning with critical patches in 30 days. Annual pen test (internal or third-party). Basic DDoS protection. IDS/IPS deployed. Antivirus on endpoints. |
| **2** | Hosting environment not well documented. Limited segmentation. Quarterly scanning or less. Pen testing not annual. Minimal DDoS protection. Limited detection capabilities. Basic endpoint protection. |
| **1** | Self-hosted with limited controls. No network segmentation. No vulnerability scanning. No penetration testing. No DDoS protection. No IDS/IPS. No endpoint security. |

### Key Evidence to Request

- Infrastructure architecture overview
- Network diagram (redacted)
- Vulnerability management policy and patching SLAs
- Most recent pen test executive summary
- DDoS mitigation documentation
- SOC/SIEM overview
- Endpoint security solution description

---

## Domain 4: Application Security & SDLC (Weight: 15%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | Formal SSDLC with security gates at each phase. Mandatory peer review + automated SAST/SCA/DAST in CI/CD. Threat modeling for new features. Dedicated secrets manager with automated rotation. Automated SCA with SBOM maintenance. Formal change management with approval workflows. Strict environment separation with synthetic test data. API gateway with comprehensive security controls. |
| **4** | SSDLC documented. Peer review + automated SAST/SCA before merge. Secrets manager used. SCA scanning automated. Change management with peer review and testing. Environments separated with anonymized non-prod data. API security controls (auth, rate limiting). |
| **3** | Security testing performed (not fully integrated in CI/CD). Peer review required. Secrets in environment variables (not code). SCA scanning performed. Change management process exists. Environments separated. Basic API security. |
| **2** | Ad hoc security testing. Code review inconsistent. Some secrets in config files. Manual dependency tracking. Informal change process. Partial environment separation. Limited API security. |
| **1** | No security testing. No code review. Secrets in source code. No dependency scanning. No change management. No environment separation. No API security controls. |

### Key Evidence to Request

- SSDLC documentation
- CI/CD pipeline security controls
- Code review policy
- Secrets management approach
- SCA tool and process
- Change management policy
- Environment architecture documentation

---

## Domain 5: Incident Response & Business Continuity (Weight: 10%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | Documented IRP tested semi-annually via tabletop exercises. Breach notification within 24 hours. Dedicated incident response team. BCP tested annually with RTO <4h, RPO <1h. DR plan with automated failover tested quarterly. 99.99%+ SLA met. Public status page with history. No major incidents in 3 years (or transparent handling with strong remediation). |
| **4** | Documented IRP tested annually. Breach notification within 48 hours. Incident response team identified. BCP tested annually with RTO <8h, RPO <4h. DR plan tested annually. 99.9% SLA. Public status page. Minor incidents handled transparently. |
| **3** | Documented IRP tested within last 2 years. Breach notification within 72 hours. BCP documented with RTO <24h. DR plan exists and has been tested. 99.5% SLA. Status page available. |
| **2** | Basic IRP exists but not recently tested. Breach notification timeline unclear. BCP exists but RTO >24h. DR plan not tested. No formal SLA. |
| **1** | No IRP. No breach notification commitment. No BCP. No DR plan. Frequent outages. History of poorly handled incidents. |

### Key Evidence to Request

- Incident response plan (or summary)
- Most recent tabletop exercise date and summary
- Breach notification policy
- BCP/DR plan summary with RTO/RPO
- Most recent DR test results
- SLA documentation and historical uptime
- Status page URL
- Incident history disclosure

---

## Domain 6: Governance & Compliance (Weight: 10%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | Dedicated CISO reporting to CEO/Board. SOC 2 Type II with clean opinion (Security + Availability + Confidentiality). ISO 27001 certified. Additional relevant certifications (PCI DSS, HIPAA, CSA STAR). Annual security awareness training with >95% completion and phishing simulations. Formal risk management framework with quarterly risk reviews. Comprehensive background checks. Cyber insurance >$5M. Contractual audit rights. |
| **4** | Dedicated security leader. SOC 2 Type II with clean opinion. ISO 27001 certified or in progress. Annual training with >90% completion. Documented risk management. Background checks for all employees. Cyber insurance with adequate coverage. Audit rights in contract. |
| **3** | Named security responsible person. SOC 2 Type II (or Type I with Type II planned). Security training with >80% completion. Risk assessment performed. Background checks for sensitive roles. General liability + some cyber coverage. SOC 2 provided in lieu of audit rights. |
| **2** | Security responsibilities distributed. SOC 2 in progress or not available. Inconsistent training. Ad hoc risk management. Limited background checks. Minimal insurance. Limited audit accommodation. |
| **1** | No security leadership. No SOC 2 or ISO 27001. No security training. No risk management. No background checks. No cyber insurance. No audit rights. |

### Key Evidence to Request

- Organization chart showing security leadership
- SOC 2 Type II report
- ISO 27001 certificate
- Additional certifications
- Training program description and completion rates
- Risk management policy
- Background check policy
- Insurance certificate
- Contract audit rights language

---

## Domain 7: Third-Party/Subprocessor Management (Weight: 5%)

### Scoring Criteria

| Score | Criteria |
|-------|----------|
| **5** | Complete subprocessor list publicly available. 30+ day advance notification of changes with objection right. All subprocessors assessed annually with SOC 2/ISO 27001 required. Same data protection obligations flow down contractually. Formal supply chain risk management with SBOM. Fourth-party risk explicitly addressed. |
| **4** | Subprocessor list provided on request. 30-day notification of changes. Subprocessors assessed with security requirements in contracts. SOC 2 reports reviewed. Dependencies scanned. Major fourth-party risks identified. |
| **3** | Subprocessor list available but may not be current. Notification of changes provided. Major subprocessors assessed. Security requirements in contracts. Dependencies tracked. |
| **2** | Partial subprocessor visibility. Limited notification of changes. Informal subprocessor assessment. Limited contractual requirements. Limited supply chain visibility. |
| **1** | No subprocessor list. No notification of changes. No subprocessor assessment. No contractual security requirements. No supply chain management. |

### Key Evidence to Request

- Current subprocessor list
- Subprocessor change notification policy
- Subprocessor assessment methodology
- Contractual flow-down requirements
- SCA/SBOM practices
- Fourth-party risk considerations

---

## Aggregate Risk Calculation

### Formula

```
Aggregate Score = (D1 x 0.25) + (D2 x 0.20) + (D3 x 0.15) + (D4 x 0.15) + (D5 x 0.10) + (D6 x 0.10) + (D7 x 0.05)

Where:
  D1 = Data Protection & Privacy score (1-5)
  D2 = Access Control & Authentication score (1-5)
  D3 = Infrastructure & Network Security score (1-5)
  D4 = Application Security & SDLC score (1-5)
  D5 = Incident Response & Business Continuity score (1-5)
  D6 = Governance & Compliance score (1-5)
  D7 = Third-Party/Subprocessor Management score (1-5)
```

### Example Calculation

| Domain | Weight | Score | Weighted |
|--------|--------|-------|----------|
| Data Protection & Privacy | 0.25 | 4 | 1.00 |
| Access Control & Authentication | 0.20 | 4 | 0.80 |
| Infrastructure & Network Security | 0.15 | 3 | 0.45 |
| Application Security & SDLC | 0.15 | 3 | 0.45 |
| Incident Response & BCP | 0.10 | 4 | 0.40 |
| Governance & Compliance | 0.10 | 4 | 0.40 |
| Third-Party Management | 0.05 | 3 | 0.15 |
| **Aggregate** | **1.00** | | **3.65** |

Result: 3.65 = **Moderate Risk** (Approve with conditions)

---

## Risk Rating Thresholds

| Weighted Score | Risk Rating | Color | Action |
|---------------|-------------|-------|--------|
| **4.0 - 5.0** | Low Risk | Green | Approve. Standard monitoring per tier schedule. |
| **3.0 - 3.9** | Moderate Risk | Yellow | Approve with conditions. Enhanced monitoring. Address gaps identified in assessment. |
| **2.0 - 2.9** | High Risk | Orange | Requires CISO/VP risk acceptance. Compensating controls required. Reassess quarterly until improved. |
| **1.0 - 1.9** | Critical Risk | Red | Do not approve without executive sign-off. Detailed remediation plan required. Consider alternative vendors. |

---

## Compensating Controls Guidance

When a vendor scores below acceptable thresholds in specific domains, compensating controls can reduce residual risk. Compensating controls are measures your organization implements to address vendor gaps.

### Common Compensating Controls by Domain

| Domain Gap | Compensating Control Examples |
|-----------|------------------------------|
| **Weak encryption** | Encrypt data before sending to vendor; use customer-managed keys; minimize data shared |
| **No MFA available** | Restrict access to named individuals; use a VPN or IP allowlist; implement session monitoring |
| **No SOC 2/ISO 27001** | Conduct your own assessment; require additional evidence; increase monitoring frequency |
| **Weak access controls** | Minimize data access; implement monitoring on your side; use separate service accounts |
| **No incident response plan** | Include vendor in your incident response plan; define notification requirements contractually |
| **No DPA** | Include data protection terms in the MSA; document processing activities internally |
| **Poor subprocessor management** | Limit data types shared; require notification of subprocessor changes contractually |
| **Weak SDLC** | Perform your own security testing of vendor's interface; limit integration depth |

### Compensating Controls Documentation

For each compensating control, document:
1. **The vendor gap** it addresses
2. **The control description** (what you will do)
3. **The control owner** (who is responsible)
4. **Implementation timeline**
5. **Effectiveness criteria** (how you know it is working)
6. **Review frequency**

---

## Scoring Tips for Assessors

1. **Be consistent.** Use the same scoring criteria across all vendors. If in doubt, refer to the specific criteria in this guide rather than gut feeling.

2. **Evidence over claims.** A vendor saying "we encrypt everything" without providing encryption standards documentation should score lower than a vendor who provides their encryption policy.

3. **Give credit for transparency.** A vendor who honestly discloses gaps and has a remediation timeline should score higher than one that gives vague, noncommittal answers.

4. **N/A is acceptable.** If a domain genuinely does not apply to the vendor relationship (e.g., AI/ML questions for a vendor that does not use AI), mark it N/A and redistribute the weight proportionally.

5. **Document your rationale.** For any score that is not obvious, write a brief note explaining why you chose that score. This helps with consistency across assessors and audit defense.

6. **Consider the trend.** If a vendor has improved significantly since the last assessment, note this. A vendor moving from 2 to 3 shows commitment to improvement.

7. **Do not inflate scores.** A score of 3 ("Adequate") is acceptable for most vendor relationships. Reserve 4 and 5 for vendors that genuinely demonstrate strong or exceptional practices.

---

## Redistributing Weight for N/A Domains

If a domain is not applicable, redistribute its weight proportionally:

```
Adjusted Weight = Original Weight / (1 - Sum of N/A Weights)
```

**Example:** If Domain 7 (Third-Party Management, 5%) is N/A:

| Domain | Original Weight | Adjusted Weight |
|--------|----------------|-----------------|
| Data Protection | 25% | 25/95 = 26.3% |
| Access Control | 20% | 20/95 = 21.1% |
| Infrastructure | 15% | 15/95 = 15.8% |
| AppSec | 15% | 15/95 = 15.8% |
| IR/BCP | 10% | 10/95 = 10.5% |
| Governance | 10% | 10/95 = 10.5% |
| Third-Party | N/A | 0% |
| **Total** | **95%** | **100%** |

---

*This scoring guide is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For a free SOC 2 readiness checklist, visit [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*
