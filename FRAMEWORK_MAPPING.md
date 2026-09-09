# Framework Compliance Mapping

**Mapping every toolkit component to compliance framework requirements.**

**Version:** 1.0  
**Maintained by:** [TrazTech](https://traztech.ca)

---

## Overview

This document maps each component of the Vendor Risk Assessment Toolkit to the specific requirements it satisfies across six major compliance frameworks. Use this mapping to demonstrate to auditors exactly how your vendor risk management program addresses their requirements.

This mapping reflects the approach TrazTech uses when preparing clients for SOC 2 and ISO 27001 audits. For more on maintaining audit-ready evidence, see [Keeping Evidence Fresh](https://traztech.ca/blog/keeping-evidence-fresh) and [Control Drift Between Audits](https://traztech.ca/blog/control-drift-between-audits) on the TrazTech blog.

---

## Framework Quick Reference

| Framework | Key Requirements | Focus Area |
|-----------|-----------------|------------|
| **SOC 2** | CC9.2, CC3.1-CC3.4, CC6.1 | Risk assessment and monitoring of vendors/business partners |
| **ISO 27001:2022** | A.5.19, A.5.20, A.5.21, A.5.22 | Supplier relationship security management |
| **HIPAA** | 164.308(b), 164.314(a) | Business associate contracts and arrangements |
| **PCI DSS v4.0** | 12.8, 12.9 | Service provider management |
| **NIST CSF** | ID.SC-1 through ID.SC-5 | Supply chain risk management |
| **GDPR** | Art. 28, Art. 32, Art. 44-49 | Processor obligations and security |

---

## SOC 2 Trust Services Criteria Mapping

### CC9.2: Risk Assessment and Management of Vendors and Business Partners

*"The entity assesses and manages risks associated with vendors and business partners."*

| Toolkit Component | How It Addresses CC9.2 |
|-------------------|----------------------|
| `methodology/VENDOR_RISK_FRAMEWORK.md` | Defines the complete vendor risk management framework, including tiering methodology, assessment requirements, scoring, risk acceptance, and ongoing monitoring |
| `templates/vendor-inventory.csv` | Provides a structured inventory of all vendors with risk scores, review dates, and compliance status: evidence of vendor tracking |
| `templates/vendor-security-questionnaire.md` | Standardized assessment instrument for evaluating vendor security posture across all relevant domains |
| `templates/vendor-risk-assessment-report.md` | Documents assessment findings, risk scores, and approval decisions: primary audit evidence |
| `templates/vendor-due-diligence-checklist.md` | Ensures consistent pre-onboarding due diligence for all new vendors |
| `templates/vendor-offboarding-checklist.md` | Ensures secure vendor termination with access revocation and data deletion |
| `scoring/risk-scoring-guide.md` | Quantitative, reproducible scoring methodology demonstrating rigor in vendor assessment |
| `automation/vendor_tracker.py` | Automated monitoring for overdue reviews and compliance gaps: evidence of ongoing management |

### CC3.1: CC3.4 (Risk Assessment)

| Criteria | Toolkit Component | Coverage |
|----------|-------------------|----------|
| **CC3.1**: Specifies suitable objectives | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 1 (Purpose) | Defines objectives for vendor risk management |
| **CC3.2**: Identifies and analyzes risk | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 3 (Tiering), Section 5 (Scoring) | Risk identification through tiering; risk analysis through domain scoring |
| **CC3.3**: Considers fraud risk | `templates/vendor-security-questionnaire.md` Section A (Background checks), Section C (Access controls) | Addresses insider threat and fraud risk through vendor controls assessment |
| **CC3.4**: Identifies and assesses changes | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4.2 (Trigger events), Section 7 (Ongoing monitoring) | Trigger-based reviews for material changes; continuous monitoring activities |

### CC6.1: Logical and Physical Access Controls

| Toolkit Component | Coverage |
|-------------------|----------|
| `templates/vendor-security-questionnaire.md` Section C (Access Control) | Assesses vendor access control and authentication practices |
| `templates/vendor-security-questionnaire.md` Section D (Infrastructure) | Assesses vendor physical and network security |

### CC7.2: Monitoring of System Components

| Toolkit Component | Coverage |
|-------------------|----------|
| `methodology/VENDOR_RISK_FRAMEWORK.md` Section 7 (Ongoing Monitoring) | Defines monitoring activities and frequencies for vendor oversight |
| `automation/vendor_tracker.py` | Automated monitoring for overdue reviews and compliance gaps |

### CC8.1: Change Management

| Toolkit Component | Coverage |
|-------------------|----------|
| `templates/vendor-security-questionnaire.md` Section E (AppSec & SDLC) | Assesses vendor change management processes |

### A1.2: Recovery from Disruptions

| Toolkit Component | Coverage |
|-------------------|----------|
| `templates/vendor-security-questionnaire.md` Section F (IR & BCP) | Assesses vendor business continuity and disaster recovery capabilities |

---

## ISO 27001:2022 Annex A Mapping

### A.5.19: Information Security in Supplier Relationships

*"Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier's products or services."*

| Toolkit Component | How It Addresses A.5.19 |
|-------------------|------------------------|
| `methodology/VENDOR_RISK_FRAMEWORK.md` | Complete framework for managing supplier security risks |
| `templates/vendor-security-questionnaire.md` | Standardized assessment of supplier security posture |
| `scoring/risk-scoring-guide.md` | Quantitative risk evaluation methodology |
| `templates/vendor-risk-assessment-report.md` | Documentation of assessment findings and risk ratings |
| `templates/vendor-due-diligence-checklist.md` | Pre-engagement security evaluation process |
| `templates/vendor-inventory.csv` | Registry of all supplier relationships with risk status |

### A.5.20: Addressing Information Security Within Supplier Agreements

*"Relevant information security requirements shall be established and agreed with each supplier based on the type of supplier relationship."*

| Toolkit Component | How It Addresses A.5.20 |
|-------------------|------------------------|
| `templates/data-processing-agreement-checklist.md` | Ensures DPAs contain all required security and privacy provisions |
| `templates/vendor-due-diligence-checklist.md` Section 3 (Legal/Contractual) | Checklist for contractual security requirements (NDA, SLA, DPA, BAA) |
| `templates/vendor-risk-assessment-report.md` Section 8 (Recommendations) | Contractual recommendations based on assessment findings |
| `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4 (Assessment Requirements) | Defines contractual requirements by vendor tier |

### A.5.21: Managing Information Security in the ICT Supply Chain

*"Processes and procedures shall be defined and implemented to manage information security risks associated with the ICT products and services supply chain."*

| Toolkit Component | How It Addresses A.5.21 |
|-------------------|------------------------|
| `templates/vendor-security-questionnaire.md` Section G (Third-Party Management) | Assesses vendor's own subprocessor and supply chain management |
| `scoring/risk-scoring-guide.md` Domain 7 (Third-Party/Subprocessor Management) | Scoring criteria for supply chain risk management |
| `templates/vendor-security-questionnaire.md` Section E (AppSec - E3 Dependencies) | Assesses software supply chain security (SCA, SBOM) |

### A.5.22: Monitoring, Review and Change Management of Supplier Services

*"The organization shall regularly monitor, review and manage changes to supplier information security practices and service delivery."*

| Toolkit Component | How It Addresses A.5.22 |
|-------------------|------------------------|
| `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4.2 (Assessment Frequency) | Defines review schedules by vendor tier |
| `methodology/VENDOR_RISK_FRAMEWORK.md` Section 7 (Ongoing Monitoring) | Continuous monitoring activities and trigger events |
| `automation/vendor_tracker.py` | Automated tracking of review schedules and overdue assessments |
| `templates/vendor-inventory.csv` | Tracks last review date and next review date for each vendor |

### Additional ISO 27001 Controls Addressed

| Control | Toolkit Component | Coverage |
|---------|-------------------|----------|
| **A.5.1** (Policies) | `methodology/VENDOR_RISK_FRAMEWORK.md` | Serves as vendor risk management policy |
| **A.5.12-A.5.13** (Data classification) | Questionnaire B1 | Assesses vendor data classification |
| **A.5.15-A.5.18** (Access control) | Questionnaire C1-C8 | Assesses vendor access controls |
| **A.5.24-A.5.28** (Incident management) | Questionnaire F1-F6 | Assesses vendor incident response |
| **A.5.29-A.5.30** (Business continuity) | Questionnaire F3-F4 | Assesses vendor BCP/DR |
| **A.5.31** (Legal/regulatory) | Questionnaire H4 | Assesses vendor regulatory compliance |
| **A.5.34** (Privacy) | Questionnaire B8-B9 | Assesses vendor privacy program |
| **A.6.1** (Screening) | Questionnaire A5 | Assesses vendor background checks |
| **A.6.3** (Training) | Questionnaire A3 | Assesses vendor security training |
| **A.7.1-A.7.14** (Physical) | Questionnaire D8 | Assesses vendor physical security |
| **A.8.5** (Authentication) | Questionnaire C1-C2, C6-C8 | Assesses vendor authentication controls |
| **A.8.8** (Vulnerability mgmt) | Questionnaire D3-D4 | Assesses vendor vulnerability management |
| **A.8.10** (Data deletion) | Questionnaire B4 | Assesses vendor data retention/disposal |
| **A.8.13** (Backup) | Questionnaire B6 | Assesses vendor backup procedures |
| **A.8.15** (Logging) | Questionnaire B7 | Assesses vendor logging capabilities |
| **A.8.20** (Network security) | Questionnaire D1-D2, D5 | Assesses vendor network controls |
| **A.8.24** (Cryptography) | Questionnaire B2-B3, E7 | Assesses vendor encryption and secrets management |
| **A.8.25-A.8.28** (SDLC) | Questionnaire E1-E7 | Assesses vendor secure development practices |
| **A.8.31** (Dev/prod separation) | Questionnaire E5 | Assesses vendor environment separation |
| **A.8.32** (Change mgmt) | Questionnaire E4 | Assesses vendor change management |

---

## HIPAA Mapping

### 164.308(b): Business Associate Contracts and Other Arrangements

*"A covered entity may permit a business associate to create, receive, maintain, or transmit electronic protected health information on the covered entity's behalf only if the covered entity obtains satisfactory assurances."*

| Toolkit Component | How It Addresses 164.308(b) |
|-------------------|-----------------------------|
| `templates/vendor-due-diligence-checklist.md` Section 3 | Includes BAA execution as a checklist item for vendors handling PHI |
| `templates/data-processing-agreement-checklist.md` | DPA review checklist applicable to BAA review (similar requirements) |
| `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4 | Assessment requirements include BAA for applicable vendors |
| `templates/vendor-security-questionnaire.md` | Assesses vendor security safeguards relevant to PHI protection |

### 164.314(a): Business Associate Contract Requirements

| Toolkit Component | Coverage |
|-------------------|----------|
| `templates/data-processing-agreement-checklist.md` | Covers security measures, breach notification, data return/deletion: all required BAA elements |
| `templates/vendor-risk-assessment-report.md` Section 8.2 | Recommends contractual protections including breach notification and data handling |

### Additional HIPAA Controls

| HIPAA Requirement | Toolkit Component | Coverage |
|-------------------|-------------------|----------|
| **164.308(a)(1)**: Security management | Questionnaire A2, A4 | Assesses vendor security policies and risk management |
| **164.308(a)(3)**: Workforce security | Questionnaire A5 | Assesses vendor background checks |
| **164.308(a)(5)**: Security training | Questionnaire A3 | Assesses vendor security awareness training |
| **164.308(a)(6)**: Incident response | Questionnaire F1-F2 | Assesses vendor incident response and breach notification |
| **164.308(a)(7)**: Contingency plan | Questionnaire B6, F3-F4 | Assesses vendor backup, BCP, and DR |
| **164.310(a)-(c)**: Physical safeguards | Questionnaire D8 | Assesses vendor physical security |
| **164.310(d)**: Device controls | Questionnaire D7 | Assesses vendor endpoint security |
| **164.312(a)(1)**: Access controls | Questionnaire B1, C3, C5 | Assesses vendor data access and RBAC |
| **164.312(b)**: Audit controls | Questionnaire B7 | Assesses vendor logging and audit trails |
| **164.312(d)**: Authentication | Questionnaire C1 | Assesses vendor authentication mechanisms |
| **164.312(e)(1)**: Transmission security | Questionnaire B3 | Assesses vendor encryption in transit |
| **164.408-164.410**: Breach notification | Questionnaire F2 | Assesses vendor breach notification process |

---

## PCI DSS v4.0 Mapping

### Requirement 12.8: Service Provider Management

*"Risk to information assets associated with service provider relationships is managed."*

| PCI DSS 12.8.x | Toolkit Component | Coverage |
|-----------------|-------------------|----------|
| **12.8.1**: List of service providers with description | `templates/vendor-inventory.csv` | Maintains vendor list with services, data access, and status |
| **12.8.2**: Written agreements with acknowledgment of responsibilities | `templates/data-processing-agreement-checklist.md`, Due Diligence Checklist Section 3 | Contractual review ensuring security responsibilities are defined |
| **12.8.3**: Established process for engaging service providers including due diligence | `templates/vendor-due-diligence-checklist.md`, `methodology/VENDOR_RISK_FRAMEWORK.md` | Complete onboarding and assessment process |
| **12.8.4**: Monitor service providers' PCI DSS compliance at least annually | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4.2, Section 7 | Assessment frequency and monitoring requirements |
| **12.8.5**: Maintain information about which PCI DSS requirements are managed by each provider | `templates/vendor-risk-assessment-report.md` | Documents vendor's security responsibilities and coverage |

### Requirement 12.9: Service Provider Acknowledgment

| PCI DSS 12.9.x | Toolkit Component | Coverage |
|-----------------|-------------------|----------|
| **12.9.1**: Service provider acknowledges responsibility | `templates/data-processing-agreement-checklist.md` | Contractual review for responsibility acknowledgment |
| **12.9.2**: Service provider supports customer compliance requests | Questionnaire H5 (Audit Rights) | Assesses vendor willingness to support compliance |

### Additional PCI DSS Controls

| PCI DSS Requirement | Toolkit Component | Coverage |
|---------------------|-------------------|----------|
| **3.4-3.6**: Protect stored cardholder data / Key management | Questionnaire B2, E7 | Assesses encryption and key/secrets management |
| **4.1**: Encrypt transmissions | Questionnaire B3 | Assesses encryption in transit |
| **6.1-6.2**: Vulnerability management | Questionnaire D3 | Assesses vulnerability scanning and patching |
| **6.3-6.5**: Secure development | Questionnaire E1-E4 | Assesses secure SDLC practices |
| **6.4**: Change management | Questionnaire E4 | Assesses change control processes |
| **7.1-7.2**: Access controls | Questionnaire C3-C4 | Assesses RBAC and privileged access |
| **8.1-8.3**: Authentication | Questionnaire C1, C5-C6 | Assesses authentication and access management |
| **9.1-9.4**: Physical security | Questionnaire D8 | Assesses physical access controls |
| **10.1-10.3**: Logging | Questionnaire B7 | Assesses audit logging |
| **11.3**: Penetration testing | Questionnaire D4 | Assesses pen testing program |
| **11.4**: IDS/IPS | Questionnaire D6 | Assesses intrusion detection |
| **12.6**: Security awareness | Questionnaire A3 | Assesses security training |
| **12.10**: Incident response | Questionnaire F1, F4 | Assesses IR and DR plans |

---

## NIST Cybersecurity Framework (CSF) Mapping

### ID.SC: Supply Chain Risk Management

| NIST CSF Control | Toolkit Component | Coverage |
|------------------|-------------------|----------|
| **ID.SC-1**: Supply chain risk management processes are identified, established, assessed, managed, and agreed to by organizational stakeholders | `methodology/VENDOR_RISK_FRAMEWORK.md` | Complete vendor risk management framework with defined processes |
| **ID.SC-2**: Suppliers and third-party partners of information systems, components, and services are identified, prioritized, and assessed using a cyber supply chain risk assessment process | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 3 (Tiering), `templates/vendor-inventory.csv` | Risk-based vendor tiering and inventory |
| **ID.SC-3**: Contracts with suppliers and third-party partners are used to implement appropriate measures designed to meet the objectives of an organization's cybersecurity program and Cyber Supply Chain Risk Management Plan | `templates/data-processing-agreement-checklist.md`, Due Diligence Checklist Section 3 | Contractual security requirements review |
| **ID.SC-4**: Suppliers and third-party partners are routinely assessed using audits, test results, or other forms of evaluations to confirm they are meeting their contractual obligations | `methodology/VENDOR_RISK_FRAMEWORK.md` Section 4.2, Section 7, `automation/vendor_tracker.py` | Assessment frequency, monitoring, and automated tracking |
| **ID.SC-5**: Response and recovery planning and testing are conducted with suppliers and critical third-party providers | Questionnaire F1-F6, `methodology/VENDOR_RISK_FRAMEWORK.md` Section 7 | Assesses vendor IR/BCP and defines monitoring |

### Additional NIST CSF Controls

| NIST CSF | Toolkit Component | Coverage |
|----------|-------------------|----------|
| **ID.RA**: Risk Assessment | `scoring/risk-scoring-guide.md`, `methodology/VENDOR_RISK_FRAMEWORK.md` Section 5 | Quantitative vendor risk assessment methodology |
| **PR.AC**: Access Control | Questionnaire Section C | Assesses vendor access control practices |
| **PR.IP-12**: Vulnerability management | Questionnaire D3, E1, E3 | Assesses vendor vulnerability management and SDLC |
| **DE.CM-8**: Vulnerability scans | Questionnaire D3-D4 | Assesses vendor scanning and pen testing |
| **RS.RP**: Response planning | Questionnaire F1 | Assesses vendor incident response planning |

---

## GDPR Mapping

### Article 28: Processor

*"Where processing is to be carried out on behalf of a controller, the controller shall use only processors providing sufficient guarantees to implement appropriate technical and organisational measures."*

| GDPR Art. 28 Paragraph | Toolkit Component | Coverage |
|------------------------|-------------------|----------|
| **28(1)**: Use only processors with sufficient guarantees | `templates/vendor-security-questionnaire.md`, `scoring/risk-scoring-guide.md` | Assessment of vendor security posture provides evidence of due diligence |
| **28(2)**: Prior authorization for subprocessors | `templates/data-processing-agreement-checklist.md` Section 5, Questionnaire G1-G3 | DPA subprocessor requirements and vendor subprocessor assessment |
| **28(3)(a)**: Process only on documented instructions | `templates/data-processing-agreement-checklist.md` Section 2 | DPA processing instructions review |
| **28(3)(b)**: Confidentiality obligations | `templates/data-processing-agreement-checklist.md` Section 3 | DPA confidentiality provisions review |
| **28(3)(c)**: Security measures (Art. 32) | `templates/data-processing-agreement-checklist.md` Section 4, Full Questionnaire | DPA security measures and comprehensive security assessment |
| **28(3)(d)**: Subprocessor obligations | `templates/data-processing-agreement-checklist.md` Section 5 | DPA subprocessor flow-down requirements |
| **28(3)(e)**: Assist with data subject rights | `templates/data-processing-agreement-checklist.md` Section 6 | DPA data subject rights assistance provisions |
| **28(3)(f)**: Assist with Art. 32-36 obligations | `templates/data-processing-agreement-checklist.md` Section 7 | DPA breach notification, DPIA, and consultation assistance |
| **28(3)(g)**: Data return/deletion after termination | `templates/data-processing-agreement-checklist.md` Section 8, `templates/vendor-offboarding-checklist.md` | DPA data return/deletion terms and offboarding procedures |
| **28(3)(h)**: Audit rights | `templates/data-processing-agreement-checklist.md` Section 9, Questionnaire H5 | DPA audit rights and vendor audit accommodation |
| **28(4)**: Subprocessor same obligations | `templates/data-processing-agreement-checklist.md` Section 5 | DPA subprocessor obligation flow-down |

### Article 32: Security of Processing

| Toolkit Component | Coverage |
|-------------------|----------|
| `templates/vendor-security-questionnaire.md` | Comprehensive security assessment covering all Art. 32 elements (encryption, confidentiality, integrity, availability, resilience, testing) |
| `scoring/risk-scoring-guide.md` | Quantitative evaluation of security adequacy |

### Articles 33-34: Breach Notification

| Toolkit Component | Coverage |
|-------------------|----------|
| Questionnaire F2 (Breach Notification) | Assesses vendor's breach notification capabilities and timelines |
| `templates/data-processing-agreement-checklist.md` Section 7 | Ensures DPA includes breach notification assistance obligations |

### Articles 44-49: International Transfers

| Toolkit Component | Coverage |
|-------------------|----------|
| Questionnaire B5 (Data Residency and Transfer) | Assesses data locations and transfer mechanisms |
| `templates/data-processing-agreement-checklist.md` Section 10 | Ensures DPA includes appropriate transfer safeguards (SCCs, adequacy) |

### Additional GDPR Articles

| GDPR Article | Toolkit Component | Coverage |
|-------------|-------------------|----------|
| **Art. 6** (Lawful processing) | Questionnaire I2 | Assesses legal basis for AI/ML training data usage |
| **Art. 13-14** (Information provision) | Questionnaire I5 | Assesses AI transparency |
| **Art. 17** (Right to erasure) | Questionnaire B4, DPA Checklist Section 6 | Data deletion and data subject rights |
| **Art. 22** (Automated decisions) | Questionnaire I1, I3 | Assesses automated decision-making controls |
| **Art. 37-39** (DPO) | Questionnaire B8 | Assesses vendor privacy program and DPO |

---

## PIPEDA Mapping

While PIPEDA does not have the same prescriptive requirements as GDPR, the toolkit addresses PIPEDA's fair information principles:

| PIPEDA Principle | Toolkit Component | Coverage |
|-----------------|-------------------|----------|
| **Principle 1** (Accountability) | `methodology/VENDOR_RISK_FRAMEWORK.md`, `templates/data-processing-agreement-checklist.md` | Organization remains accountable for data transferred to processors; DPA ensures comparable protection |
| **Principle 3** (Consent) | Questionnaire I2 | Assesses consent mechanisms for AI/ML data usage |
| **Principle 4.1.3** (Third-party processing) | Full Toolkit | Entire toolkit ensures accountability for data processed by third parties |
| **Principle 5** (Limiting use/retention) | Questionnaire B4, DPA Checklist Section 8 | Assesses data retention and disposal practices |
| **Principle 7** (Safeguards) | `templates/vendor-security-questionnaire.md`, DPA Checklist Section 4 | Comprehensive assessment of security safeguards |
| **Principle 9** (Individual access) | DPA Checklist Section 6 | Ensures processor assists with access requests |
| **Breach Regulations** | Questionnaire F2, DPA Checklist Section 7 | Assesses breach notification capabilities |

---

## Cross-Reference Matrix

This matrix shows which toolkit files address which framework requirements at a glance.

| Toolkit File | SOC 2 | ISO 27001 | HIPAA | PCI DSS | NIST CSF | GDPR |
|-------------|-------|-----------|-------|---------|----------|------|
| `VENDOR_RISK_FRAMEWORK.md` | CC9.2, CC3.1-CC3.4, CC7.2 | A.5.19, A.5.22 | 164.308(b) | 12.8.3, 12.8.4 | ID.SC-1, ID.SC-2, ID.SC-4 | Art. 28(1) |
| `vendor-inventory.csv` | CC9.2 | A.5.19 | 164.308(b) | 12.8.1 | ID.SC-2 | Art. 28(1) |
| `vendor-security-questionnaire.md` | CC9.2, CC6.1, CC8.1 | A.5.19, A.5.21, A.5.22 | 164.308-164.312 | 12.8.2, 3-11 | ID.SC-2, ID.SC-5 | Art. 28(1), Art. 32 |
| `vendor-risk-assessment-report.md` | CC9.2, CC3.2 | A.5.19 | 164.308(b) | 12.8.5 | ID.SC-2 | Art. 28(1) |
| `vendor-due-diligence-checklist.md` | CC9.2 | A.5.19, A.5.20 | 164.308(b), 164.314 | 12.8.3 | ID.SC-1, ID.SC-3 | Art. 28 |
| `data-processing-agreement-checklist.md` | CC9.2 | A.5.20 | 164.314 | 12.8.2, 12.9.1 | ID.SC-3 | Art. 28(3) |
| `vendor-offboarding-checklist.md` | CC9.2 | A.5.19, A.5.20 | 164.308(b) | 12.8 | ID.SC-1 | Art. 28(3)(g) |
| `risk-scoring-guide.md` | CC3.2, CC9.2 | A.5.19 | 164.308(a)(1) | 12.8 | ID.RA, ID.SC-2 | Art. 28(1) |
| `vendor_tracker.py` | CC9.2, CC7.2 | A.5.22 | 164.308(b) | 12.8.4 | ID.SC-4 | Art. 28(1) |

---

## Using This Mapping During Audits

### SOC 2 Audit

When your SOC 2 auditor examines CC9.2, present:
1. The `VENDOR_RISK_FRAMEWORK.md` as your vendor risk management policy
2. Completed `vendor-risk-assessment-report.md` files as evidence of vendor assessments
3. The `vendor-inventory.csv` showing all vendors, tiers, and review dates
4. Output from `vendor_tracker.py` showing no overdue reviews

### ISO 27001 Audit

For ISO 27001 A.5.19-A.5.22:
1. `VENDOR_RISK_FRAMEWORK.md` demonstrates your supplier security policy (A.5.19)
2. Completed `data-processing-agreement-checklist.md` files demonstrate contractual requirements (A.5.20)
3. Questionnaire Section G responses demonstrate ICT supply chain management (A.5.21)
4. `vendor_tracker.py` output and monitoring records demonstrate ongoing review (A.5.22)

### HIPAA Audit

For 164.308(b) and 164.314:
1. Completed `vendor-due-diligence-checklist.md` with BAA execution evidence
2. `vendor-risk-assessment-report.md` for each business associate
3. `vendor-inventory.csv` listing all business associates

For detailed compliance calendar planning including vendor review scheduling, see [Compliance Calendar: What Actually Recurs](https://traztech.ca/blog/compliance-calendar-what-actually-recurs) on the TrazTech blog.

---

*This mapping is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). TrazTech has achieved zero exceptions on SOC 2 Type II audits across 76 controls. For a free SOC 2 readiness checklist, visit [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*
