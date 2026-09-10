# Vendor Security Questionnaire

**Version:** 1.0  
**Maintained by:** [TrazTech](https://traztech.ca)  
**Compliance Mapping:** SOC 2 CC9.2 | ISO 27001 A.5.19-A.5.22 | HIPAA 164.308(b) | PCI DSS 12.8 | GDPR Art. 28, 32

---

## Instructions

This questionnaire is used to assess the security posture of third-party vendors. It should be completed by the vendor's security or IT leadership and returned with supporting evidence as indicated.

**For the assessor:** Each question includes:
- The question text
- Expected evidence (what the vendor should provide)
- Scoring guidance (1-5 scale)
- Compliance framework mapping (which framework requires this)

**Scoring Scale:**
| Score | Meaning |
|-------|---------|
| 5 | Excellent: Industry-leading, exceeds requirements |
| 4 | Good: Strong practices, meets all requirements |
| 3 | Adequate: Meets minimum requirements |
| 2 | Below Standard: Gaps exist, compensating controls may be needed |
| 1 | Inadequate: Significant deficiencies, material risk |
| N/A | Not applicable to this vendor relationship |

**Tier applicability:**
- Tier 1 (Critical) and Tier 2 (High): Complete all sections
- Tier 3 (Medium): Complete Sections A, B, C, F, H only
- Tier 4 (Low): Self-attestation; this questionnaire is not required

---

## Vendor Information

| Field | Response |
|-------|----------|
| Vendor Name | |
| Primary Contact Name | |
| Primary Contact Email | |
| Primary Contact Title | |
| Date Completed | |
| Vendor Website | |
| Headquarters Location | |
| Year Founded | |
| Number of Employees | |
| Description of Services Provided | |
| Data Types Accessed/Processed | |

---

## Section A: Company Overview and Governance

### A1. Organizational Security Leadership

**Question:** Does your organization have a dedicated Chief Information Security Officer (CISO) or equivalent security leadership role? If so, who does this role report to?

**Expected Evidence:** Organization chart showing security leadership reporting structure.

**Scoring Guidance:**
- 5: Dedicated CISO reporting to CEO/Board; mature security organization
- 4: Dedicated security leader (VP/Director level) with clear authority
- 3: Security responsibility assigned to a named individual (e.g., CTO wears both hats)
- 2: Security responsibilities distributed without clear ownership
- 1: No identifiable security leadership

**Framework Mapping:** ISO 27001 A.5.1, SOC 2 CC1.1

---

### A2. Information Security Policy

**Question:** Does your organization maintain a documented information security policy? When was it last reviewed and approved?

**Expected Evidence:** Copy of the information security policy cover page showing approval date, or policy table of contents with revision history.

**Scoring Guidance:**
- 5: Comprehensive policy reviewed within last 12 months; Board-approved
- 4: Comprehensive policy reviewed within last 12 months
- 3: Policy exists but has not been reviewed in the last 12-24 months
- 2: Policy exists but is outdated (>24 months) or incomplete
- 1: No documented information security policy

**Framework Mapping:** ISO 27001 A.5.1, SOC 2 CC1.1, HIPAA 164.308(a)(1)

---

### A3. Security Awareness Training

**Question:** Do all employees receive security awareness training? How frequently? What topics are covered?

**Expected Evidence:** Training program description, completion rates, sample training content topics.

**Scoring Guidance:**
- 5: Annual training + ongoing phishing simulations; >95% completion rate; role-based training for developers and admins
- 4: Annual training with >90% completion; phishing simulations
- 3: Annual training with >80% completion
- 2: Training exists but is inconsistent or has low completion rates
- 1: No formal security awareness training program

**Framework Mapping:** ISO 27001 A.6.3, SOC 2 CC1.4, HIPAA 164.308(a)(5), PCI DSS 12.6

---

### A4. Risk Management Program

**Question:** Does your organization maintain a formal risk management program? How are risks identified, assessed, and treated?

**Expected Evidence:** Risk management policy or framework description; risk register summary (redacted if needed).

**Scoring Guidance:**
- 5: Formal risk management framework (e.g., ISO 31000); risk register reviewed quarterly; risk appetite defined by Board
- 4: Documented risk management process; risk register maintained and reviewed at least annually
- 3: Risks are identified and tracked but the process is informal
- 2: Ad hoc risk identification without formal tracking
- 1: No risk management program

**Framework Mapping:** ISO 27001 A.5.1, SOC 2 CC3.1-CC3.4, NIST CSF ID.RA

---

### A5. Background Checks

**Question:** Are background checks performed on employees prior to hire? What do they include?

**Expected Evidence:** Background check policy; description of checks performed.

**Scoring Guidance:**
- 5: Comprehensive checks (criminal, education, employment, credit where applicable) for all employees; enhanced checks for security/privileged roles
- 4: Standard background checks for all employees
- 3: Background checks for employees in sensitive roles only
- 2: Background checks are performed inconsistently
- 1: No background check program

**Framework Mapping:** ISO 27001 A.6.1, SOC 2 CC1.4, HIPAA 164.308(a)(3)

---

### A6. Insurance Coverage

**Question:** Does your organization carry cyber liability insurance? What is the coverage amount?

**Expected Evidence:** Certificate of insurance or summary of coverage.

**Scoring Guidance:**
- 5: Comprehensive cyber insurance with >$5M coverage; errors & omissions included
- 4: Cyber insurance with adequate coverage for the service scope
- 3: General liability insurance with some cyber coverage
- 2: Minimal insurance coverage
- 1: No cyber liability insurance

**Framework Mapping:** SOC 2 CC9.2, ISO 27001 A.5.19

---

### A7. Security Metrics and Reporting

**Question:** Does your organization track and report on security metrics (e.g., mean time to detect, mean time to respond, vulnerability remediation rates, training completion)? How are these metrics used to drive improvement?

**Expected Evidence:** Security metrics dashboard or sample report; description of metrics review cadence.

**Scoring Guidance:**
- 5: Comprehensive security KPIs tracked and reported to Board/leadership quarterly; metrics drive investment and improvement decisions; benchmarked against industry
- 4: Key security metrics tracked and reported to leadership regularly; used to identify improvement areas
- 3: Basic security metrics tracked (e.g., patching compliance, training completion); reviewed periodically
- 2: Limited metrics tracking; ad hoc reporting
- 1: No security metrics tracked

**Framework Mapping:** ISO 27001 A.5.1, SOC 2 CC4.1, NIST CSF ID.GV-4

---

## Section B: Data Protection and Privacy

### B1. Data Classification

**Question:** Does your organization have a data classification scheme? How is customer data classified and handled according to this scheme?

**Expected Evidence:** Data classification policy; description of how our data would be classified.

**Scoring Guidance:**
- 5: Formal classification scheme (e.g., Public/Internal/Confidential/Restricted) with documented handling procedures for each level; enforced technically
- 4: Formal classification scheme with documented handling procedures
- 3: Classification scheme exists but handling procedures are informal
- 2: Informal data classification with inconsistent application
- 1: No data classification scheme

**Framework Mapping:** ISO 27001 A.5.12-A.5.13, SOC 2 CC6.1, HIPAA 164.312(a)

---

### B2. Data Encryption at Rest

**Question:** Is customer data encrypted at rest? What encryption algorithm and key length are used? How are encryption keys managed?

**Expected Evidence:** Documentation of encryption standards; key management procedures.

**Scoring Guidance:**
- 5: AES-256 (or equivalent) for all data at rest; HSM-backed key management; automated key rotation; customer-managed key (CMK) option available
- 4: AES-256 for all customer data at rest; documented key management with regular rotation
- 3: Encryption at rest enabled but using provider defaults; basic key management
- 2: Encryption at rest for some but not all data stores
- 1: No encryption at rest or using deprecated algorithms

**Framework Mapping:** ISO 27001 A.8.24, SOC 2 CC6.1, HIPAA 164.312(a)(2)(iv), PCI DSS 3.4

---

### B3. Data Encryption in Transit

**Question:** Is data encrypted in transit? What protocols and versions are used? Are older protocols (TLS 1.0, 1.1, SSL) disabled?

**Expected Evidence:** TLS configuration documentation; SSL Labs scan results or equivalent.

**Scoring Guidance:**
- 5: TLS 1.3 preferred, TLS 1.2 minimum; HSTS enabled; certificate pinning for APIs; SSL 3.0 and TLS 1.0/1.1 disabled
- 4: TLS 1.2+ enforced; HSTS enabled; older protocols disabled
- 3: TLS 1.2 supported but older protocols not fully deprecated
- 2: TLS supported but TLS 1.0 or 1.1 still accepted
- 1: Unencrypted connections possible; SSL 3.0 still enabled

**Framework Mapping:** ISO 27001 A.8.24, SOC 2 CC6.1, HIPAA 164.312(e)(1), PCI DSS 4.1

---

### B4. Data Retention and Disposal

**Question:** What is your data retention policy for customer data? How is data securely deleted when no longer needed or upon contract termination?

**Expected Evidence:** Data retention policy; data disposal procedures; certificate of destruction process.

**Scoring Guidance:**
- 5: Defined retention periods per data type; automated deletion; cryptographic erasure for decommissioned storage; customer can request data export and deletion
- 4: Documented retention policy; secure deletion procedures; customer data deleted within 30 days of contract termination
- 3: General retention guidelines; data deletion on request; timeframe >30 days
- 2: Informal retention practices; deletion process unclear
- 1: No retention policy; data retained indefinitely; no deletion process

**Framework Mapping:** ISO 27001 A.8.10, SOC 2 CC6.5, GDPR Art. 17, PIPEDA Principle 5

---

### B5. Data Residency and Transfer

**Question:** In which countries/regions is customer data stored and processed? Are there any cross-border data transfers? If so, what legal mechanisms are used?

**Expected Evidence:** Data residency documentation; list of data center locations; Standard Contractual Clauses or adequacy decisions if applicable.

**Scoring Guidance:**
- 5: Data residency options available; all cross-border transfers covered by appropriate legal mechanisms (SCCs, adequacy decisions); data sovereignty controls
- 4: Clear data residency documentation; cross-border transfers covered by legal mechanisms
- 3: Data locations documented; some cross-border transfer mechanisms in place
- 2: Data residency unclear; cross-border transfers may lack proper legal basis
- 1: No data residency controls; no cross-border transfer mechanisms

**Framework Mapping:** GDPR Art. 44-49, ISO 27001 A.5.14, PIPEDA Principle 1

---

### B6. Data Backup

**Question:** How is customer data backed up? What is the backup frequency, retention period, and recovery testing schedule?

**Expected Evidence:** Backup policy; backup architecture documentation; most recent recovery test results.

**Scoring Guidance:**
- 5: Real-time replication + daily backups; encrypted backups stored in separate region; quarterly recovery tests documented; RPO <1 hour
- 4: Daily backups; encrypted; separate location; annual recovery tests
- 3: Regular backups; encrypted; recovery tested but not recently
- 2: Backups exist but are infrequent or not encrypted
- 1: No documented backup process or backup recovery not tested

**Framework Mapping:** ISO 27001 A.8.13, SOC 2 A1.2, HIPAA 164.308(a)(7)

---

### B7. Data Access Logging

**Question:** Is access to customer data logged? What data access events are captured? How long are logs retained?

**Expected Evidence:** Logging policy; sample log fields (redacted); log retention periods.

**Scoring Guidance:**
- 5: All data access logged (who, what, when, from where); logs immutable and forwarded to SIEM; retained 12+ months; automated alerting on anomalous access
- 4: Comprehensive access logging; centralized log management; 12-month retention
- 3: Access logging enabled for most systems; 6+ month retention
- 2: Partial logging; inconsistent retention
- 1: No data access logging

**Framework Mapping:** ISO 27001 A.8.15, SOC 2 CC7.2, HIPAA 164.312(b), PCI DSS 10.1-10.3

---

### B8. Privacy Program

**Question:** Does your organization have a dedicated privacy program? Is there a Data Protection Officer (DPO) or equivalent? What privacy regulations do you comply with?

**Expected Evidence:** Privacy policy; DPO contact information; list of applicable privacy regulations and compliance status.

**Scoring Guidance:**
- 5: Dedicated DPO/CPO; comprehensive privacy program; privacy impact assessments performed; compliant with GDPR, CCPA, PIPEDA as applicable
- 4: Named privacy officer; documented privacy program; compliant with applicable regulations
- 3: Privacy addressed within security program; external privacy counsel available
- 2: Basic privacy notice exists but no formal privacy program
- 1: No privacy program or privacy officer

**Framework Mapping:** GDPR Art. 37-39, ISO 27001 A.5.34, PIPEDA Principle 1

---

### B9. Data Processing Agreement

**Question:** Are you willing to execute a Data Processing Agreement (DPA) that meets GDPR Article 28 requirements? Do you have a standard DPA?

**Expected Evidence:** Standard DPA template or willingness to review and sign customer-provided DPA.

**Scoring Guidance:**
- 5: Standard DPA available that meets or exceeds GDPR Art. 28; responsive to customer-specific DPA requirements
- 4: Standard DPA available; willing to negotiate
- 3: Willing to sign a DPA but no standard template
- 2: Reluctant to sign a DPA; significant pushback expected
- 1: Unwilling to sign a DPA

**Framework Mapping:** GDPR Art. 28, ISO 27001 A.5.20, PIPEDA Principle 7

---

### B10. Data Loss Prevention

**Question:** Do you have data loss prevention (DLP) controls in place to prevent unauthorized exfiltration of customer data? What mechanisms are used?

**Expected Evidence:** DLP policy; description of DLP controls (email, endpoint, cloud, network).

**Scoring Guidance:**
- 5: Multi-layered DLP (endpoint, network, cloud, email); automated detection and blocking of sensitive data exfiltration; DLP events logged and reviewed; integrated with SIEM
- 4: DLP controls covering primary data channels (email, cloud storage); automated alerts; regular review
- 3: Basic DLP controls on key channels; some automated detection
- 2: Limited DLP; reliance on manual processes
- 1: No DLP controls

**Framework Mapping:** ISO 27001 A.8.12, SOC 2 CC6.7, HIPAA 164.312(e)(1)

---

## Section C: Access Control and Authentication

### C1. Authentication Standards

**Question:** What authentication mechanisms are supported for user access to your platform? Is multi-factor authentication (MFA) available and enforced?

**Expected Evidence:** Authentication configuration documentation; MFA enrollment statistics for your own employees.

**Scoring Guidance:**
- 5: MFA enforced for all users (customers and employees); supports FIDO2/WebAuthn, TOTP; SSO via SAML 2.0/OIDC; phishing-resistant MFA for privileged access
- 4: MFA available and enforced for all users; SSO supported
- 3: MFA available but not enforced; SSO supported
- 2: MFA available for admin accounts only; password-only for regular users
- 1: No MFA support; password-only authentication

**Framework Mapping:** ISO 27001 A.8.5, SOC 2 CC6.1, HIPAA 164.312(d), PCI DSS 8.3, NIST CSF PR.AC-7

---

### C2. Single Sign-On

**Question:** Do you support Single Sign-On (SSO) integration? Which protocols are supported (SAML 2.0, OIDC, etc.)? Is SSO available on all pricing tiers?

**Expected Evidence:** SSO integration documentation; supported identity providers list.

**Scoring Guidance:**
- 5: SAML 2.0 and OIDC supported; SSO available on all tiers (no "SSO tax"); SCIM provisioning supported
- 4: SAML 2.0 and OIDC supported; SCIM provisioning supported
- 3: SAML 2.0 or OIDC supported; SSO restricted to enterprise tier
- 2: SSO available but limited protocol support or significant restrictions
- 1: No SSO support

**Framework Mapping:** ISO 27001 A.8.5, SOC 2 CC6.1

---

### C3. Role-Based Access Control

**Question:** Does your platform support role-based access control (RBAC)? Can customers configure custom roles and permissions? Is the principle of least privilege applied?

**Expected Evidence:** RBAC documentation; list of default roles and permissions; custom role configuration options.

**Scoring Guidance:**
- 5: Granular RBAC with custom roles; attribute-based access control (ABAC) available; API-level permission controls; audit trail for role changes
- 4: Predefined roles with granular permissions; custom roles available; role change logging
- 3: Predefined roles with reasonable granularity; limited customization
- 2: Basic roles (admin/user) with limited granularity
- 1: No RBAC; all users have equal access

**Framework Mapping:** ISO 27001 A.5.15-A.5.18, SOC 2 CC6.3, HIPAA 164.312(a)(1), PCI DSS 7.1

---

### C4. Privileged Access Management

**Question:** How do you manage privileged/administrative access to production systems and customer data? Are privileged sessions monitored?

**Expected Evidence:** Privileged access management (PAM) policy; description of privileged access controls.

**Scoring Guidance:**
- 5: Dedicated PAM solution; just-in-time (JIT) access; break-glass procedures; all privileged sessions logged and recorded; regular access reviews
- 4: PAM controls; privileged sessions logged; quarterly access reviews
- 3: Separate privileged accounts; access logging; annual access reviews
- 2: Privileged access exists but management is informal
- 1: Shared admin accounts; no privileged access controls

**Framework Mapping:** ISO 27001 A.8.2, SOC 2 CC6.1-CC6.3, PCI DSS 7.1-7.2

---

### C5. Access Reviews

**Question:** How frequently are user access rights reviewed? What is the process for revoking access upon role changes or termination?

**Expected Evidence:** Access review policy; most recent access review completion evidence; offboarding/termination procedures.

**Scoring Guidance:**
- 5: Quarterly access reviews for all systems; automated deprovisioning via SCIM/HR integration; access revoked within 1 hour of termination
- 4: Quarterly access reviews; access revoked within 24 hours of termination
- 3: Semi-annual access reviews; access revoked within 48 hours of termination
- 2: Annual access reviews; access revocation is manual and sometimes delayed
- 1: No regular access reviews; no formal termination process

**Framework Mapping:** ISO 27001 A.5.18, SOC 2 CC6.2-CC6.3, HIPAA 164.312(a)(1), PCI DSS 8.1.4

---

### C6. Password Policy

**Question:** What password requirements are enforced? Is there a policy against password reuse? Are passwords stored securely (hashed and salted)?

**Expected Evidence:** Password policy documentation; description of password storage mechanism.

**Scoring Guidance:**
- 5: Minimum 12 characters; complexity requirements or passphrase support; password reuse prevention (last 24); bcrypt/scrypt/Argon2 hashing; credential breach monitoring
- 4: Strong password requirements; reuse prevention; secure hashing; MFA reduces password reliance
- 3: Reasonable password requirements; secure hashing; some reuse prevention
- 2: Basic password requirements; unsure about hashing implementation
- 1: Weak or no password requirements; potential for insecure storage

**Framework Mapping:** ISO 27001 A.8.5, SOC 2 CC6.1, PCI DSS 8.2

---

### C7. API Authentication

**Question:** How are API integrations authenticated? Are API keys rotatable? Is OAuth 2.0 supported? What rate limiting is in place?

**Expected Evidence:** API authentication documentation; rate limiting policies.

**Scoring Guidance:**
- 5: OAuth 2.0 with scoped tokens; API keys rotatable via self-service; mutual TLS option; per-endpoint rate limiting; API access logging
- 4: OAuth 2.0 supported; API keys rotatable; rate limiting; access logging
- 3: API key authentication with rotation capability; basic rate limiting
- 2: Static API keys; limited rotation capability; no rate limiting
- 1: Insecure API authentication; no rate limiting

**Framework Mapping:** ISO 27001 A.8.5, SOC 2 CC6.1

---

### C8. Session Management

**Question:** How are user sessions managed? What are the session timeout policies? Are concurrent sessions limited?

**Expected Evidence:** Session management configuration documentation.

**Scoring Guidance:**
- 5: Configurable session timeouts; idle timeout <15 min for privileged sessions; session binding to IP/device; concurrent session limits; secure session tokens
- 4: Reasonable session timeouts; idle timeout enforced; secure session management
- 3: Session timeouts configured; basic session management
- 2: Long or no session timeouts; sessions persist indefinitely
- 1: No session management controls

**Framework Mapping:** ISO 27001 A.8.5, SOC 2 CC6.1, PCI DSS 8.1.8

---

## Section D: Infrastructure and Network Security

### D1. Hosting Environment

**Question:** Where is your application hosted (cloud provider, on-premises, hybrid)? If cloud, which provider(s) and region(s)?

**Expected Evidence:** Infrastructure architecture overview; cloud provider and region list.

**Scoring Guidance:**
- 5: Major cloud provider(s) (AWS, Azure, GCP) with SOC 2 Type II; multi-region deployment; infrastructure-as-code; dedicated/isolated customer environments available
- 4: Major cloud provider with SOC 2 Type II; documented infrastructure architecture
- 3: Reputable hosting provider; basic architecture documentation
- 2: Hosting environment not well documented; smaller or less established provider
- 1: Self-hosted with limited infrastructure security controls

**Framework Mapping:** ISO 27001 A.8.20, SOC 2 CC6.1, PCI DSS 12.8

---

### D2. Network Segmentation

**Question:** Is your network segmented to isolate customer data and production environments? How are environments separated (production, staging, development)?

**Expected Evidence:** Network architecture diagram (redacted if needed); environment separation documentation.

**Scoring Guidance:**
- 5: Micro-segmentation; customer data isolated per tenant; strict network policies; production fully isolated from dev/staging; zero-trust network architecture
- 4: Network segmentation between environments; customer data isolated; firewall rules documented
- 3: Basic segmentation between production and non-production; some tenant isolation
- 2: Limited segmentation; environments partially separated
- 1: Flat network; no segmentation between environments

**Framework Mapping:** ISO 27001 A.8.22, SOC 2 CC6.6, PCI DSS 1.2-1.3

---

### D3. Vulnerability Management

**Question:** Do you have a vulnerability management program? How frequently are vulnerability scans performed? What is your patching SLA for critical, high, medium, and low vulnerabilities?

**Expected Evidence:** Vulnerability management policy; patching SLAs; recent scan summary (redacted).

**Scoring Guidance:**
- 5: Continuous automated scanning; critical patches within 24h; high within 7d; medium within 30d; vulnerability metrics tracked; third-party validation
- 4: Weekly scanning; critical patches within 48h; high within 14d; documented program
- 3: Monthly scanning; patching within 30 days for critical/high
- 2: Quarterly scanning; inconsistent patching cadence
- 1: No regular vulnerability scanning or patching program

**Framework Mapping:** ISO 27001 A.8.8, SOC 2 CC7.1, HIPAA 164.308(a)(1), PCI DSS 6.1-6.2, NIST CSF DE.CM-8

---

### D4. Penetration Testing

**Question:** Do you conduct regular penetration testing? Is it performed by an independent third party? How frequently? Can you share results or a summary?

**Expected Evidence:** Most recent penetration test executive summary; remediation status of findings.

**Scoring Guidance:**
- 5: Annual third-party pen test + continuous bug bounty program; results shared with customers; all critical/high findings remediated before report issuance
- 4: Annual third-party pen test; executive summary shareable; all critical/high findings remediated within 30 days
- 3: Annual pen test (internal or third-party); findings tracked and remediated
- 2: Pen testing performed but not annually or by independent party
- 1: No penetration testing performed

**Framework Mapping:** ISO 27001 A.8.8, SOC 2 CC4.1, PCI DSS 11.3, NIST CSF DE.CM-8

---

### D5. DDoS Protection

**Question:** What DDoS mitigation measures are in place? Is there a DDoS response plan?

**Expected Evidence:** DDoS protection architecture; mitigation provider information.

**Scoring Guidance:**
- 5: Enterprise DDoS mitigation service (e.g., Cloudflare, AWS Shield Advanced); automated detection and mitigation; documented response runbook
- 4: DDoS mitigation service; automated detection; response plan documented
- 3: Basic DDoS protection (e.g., cloud provider default); response plan exists
- 2: Minimal DDoS protection; no documented response plan
- 1: No DDoS protection measures

**Framework Mapping:** ISO 27001 A.8.20, SOC 2 A1.2

---

### D6. Intrusion Detection/Prevention

**Question:** Do you have intrusion detection/prevention systems (IDS/IPS) deployed? Is there a security operations center (SOC) monitoring alerts?

**Expected Evidence:** IDS/IPS deployment description; SOC coverage hours; monitoring architecture overview.

**Scoring Guidance:**
- 5: Network and host-based IDS/IPS; 24/7 SOC (internal or MSSP); SIEM with automated correlation; mean time to detect <15 minutes
- 4: IDS/IPS deployed; SOC coverage during business hours + on-call; SIEM
- 3: IDS/IPS deployed; alerts reviewed during business hours; basic SIEM
- 2: Some detection capabilities; limited monitoring
- 1: No intrusion detection or prevention systems

**Framework Mapping:** ISO 27001 A.8.16, SOC 2 CC7.2, PCI DSS 11.4

---

### D7. Endpoint Security

**Question:** What endpoint security controls are deployed on employee workstations and servers? Is mobile device management (MDM) used?

**Expected Evidence:** Endpoint security solution description; MDM policy.

**Scoring Guidance:**
- 5: EDR on all endpoints; MDM enforced; full disk encryption; automated patching; application allowlisting; USB restrictions
- 4: EDR deployed; MDM for company devices; full disk encryption; automated patching
- 3: Antivirus/anti-malware on endpoints; full disk encryption; basic MDM
- 2: Basic antivirus; encryption not enforced on all endpoints
- 1: No endpoint security controls

**Framework Mapping:** ISO 27001 A.8.1, SOC 2 CC6.8, HIPAA 164.310(d)

---

### D8. Physical Security

**Question:** What physical security controls protect your data centers and offices? Are there visitor management procedures?

**Expected Evidence:** Physical security policy; data center certifications (SOC 2, ISO 27001); office access controls description.

**Scoring Guidance:**
- 5: SOC 2-certified data centers; biometric access controls; 24/7 guards and CCTV; visitor logging; clean desk policy enforced
- 4: Certified data centers; badge access; CCTV; visitor management
- 3: Badge/key access to office; cloud hosting in certified data centers
- 2: Basic physical access controls; limited monitoring
- 1: No physical security controls; open access to facilities

**Framework Mapping:** ISO 27001 A.7.1-A.7.14, SOC 2 CC6.4, HIPAA 164.310(a)-(c), PCI DSS 9.1-9.4

---

### D9. Security Logging and Monitoring Architecture

**Question:** Describe your centralized logging and monitoring architecture. What log sources are collected? How are logs protected from tampering?

**Expected Evidence:** Logging architecture diagram; log source inventory; log integrity controls description.

**Scoring Guidance:**
- 5: Centralized SIEM ingesting all security-relevant logs (auth, network, application, cloud API); write-once/immutable log storage; real-time alerting with tuned rules; log integrity verification
- 4: Centralized SIEM with comprehensive log sources; tamper-evident storage; alerting configured
- 3: Centralized logging for key systems; basic alerting; logs protected from unauthorized modification
- 2: Partial centralized logging; limited alerting; log integrity not assured
- 1: No centralized logging; logs stored locally on individual systems

**Framework Mapping:** ISO 27001 A.8.15-A.8.16, SOC 2 CC7.2, PCI DSS 10.5, HIPAA 164.312(b)

---

### D10. Cloud Security Posture

**Question:** If you use cloud infrastructure, what cloud security controls are in place? Do you use cloud security posture management (CSPM) tools? How are cloud misconfigurations detected and remediated?

**Expected Evidence:** Cloud security architecture documentation; CSPM tool description; misconfiguration remediation process.

**Scoring Guidance:**
- 5: CSPM tool deployed with continuous monitoring; automated remediation for critical misconfigurations; CIS benchmarks enforced; cloud-native security services enabled (GuardDuty, Security Hub, etc.); regular cloud security reviews
- 4: CSPM tool deployed; automated alerting on misconfigurations; CIS benchmarks as baseline; regular reviews
- 3: Cloud security best practices followed; periodic manual reviews; some automated checks
- 2: Basic cloud security configuration; infrequent reviews
- 1: No cloud security posture management; default configurations

**Framework Mapping:** ISO 27001 A.8.20, SOC 2 CC6.1, NIST CSF PR.IP-1

---

## Section E: Application Security and SDLC

### E1. Secure Development Lifecycle

**Question:** Do you follow a secure software development lifecycle (SSDLC)? What security activities are integrated into each phase?

**Expected Evidence:** SSDLC documentation; description of security gates in CI/CD pipeline.

**Scoring Guidance:**
- 5: Formal SSDLC with security requirements, threat modeling, secure code review, SAST/DAST, security testing in CI/CD, and security sign-off before release
- 4: SSDLC with most security activities; automated security testing in CI/CD
- 3: Security testing performed but not fully integrated into SDLC
- 2: Ad hoc security testing; not integrated into development process
- 1: No secure development practices

**Framework Mapping:** ISO 27001 A.8.25-A.8.28, SOC 2 CC8.1, PCI DSS 6.3-6.5, NIST CSF PR.IP-12

---

### E2. Code Review

**Question:** Is code reviewed for security before deployment? Is peer review mandatory? Are automated static analysis tools used?

**Expected Evidence:** Code review policy; SAST tool(s) used; CI/CD pipeline configuration showing security checks.

**Scoring Guidance:**
- 5: Mandatory peer review + automated SAST/SCA + manual security review for sensitive changes; coverage metrics tracked
- 4: Mandatory peer review + automated SAST/SCA before merge
- 3: Peer review required; SAST/SCA used but not mandatory
- 2: Code review inconsistently performed; no automated analysis
- 1: No code review process

**Framework Mapping:** ISO 27001 A.8.25, SOC 2 CC8.1, PCI DSS 6.3.2

---

### E3. Dependency Management

**Question:** How do you manage third-party libraries and dependencies? Are dependencies scanned for known vulnerabilities? Is there a process for updating vulnerable dependencies?

**Expected Evidence:** SCA tool(s) used; dependency update policy; sample SCA report (redacted).

**Scoring Guidance:**
- 5: Automated SCA in CI/CD; dependency updates within 48h for critical vulns; software bill of materials (SBOM) maintained; lockfile enforcement
- 4: Automated SCA; critical dependency vulnerabilities addressed within 7 days
- 3: SCA scanning performed; dependencies updated regularly
- 2: Manual dependency tracking; updates performed inconsistently
- 1: No dependency management or vulnerability scanning

**Framework Mapping:** ISO 27001 A.8.28, SOC 2 CC8.1, NIST CSF PR.IP-12

---

### E4. Change Management

**Question:** Do you have a formal change management process for production deployments? Are changes tested before deployment? Is there a rollback procedure?

**Expected Evidence:** Change management policy; deployment pipeline documentation; rollback procedures.

**Scoring Guidance:**
- 5: Formal change management with approval workflows; automated testing (unit, integration, security); blue-green or canary deployments; automated rollback
- 4: Documented change management; peer-reviewed changes; tested before deployment; rollback procedures
- 3: Change management process exists; testing before deployment; manual rollback
- 2: Informal change process; limited testing before deployment
- 1: No change management; changes deployed directly to production

**Framework Mapping:** ISO 27001 A.8.32, SOC 2 CC8.1, PCI DSS 6.4

---

### E5. Environment Separation

**Question:** Are development, staging, and production environments separated? Is production data used in non-production environments?

**Expected Evidence:** Environment architecture documentation; data handling policy for non-production environments.

**Scoring Guidance:**
- 5: Strict environment separation; no production data in non-production; synthetic test data used; separate credentials per environment; access controls per environment
- 4: Environments separated; anonymized/masked data in non-production; separate credentials
- 3: Environments separated; production data occasionally used in staging (masked)
- 2: Environments partially separated; production data used in development
- 1: No environment separation; shared infrastructure and data

**Framework Mapping:** ISO 27001 A.8.31, SOC 2 CC6.1, PCI DSS 6.4.1-6.4.2

---

### E6. API Security

**Question:** What measures are in place to secure APIs? Is there API documentation? Are APIs tested for security vulnerabilities?

**Expected Evidence:** API security controls documentation; API testing methodology.

**Scoring Guidance:**
- 5: API gateway with rate limiting, authentication, and input validation; OpenAPI spec maintained; regular API security testing (DAST); API versioning
- 4: API security controls (authentication, rate limiting); documented APIs; periodic security testing
- 3: Basic API security controls; some documentation; ad hoc testing
- 2: Limited API security controls; minimal documentation
- 1: No API security controls

**Framework Mapping:** ISO 27001 A.8.26, SOC 2 CC6.1

---

### E7. Secrets Management

**Question:** How are secrets (API keys, database credentials, certificates) managed? Are secrets stored in source code repositories?

**Expected Evidence:** Secrets management solution description; policy on secrets in code.

**Scoring Guidance:**
- 5: Dedicated secrets manager (Vault, AWS Secrets Manager, etc.); automated secret rotation; pre-commit hooks preventing secrets in code; secrets scanning in CI/CD
- 4: Secrets manager used; no secrets in code; rotation policy documented
- 3: Secrets stored in environment variables or config files (not code); manual rotation
- 2: Some secrets in code or configuration files; inconsistent management
- 1: Secrets in plaintext in code repositories

**Framework Mapping:** ISO 27001 A.8.24, SOC 2 CC6.1, PCI DSS 3.5-3.6

---

## Section F: Incident Response and Business Continuity

### F1. Incident Response Plan

**Question:** Do you have a documented incident response plan? When was it last tested?

**Expected Evidence:** Incident response plan (or executive summary); most recent tabletop exercise date and summary.

**Scoring Guidance:**
- 5: Documented IRP aligned with NIST SP 800-61; tested via tabletop exercises at least semi-annually; lessons learned incorporated; dedicated incident response team
- 4: Documented IRP; annual tabletop exercise; incident response team identified
- 3: Documented IRP; tested within last 2 years
- 2: Basic IRP exists but has not been tested
- 1: No documented incident response plan

**Framework Mapping:** ISO 27001 A.5.24-A.5.28, SOC 2 CC7.3-CC7.5, HIPAA 164.308(a)(6), PCI DSS 12.10, NIST CSF RS.RP

---

### F2. Breach Notification

**Question:** What is your breach notification process and timeline? Will you notify affected customers? Within what timeframe?

**Expected Evidence:** Breach notification policy; contractual notification commitments.

**Scoring Guidance:**
- 5: Notification within 24 hours of confirmed breach; dedicated communication channel; regular status updates; post-incident report provided
- 4: Notification within 48 hours; status updates during incident; post-incident report
- 3: Notification within 72 hours (GDPR-compliant minimum); post-incident summary
- 2: Notification timeline undefined; best-effort communication
- 1: No breach notification commitment

**Framework Mapping:** GDPR Art. 33-34, ISO 27001 A.5.26, HIPAA 164.408-164.410, PIPEDA Breach of Security Safeguards Regulations

---

### F3. Business Continuity Plan

**Question:** Do you have a business continuity plan (BCP)? What is your Recovery Time Objective (RTO) and Recovery Point Objective (RPO)?

**Expected Evidence:** BCP executive summary; RTO and RPO commitments; most recent BCP test results.

**Scoring Guidance:**
- 5: Documented BCP tested annually; RTO <4 hours, RPO <1 hour; multi-region failover; BIA conducted annually
- 4: Documented BCP tested annually; RTO <8 hours, RPO <4 hours
- 3: Documented BCP; RTO <24 hours; tested within last 2 years
- 2: Basic BCP exists; RTO >24 hours; not tested recently
- 1: No business continuity plan

**Framework Mapping:** ISO 27001 A.5.29-A.5.30, SOC 2 A1.2-A1.3, HIPAA 164.308(a)(7)

---

### F4. Disaster Recovery

**Question:** Do you have a disaster recovery plan? Are DR tests performed regularly? What was the result of the most recent DR test?

**Expected Evidence:** DR plan summary; most recent DR test results; DR architecture overview.

**Scoring Guidance:**
- 5: DR plan with automated failover; tested quarterly; documented test results with recovery times; multi-region/multi-cloud DR capability
- 4: DR plan tested annually; documented results; failover capability demonstrated
- 3: DR plan exists; tested within last 2 years; basic failover capability
- 2: DR plan exists on paper but not tested
- 1: No disaster recovery plan

**Framework Mapping:** ISO 27001 A.5.29-A.5.30, SOC 2 A1.2-A1.3, HIPAA 164.308(a)(7), PCI DSS 12.10.1

---

### F5. SLA and Uptime Commitment

**Question:** What is your uptime SLA? What has your actual uptime been over the past 12 months? Is there a public status page?

**Expected Evidence:** SLA documentation; historical uptime data; status page URL.

**Scoring Guidance:**
- 5: 99.99%+ SLA; actual uptime meets or exceeds SLA; public status page with real-time and historical data; credit/refund mechanism for outages
- 4: 99.9% SLA; uptime meets SLA; public status page
- 3: 99.5% SLA; public status page; generally reliable
- 2: No formal SLA; uptime not consistently tracked
- 1: No SLA; frequent outages; no status page

**Framework Mapping:** SOC 2 A1.1, ISO 27001 A.5.20

---

### F6. Incident History

**Question:** Have you experienced any security incidents or data breaches in the past 3 years? If so, please describe the nature, impact, and remediation.

**Expected Evidence:** Incident history disclosure; remediation actions taken.

**Scoring Guidance:**
- 5: No incidents in 3 years; or incidents occurred but were handled transparently with strong remediation and public disclosure
- 4: Minor incidents with effective response and remediation; transparent communication
- 3: Incidents occurred; response was adequate; lessons learned implemented
- 2: Incidents occurred; response was slow or incomplete
- 1: Major incidents with poor response; ongoing concerns; lack of transparency

**Framework Mapping:** ISO 27001 A.5.27, SOC 2 CC7.4-CC7.5

---

### F7. Communication During Incidents

**Question:** How do you communicate with customers during an active security or availability incident? Is there a dedicated incident communication channel?

**Expected Evidence:** Incident communication plan; status page URL; sample incident notification template.

**Scoring Guidance:**
- 5: Dedicated status page with real-time updates; proactive email/in-app notifications; dedicated incident communication team; post-incident report within 5 business days
- 4: Status page with updates during incidents; email notifications; post-incident summary provided
- 3: Email notifications during major incidents; status page available but updates may be delayed
- 2: Reactive communication only when asked; no status page
- 1: No incident communication process; customers discover issues on their own

**Framework Mapping:** ISO 27001 A.5.26, SOC 2 CC7.4, HIPAA 164.308(a)(6)

---

### F8. Resilience Testing

**Question:** Beyond DR testing, do you conduct resilience or chaos engineering exercises to test system behavior under failure conditions? How do you validate that your systems degrade gracefully?

**Expected Evidence:** Resilience testing program description; chaos engineering practices; recent test results.

**Scoring Guidance:**
- 5: Formal chaos engineering program (e.g., using Chaos Monkey, Gremlin, or equivalent); regular game day exercises; graceful degradation validated; results documented and acted on
- 4: Periodic resilience testing; failure injection for critical components; results documented
- 3: Some resilience testing performed ad hoc; basic failure scenarios tested
- 2: Minimal resilience testing; reliance on DR testing only
- 1: No resilience testing beyond basic DR

**Framework Mapping:** ISO 27001 A.5.29, SOC 2 A1.2, NIST CSF PR.IP-10

---

## Section G: Third-Party and Subprocessor Management

### G1. Subprocessor Inventory

**Question:** Do you use subprocessors or sub-service organizations that access or process customer data? Can you provide a current list?

**Expected Evidence:** Current subprocessor list with names, services, and data access description.

**Scoring Guidance:**
- 5: Complete subprocessor list publicly available; proactive notification of changes; customer consent mechanism for new subprocessors
- 4: Subprocessor list provided on request; notification of changes; list maintained
- 3: Subprocessor list available but may not be current; notification process exists
- 2: Partial subprocessor visibility; limited notification
- 1: No subprocessor list available; no visibility into subprocessors

**Framework Mapping:** GDPR Art. 28(2), ISO 27001 A.5.21, SOC 2 CC9.2

---

### G2. Subprocessor Assessment

**Question:** How do you assess the security of your subprocessors? Are subprocessors subject to the same security requirements as your organization?

**Expected Evidence:** Subprocessor assessment policy; contractual security requirements for subprocessors.

**Scoring Guidance:**
- 5: All subprocessors assessed annually; SOC 2/ISO 27001 required; contractual security obligations flow down; right to audit included
- 4: Subprocessors assessed; security requirements contractually imposed; SOC 2 reports reviewed
- 3: Major subprocessors assessed; security requirements in contracts
- 2: Informal subprocessor assessment; limited contractual requirements
- 1: No subprocessor assessment program

**Framework Mapping:** ISO 27001 A.5.21, SOC 2 CC9.2, GDPR Art. 28(4)

---

### G3. Subprocessor Change Notification

**Question:** Will you notify customers before adding new subprocessors that access customer data? What is the notification period?

**Expected Evidence:** Subprocessor change notification policy; mechanism for customer objection.

**Scoring Guidance:**
- 5: 30+ day advance notification; customer can object; alternative provided if customer objects; published change log
- 4: 30-day advance notification; customer can object
- 3: Notification provided but with short notice (<30 days)
- 2: Notification provided after the change
- 1: No notification of subprocessor changes

**Framework Mapping:** GDPR Art. 28(2), ISO 27001 A.5.21

---

### G4. Supply Chain Security

**Question:** How do you manage supply chain security risks? Do you assess the security of your software dependencies and technology partners?

**Expected Evidence:** Supply chain risk management policy; SCA/SBOM practices.

**Scoring Guidance:**
- 5: Formal supply chain risk management; SBOM maintained; software dependencies scanned; vendor security assessments; signing and provenance verification
- 4: Dependencies scanned; key technology partners assessed; SBOM available
- 3: Software dependencies tracked and updated; informal partner assessment
- 2: Limited supply chain visibility; ad hoc management
- 1: No supply chain security management

**Framework Mapping:** ISO 27001 A.5.21, NIST CSF ID.SC, SOC 2 CC9.2

---

### G5. Fourth-Party Risk

**Question:** How do you manage risk from your vendors' vendors (fourth-party risk)? Do you have visibility into critical fourth-party dependencies?

**Expected Evidence:** Fourth-party risk policy; concentration risk assessment.

**Scoring Guidance:**
- 5: Fourth-party risk explicitly addressed in risk management framework; concentration risk tracked; critical fourth-party dependencies identified
- 4: Major fourth-party dependencies identified; risk considered in vendor assessments
- 3: Awareness of fourth-party risk; addressed informally
- 2: Limited fourth-party visibility
- 1: No consideration of fourth-party risk

**Framework Mapping:** ISO 27001 A.5.21, NIST CSF ID.SC-2

---

### G6. Concentration Risk

**Question:** Are there any single points of failure in your supply chain? Do you have contingency plans if a critical subprocessor becomes unavailable?

**Expected Evidence:** Concentration risk assessment; contingency plans for critical dependencies.

**Scoring Guidance:**
- 5: Concentration risk formally assessed and tracked; contingency plans for all critical dependencies; multi-provider strategies where feasible; tested failover for key subprocessors
- 4: Major concentration risks identified; contingency plans for most critical dependencies
- 3: Awareness of concentration risk; informal contingency planning
- 2: Limited concentration risk awareness; no contingency plans
- 1: No consideration of concentration risk

**Framework Mapping:** ISO 27001 A.5.29, NIST CSF ID.SC-5, SOC 2 A1.2

---

## Section H: Compliance and Certifications

### H1. SOC 2 Report

**Question:** Do you have a current SOC 2 Type II report? What Trust Services Criteria are covered? Can you share the report under NDA?

**Expected Evidence:** SOC 2 Type II report (or bridge letter if in between reporting periods).

**Scoring Guidance:**
- 5: SOC 2 Type II with clean opinion covering Security, Availability, Confidentiality; report covers current period; shared proactively
- 4: SOC 2 Type II with clean opinion covering Security; shared under NDA
- 3: SOC 2 Type I or Type II with minor exceptions; shared under NDA
- 2: SOC 2 in progress; Type I available or planned
- 1: No SOC 2 report; no plans to obtain

**Framework Mapping:** SOC 2 CC9.2, ISO 27001 A.5.19

---

### H2. ISO 27001 Certification

**Question:** Is your organization ISO 27001:2022 certified? What is the certification scope? When was your last surveillance audit?

**Expected Evidence:** ISO 27001 certificate; Statement of Applicability (SoA) summary.

**Scoring Guidance:**
- 5: ISO 27001:2022 certified; scope covers all services provided to customer; surveillance audit within last 12 months
- 4: ISO 27001 certified (2013 or 2022); scope covers relevant services
- 3: ISO 27001 certification in progress; expected within 12 months
- 2: ISO 27001 aligned but not certified; no current plans for certification
- 1: No ISO 27001 certification or alignment

**Framework Mapping:** ISO 27001 A.5.19, SOC 2 CC9.2

---

### H3. Additional Certifications

**Question:** Do you hold any additional security or compliance certifications (PCI DSS, HIPAA, FedRAMP, CSA STAR, SOC 3, etc.)?

**Expected Evidence:** Certificates or attestation letters for each claimed certification.

**Scoring Guidance:**
- 5: Multiple relevant certifications (PCI DSS, HIPAA, CSA STAR Level 2, FedRAMP); comprehensive compliance program
- 4: Additional certifications relevant to the services provided
- 3: One additional certification or in progress toward one
- 2: Self-assessed compliance frameworks without third-party validation
- 1: No additional certifications

**Framework Mapping:** PCI DSS 12.8.2, HIPAA 164.308(b)

---

### H4. Regulatory Compliance

**Question:** What regulatory requirements apply to your organization? How do you stay current with regulatory changes?

**Expected Evidence:** List of applicable regulations; regulatory monitoring process description.

**Scoring Guidance:**
- 5: Comprehensive regulatory compliance tracking; dedicated compliance team; proactive adaptation to regulatory changes; external counsel engaged
- 4: Regulatory requirements identified and tracked; compliance monitored
- 3: Key regulations identified; compliance addressed as part of security program
- 2: Limited regulatory awareness; reactive compliance
- 1: No regulatory compliance program

**Framework Mapping:** ISO 27001 A.5.31, SOC 2 CC1.1

---

### H5. Audit Rights

**Question:** Do your contracts include audit rights for customers? Can customers or their representatives conduct security assessments of your environment?

**Expected Evidence:** Standard contract language regarding audit rights; description of audit process.

**Scoring Guidance:**
- 5: Contractual audit rights; customer can conduct on-site or remote assessments; SOC 2 report satisfies annual audit right; additional assessments accommodated
- 4: Audit rights in contract; SOC 2 report provided as primary mechanism; additional assessments on request
- 3: SOC 2 report provided in lieu of audit rights; willing to discuss additional assurance
- 2: Limited audit rights; reluctant to accommodate assessments
- 1: No audit rights; unwilling to provide assurance beyond marketing materials

**Framework Mapping:** ISO 27001 A.5.22, GDPR Art. 28(3)(h), PCI DSS 12.8.2

---

### H6. Trust Center or Security Portal

**Question:** Do you maintain a public trust center, security portal, or transparency page where customers can access security documentation, compliance reports, and security updates?

**Expected Evidence:** Trust center URL; description of available resources.

**Scoring Guidance:**
- 5: Comprehensive trust center with self-service access to SOC 2 reports, penetration test summaries, DPA, subprocessor list, security whitepaper, and compliance status; regularly updated
- 4: Trust center with key documents available (SOC 2, DPA, subprocessor list); updated at least quarterly
- 3: Security page or portal with basic information; documents available on request
- 2: Security information available only on request; no public portal
- 1: No security documentation available to customers

**Framework Mapping:** SOC 2 CC9.2, ISO 27001 A.5.19

---

## Section I: AI/ML Specific Questions

*Complete this section only if the vendor uses artificial intelligence or machine learning in the services provided to you.*

### I1. AI/ML Model Overview

**Question:** Does your product use AI or machine learning models? If so, what type(s) of models are used, and what role do they play in the service?

**Expected Evidence:** Description of AI/ML usage; model types; role in service delivery.

**Scoring Guidance:**
- 5: Clear documentation of AI/ML usage; model cards or factsheets available; AI is optional/configurable; non-AI fallback available
- 4: AI/ML usage documented; purpose clearly defined; customer can understand how AI affects their data
- 3: AI/ML usage acknowledged; basic description of purpose
- 2: AI/ML usage acknowledged but poorly documented
- 1: AI/ML usage not disclosed or unclear

**Framework Mapping:** ISO 27001 A.5.1, GDPR Art. 22

---

### I2. Training Data

**Question:** Is customer data used to train AI/ML models? Can customers opt out of model training? How is training data handled and protected?

**Expected Evidence:** AI/ML training data policy; opt-out mechanism documentation.

**Scoring Guidance:**
- 5: Customer data never used for training by default; clear opt-in required; training data segregated and secured; data minimization applied
- 4: Customer data not used for training by default; opt-out available; clear documentation
- 3: Customer data may be used for training but opt-out is available
- 2: Customer data used for training with limited opt-out capability
- 1: Customer data used for training with no opt-out

**Framework Mapping:** GDPR Art. 6, Art. 22; PIPEDA Principle 3

---

### I3. AI Output and Decision-Making

**Question:** Does the AI make automated decisions that affect individuals? Is there a mechanism for human review of AI decisions? How is bias monitored?

**Expected Evidence:** Automated decision-making policy; human-in-the-loop process; bias monitoring methodology.

**Scoring Guidance:**
- 5: Human oversight for all consequential decisions; bias testing and monitoring; model performance metrics published; appeals process available
- 4: Human-in-the-loop for important decisions; bias monitoring in place; performance tracked
- 3: Some human oversight; bias acknowledged; working on monitoring
- 2: Limited human oversight; no formal bias monitoring
- 1: Fully automated decisions with no human review or bias monitoring

**Framework Mapping:** GDPR Art. 22, ISO 27001 A.5.1

---

### I4. AI Security

**Question:** What measures protect your AI/ML models from adversarial attacks, data poisoning, or prompt injection? How is model integrity assured?

**Expected Evidence:** AI security controls documentation; adversarial testing results.

**Scoring Guidance:**
- 5: Adversarial robustness testing; input validation and sanitization; model integrity monitoring; red teaming for AI-specific threats; documented AI threat model
- 4: AI-specific security controls; adversarial testing performed; model monitoring in place
- 3: Basic AI security controls; some testing performed
- 2: Limited AI-specific security measures
- 1: No AI-specific security controls

**Framework Mapping:** ISO 27001 A.8.25, NIST AI RMF

---

### I5. AI Transparency and Explainability

**Question:** Can you explain how your AI models reach their outputs? Is there documentation of model limitations and known failure modes?

**Expected Evidence:** Model documentation; explainability features; known limitations disclosure.

**Scoring Guidance:**
- 5: Comprehensive model documentation including limitations; explainability features available to customers; regular model performance reports; transparency reports published
- 4: Model documentation available; limitations disclosed; basic explainability
- 3: High-level documentation; some limitations acknowledged
- 2: Limited documentation; limitations not well understood
- 1: No model documentation or transparency

**Framework Mapping:** GDPR Art. 13-14, ISO 27001 A.5.1

---

### I6. AI Governance and Responsible Use

**Question:** Does your organization have an AI governance framework or responsible AI policy? How do you ensure AI systems are developed and deployed ethically?

**Expected Evidence:** AI governance policy; responsible AI principles; AI ethics review process.

**Scoring Guidance:**
- 5: Formal AI governance framework; AI ethics board or review committee; responsible AI principles published; AI impact assessments for new deployments; alignment with recognized AI governance standards (e.g., NIST AI RMF, EU AI Act preparedness)
- 4: Documented AI governance policy; AI ethics considerations integrated into development process; responsible AI principles adopted
- 3: AI governance addressed informally; some ethical considerations in AI development
- 2: Limited AI governance; ad hoc ethical considerations
- 1: No AI governance framework or responsible AI practices

**Framework Mapping:** NIST AI RMF, ISO 27001 A.5.1, GDPR Art. 22

---

### I7. AI Output Monitoring and Guardrails

**Question:** Does your organization have a process for monitoring AI model outputs for bias, hallucination, or safety issues? Describe any guardrails in place.

**Expected Evidence:** AI monitoring documentation, guardrail configuration.

**Scoring Guidance:**
- 5: Comprehensive AI output monitoring with automated guardrails; bias detection, hallucination detection, and safety filters in production; regular reviews of flagged outputs; documented escalation process
- 4: AI output monitoring in place with guardrails for key risk areas; regular review of flagged outputs
- 3: Basic monitoring of AI outputs; some guardrails implemented; periodic review
- 2: Limited AI output monitoring; minimal guardrails
- 1: No AI output monitoring or guardrails

**Framework Mapping:** ISO 42001

---

### I8. AI Training Data Governance

**Question:** How does your organization handle data used for training or fine-tuning AI models? Describe data governance practices.

**Expected Evidence:** AI data governance policy, training data documentation.

**Scoring Guidance:**
- 5: Formal AI data governance program; training data inventoried, classified, and documented; data provenance tracked; consent and licensing verified; bias assessment performed on training datasets; regular audits of training data quality
- 4: Documented AI data governance practices; training data cataloged; provenance and consent tracked; periodic reviews
- 3: Basic training data governance; data sources documented; some quality controls in place
- 2: Limited training data governance; informal documentation
- 1: No AI data governance practices for training data

**Framework Mapping:** ISO 42001, GDPR Art. 22

---

## Submission Instructions

Please return this completed questionnaire along with the following supporting documents:

1. SOC 2 Type II report (most recent)
2. ISO 27001 certificate (if applicable)
3. Penetration test executive summary (most recent)
4. Network architecture diagram (can be redacted)
5. Data Processing Agreement (your standard DPA)
6. Subprocessor list
7. Business continuity/disaster recovery plan summary
8. Cyber liability insurance certificate
9. Privacy policy URL

**Submit to:** [Your security team email]  
**Questions about this questionnaire:** [Your contact information]

---

*This questionnaire is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For a free SOC 2 readiness checklist, visit [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*
