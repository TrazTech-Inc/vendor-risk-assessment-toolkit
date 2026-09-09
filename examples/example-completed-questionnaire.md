# Vendor Security Questionnaire -- Completed Example

**Vendor:** CloudWidget Inc
**Completed By:** Alex Rivera, VP of Security, CloudWidget Inc
**Date Completed:** 2026-05-28
**Assessor:** Sarah Chen, Security Lead

*This is an example of a completed questionnaire showing what good (and not-so-good) responses look like. CloudWidget Inc is a fictional SaaS vendor used for illustration purposes.*

---

## Vendor Information

| Field | Response |
|-------|----------|
| Vendor Name | CloudWidget Inc |
| Primary Contact Name | Alex Rivera |
| Primary Contact Email | alex.rivera@cloudwidget.example.com |
| Primary Contact Title | VP of Security |
| Date Completed | 2026-05-28 |
| Vendor Website | https://cloudwidget.example.com |
| Headquarters Location | San Francisco, CA, USA |
| Year Founded | 2019 |
| Number of Employees | 185 |
| Description of Services Provided | Cloud-based project management and workflow automation platform. Stores project data, documents, user profiles, and integrates with customer communication tools. |
| Data Types Accessed/Processed | Customer names, email addresses, project data (documents, tasks, comments), file attachments, user activity logs |

---

## Section A: Company Overview and Governance

### A1. Organizational Security Leadership

**Response:** Yes. CloudWidget has a VP of Security (Alex Rivera) who reports directly to the CTO. The security team consists of 4 FTEs: VP of Security, 2 Security Engineers, and 1 GRC Analyst. The VP of Security has a standing monthly meeting with the Board of Directors to report on security metrics and incidents.

**Evidence Provided:** Organization chart showing security team reporting structure.

**Assessor Score:** 4 / 5
**Assessor Notes:** Strong for a company of this size. Dedicated security leadership with Board visibility. Not a 5 because CISO title and direct CEO reporting line are not present, but the function is well-established.

---

### A2. Information Security Policy

**Response:** Yes. Our Information Security Policy was last reviewed and approved by the CTO on January 15, 2026. It covers data classification, access control, incident response, acceptable use, and vendor management. The policy is reviewed annually and distributed to all employees via our internal knowledge base.

**Evidence Provided:** Policy cover page with approval signature and revision history showing annual reviews since 2021.

**Assessor Score:** 4 / 5
**Assessor Notes:** Comprehensive policy with annual review cycle. Current and well-maintained.

---

### A3. Security Awareness Training

**Response:** All employees complete security awareness training within their first week of onboarding and annually thereafter. Training covers phishing recognition, password hygiene, data handling, social engineering, and incident reporting. We conduct quarterly phishing simulations. Current completion rate is 94% for annual training. Developers receive additional secure coding training annually.

**Evidence Provided:** Training program outline; quarterly phishing simulation results; completion rate dashboard screenshot.

**Assessor Score:** 4 / 5
**Assessor Notes:** Strong training program. Phishing simulations and role-based training for developers are good indicators of maturity. 94% completion rate is solid.

---

### A4. Risk Management Program

**Response:** CloudWidget maintains a risk register that is reviewed quarterly by the security team and annually by leadership. Risks are identified through annual risk assessments, pen test findings, incident reviews, and employee reports. Each risk is scored on likelihood and impact, and treatment plans are assigned. We follow a risk management process loosely aligned with ISO 31000.

**Evidence Provided:** Risk management process document; redacted risk register summary showing 23 tracked risks.

**Assessor Score:** 4 / 5
**Assessor Notes:** Structured risk management with quarterly reviews. Good risk register hygiene. "Loosely aligned" with ISO 31000 means it is not formally certified, but the process is sound.

---

### A5. Background Checks

**Response:** All employees undergo criminal background checks and employment verification before their start date. For employees in security-sensitive roles (security team, DevOps, database admins), we also conduct education verification and reference checks.

**Evidence Provided:** Background check policy document.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good coverage. Enhanced checks for sensitive roles is a positive signal.

---

### A6. Insurance Coverage

**Response:** CloudWidget carries $5M in cyber liability insurance through Beazley, including coverage for data breach response, business interruption, and errors & omissions. Policy renews annually in September.

**Evidence Provided:** Certificate of insurance (current through September 2027).

**Assessor Score:** 4 / 5
**Assessor Notes:** Adequate coverage for the scope of the engagement. $5M is reasonable for a company of this size and the type of data processed.

---

## Section B: Data Protection and Privacy

### B1. Data Classification

**Response:** CloudWidget uses a four-tier data classification scheme: Public, Internal, Confidential, and Restricted. Customer data is classified as Confidential by default. Any data containing PII is classified as Restricted. Classification is applied at the system/database level, and handling procedures are documented for each classification tier.

**Evidence Provided:** Data classification policy; data handling matrix.

**Assessor Score:** 4 / 5
**Assessor Notes:** Well-defined classification scheme. Handling procedures are documented. Good practice of classifying customer data as Confidential by default.

---

### B2. Data Encryption at Rest

**Response:** All customer data is encrypted at rest using AES-256. We use AWS RDS with encryption enabled for our primary database, and S3 server-side encryption (SSE-S3) for file storage. Encryption keys are managed through AWS KMS. Key rotation occurs annually. We do not currently offer customer-managed keys (CMK).

**Evidence Provided:** Infrastructure documentation showing encryption configuration; AWS KMS key policy.

**Assessor Score:** 4 / 5
**Assessor Notes:** AES-256 with KMS is strong. Annual key rotation is acceptable. Lack of CMK option keeps this from a 5, but is not a concern for our use case.

---

### B3. Data Encryption in Transit

**Response:** All data in transit is encrypted using TLS 1.2 or higher. TLS 1.0 and 1.1 are disabled. We enforce HSTS with a max-age of 1 year. Internal service-to-service communication uses mutual TLS. Our SSL Labs rating is A+.

**Evidence Provided:** SSL Labs scan report showing A+ rating; TLS configuration documentation.

**Assessor Score:** 5 / 5
**Assessor Notes:** Excellent. TLS 1.2 minimum, HSTS, mutual TLS internally, and documented A+ SSL Labs rating.

---

### B4. Data Retention and Disposal

**Response:** Customer data is retained for the duration of the contract. Upon contract termination, customer data is deleted within 30 days from production systems. Backup data containing customer information is purged within 90 days due to our backup rotation cycle. Customers can request data export in JSON format and data deletion at any time during the contract. Deletion requests are fulfilled within 5 business days.

**Evidence Provided:** Data retention policy; data deletion procedure documentation.

**Assessor Score:** 4 / 5
**Assessor Notes:** Clear retention policy. 30-day production deletion and 90-day backup deletion are reasonable. Self-service data export is a positive.

---

### B5. Data Residency and Transfer

**Response:** All customer data is stored and processed in AWS US-East-1 (N. Virginia) and US-West-2 (Oregon) regions. We do not transfer customer data outside the United States. For EU customers, we offer an EU data residency option using AWS eu-west-1 (Ireland). We have Standard Contractual Clauses (SCCs) available for cross-border transfers.

**Evidence Provided:** Data residency documentation; SCC template.

**Assessor Score:** 4 / 5
**Assessor Notes:** Clear data residency with EU option. SCCs available. Good for our requirements.

---

### B6. Data Backup

**Response:** Customer data is backed up daily with encrypted snapshots stored in a separate AWS region. Backups are retained for 30 days. We test backup restoration quarterly, with the most recent test completed on April 5, 2026. Our RPO is 24 hours and our tested RTO is 4 hours.

**Evidence Provided:** Backup architecture documentation; most recent quarterly backup restoration test report (April 2026).

**Assessor Score:** 4 / 5
**Assessor Notes:** Daily backups with quarterly restore testing is solid. Cross-region backup storage adds resilience.

---

### B7. Data Access Logging

**Response:** All access to customer data is logged, including the user identity, action performed, resource accessed, timestamp, and source IP address. Logs are forwarded to our Datadog SIEM in real-time. Log retention is 12 months in the SIEM and 18 months in cold storage (S3 Glacier). Automated alerts are configured for anomalous access patterns, including off-hours access, bulk data access, and access from unusual locations.

**Evidence Provided:** Logging policy; sample log entry format (redacted); alert configuration summary.

**Assessor Score:** 5 / 5
**Assessor Notes:** Comprehensive logging with centralized SIEM, long retention, and automated alerting. This is a strong capability.

---

### B8. Privacy Program

**Response:** Our GRC Analyst serves as the privacy lead. We comply with CCPA and have a published privacy policy. We conduct privacy impact assessments for new features that process personal data. We do not have a formal DPO as we are not subject to GDPR (we do not target EU customers from our US operations), but we have GDPR-compliant practices in place for our EU data residency customers.

**Evidence Provided:** Privacy policy URL; PIA process documentation.

**Assessor Score:** 3 / 5
**Assessor Notes:** Privacy is addressed but not by a dedicated privacy professional. Adequate for current needs but would benefit from a formal privacy program, especially as they serve EU customers.

---

### B9. Data Processing Agreement

**Response:** Yes, we have a standard DPA that covers GDPR Article 28 requirements. We are willing to review and sign customer-provided DPAs as well. Our standard DPA includes data processing scope, security measures, subprocessor notification, breach notification within 48 hours, audit rights (satisfied by SOC 2 report), and data deletion upon termination.

**Evidence Provided:** Standard DPA template.

**Assessor Score:** 4 / 5
**Assessor Notes:** Standard DPA is comprehensive. Willingness to sign customer DPAs is appreciated. 48-hour breach notification is strong.

---

## Section C: Access Control and Authentication

### C1. Authentication Standards

**Response:** MFA is required for all users (both customer users and our employees). We support TOTP-based MFA and push notifications via our mobile app. For our employees accessing production systems, we require hardware security keys (YubiKey). SSO is supported via SAML 2.0 and OIDC.

**Evidence Provided:** Authentication configuration documentation; MFA enrollment report showing 100% employee enrollment.

**Assessor Score:** 5 / 5
**Assessor Notes:** MFA enforced for all users. Hardware keys for production access. SSO supported. Excellent.

---

### C2. Single Sign-On

**Response:** We support SAML 2.0 and OpenID Connect (OIDC) for SSO integration. SSO is available on our Business and Enterprise plans (not on the Starter plan). We support SCIM 2.0 for automated user provisioning and deprovisioning with Okta, Azure AD, and OneLogin.

**Evidence Provided:** SSO integration documentation; SCIM implementation guide.

**Assessor Score:** 4 / 5
**Assessor Notes:** SAML and OIDC with SCIM is strong. SSO is not available on all tiers (the "SSO tax" applies to the Starter plan), but it is available on the plan we use. Marking 4 since SSO is restricted by plan.

---

### C3. Role-Based Access Control

**Response:** Our platform supports 5 predefined roles (Owner, Admin, Manager, Member, Guest) with granular permissions at the project, workspace, and organization levels. Custom roles are available on the Enterprise plan. All role changes are logged with the actor, action, and timestamp.

**Evidence Provided:** RBAC documentation; role permission matrix.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good RBAC with granular permissions. Custom roles on Enterprise plan. Role change audit trail.

---

### C4. Privileged Access Management

**Response:** Production access is managed through a bastion host with JIT (just-in-time) access provisioning. Engineers request access through Jira tickets with manager approval. Access is granted for a maximum of 4 hours and automatically revoked. All privileged sessions are logged and auditable. We do not have a dedicated PAM tool but the process is enforced through our infrastructure automation.

**Evidence Provided:** Privileged access procedure documentation; bastion host architecture diagram.

**Assessor Score:** 4 / 5
**Assessor Notes:** JIT access with automatic revocation is strong. Approval workflow and session logging are present. No dedicated PAM tool, but the controls are effective.

---

### C5. Access Reviews

**Response:** We conduct quarterly access reviews for all production systems and customer-facing applications. Access reviews are tracked in Jira and require manager sign-off. Upon employee termination, access is revoked within 4 hours through our automated offboarding playbook in Okta. Role changes trigger an access review within 24 hours.

**Evidence Provided:** Most recent quarterly access review completion evidence (Q1 2026); offboarding playbook documentation.

**Assessor Score:** 4 / 5
**Assessor Notes:** Quarterly reviews with documented completion. Automated offboarding within 4 hours is strong. Role change reviews within 24 hours.

---

### C6. Password Policy

**Response:** Minimum 12 characters with at least one uppercase, one lowercase, one number, and one special character. Password reuse is prevented (last 12 passwords). Passwords are hashed using bcrypt with a cost factor of 12. We encourage the use of password managers and MFA reduces password-only risk.

**Evidence Provided:** Password policy document; technical documentation confirming bcrypt hashing.

**Assessor Score:** 4 / 5
**Assessor Notes:** Strong password requirements. bcrypt hashing is appropriate. Reuse prevention in place.

---

### C7. API Authentication

**Response:** Our API supports OAuth 2.0 with scoped access tokens. API keys are also available and can be rotated by the customer at any time through the admin console. Rate limiting is enforced at 1,000 requests per minute per API key. All API access is logged.

**Evidence Provided:** API documentation; rate limiting documentation.

**Assessor Score:** 4 / 5
**Assessor Notes:** OAuth 2.0 with scoped tokens is the right approach. Self-service key rotation and rate limiting are present.

---

### C8. Session Management

**Response:** Sessions expire after 24 hours of inactivity for regular users and 1 hour for admin users. Sessions are bound to the user's IP address (configurable). Maximum concurrent sessions per user is 5 (configurable by the customer admin). Session tokens are random 256-bit values stored in secure, HttpOnly, SameSite cookies.

**Evidence Provided:** Session management configuration documentation.

**Assessor Score:** 4 / 5
**Assessor Notes:** Reasonable session timeouts with shorter timeout for admins. Secure session token handling.

---

## Section D: Infrastructure and Network Security

### D1. Hosting Environment

**Response:** CloudWidget is hosted on AWS across two regions (US-East-1 and US-West-2) with active-passive failover. All infrastructure is defined as code using Terraform. We use EKS (Kubernetes) for container orchestration with dedicated node groups for each tenant on Enterprise plans.

**Evidence Provided:** Infrastructure architecture overview; AWS region/service list.

**Assessor Score:** 4 / 5
**Assessor Notes:** AWS is a strong choice with SOC 2 Type II. Multi-region with IaC is mature. Kubernetes orchestration is modern.

---

### D2. Network Segmentation

**Response:** Our network is segmented using AWS VPCs with separate subnets for public-facing, application, and data tiers. Production is fully isolated from staging and development via separate AWS accounts. Network policies are enforced using AWS security groups and Kubernetes network policies. Tenant data is logically isolated at the database level.

**Evidence Provided:** Network architecture diagram (redacted); network segmentation policy.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good segmentation with separate AWS accounts for environment isolation. Logical tenant isolation. Not micro-segmentation but appropriate for SaaS.

---

### D3. Vulnerability Management

**Response:** We run automated vulnerability scans weekly using Qualys on our infrastructure and Snyk for application dependencies. Patching SLAs: Critical -- 48 hours, High -- 7 days, Medium -- 30 days, Low -- 90 days. Patching compliance is tracked on a dashboard reviewed weekly by the security team.

**Evidence Provided:** Vulnerability management policy; patching SLA document; recent scan summary showing 0 critical and 2 high findings (both under remediation within SLA).

**Assessor Score:** 4 / 5
**Assessor Notes:** Weekly scanning with defined SLAs is solid. Two open high findings are within SLA. Active tracking and remediation.

---

### D4. Penetration Testing

**Response:** We conduct annual third-party penetration testing. Our most recent pen test was completed in February 2026 by NCC Group. The test covered external network, web application, and API testing. 2 medium and 4 low findings were identified; all have been remediated. We can share the executive summary under NDA.

**Evidence Provided:** Pen test executive summary (NCC Group, February 2026); remediation status showing all findings resolved.

**Assessor Score:** 4 / 5
**Assessor Notes:** Annual third-party pen test by a reputable firm. All findings remediated. No bug bounty program (which would be needed for a 5).

---

### D5. DDoS Protection

**Response:** We use AWS Shield Standard for all resources and AWS Shield Advanced for our public-facing endpoints. Additionally, we use CloudFront with AWS WAF for DDoS mitigation at the application layer. Our DDoS response runbook is documented and was tested during our most recent DR exercise.

**Evidence Provided:** DDoS protection architecture documentation; WAF rule summary.

**Assessor Score:** 4 / 5
**Assessor Notes:** AWS Shield Advanced plus WAF is a strong DDoS posture. Documented response runbook.

---

### D6. Intrusion Detection/Prevention

**Response:** We use AWS GuardDuty for threat detection across all accounts, Falco for runtime container security monitoring, and Datadog for log-based threat detection. Our security team reviews alerts during business hours (8am-8pm PT) with PagerDuty escalation for critical alerts 24/7. We do not have a dedicated 24/7 SOC.

**Evidence Provided:** Security monitoring architecture diagram; PagerDuty escalation policy.

**Assessor Score:** 3 / 5
**Assessor Notes:** Good detection tooling (GuardDuty, Falco, Datadog). However, no 24/7 SOC is a gap -- business-hours monitoring with on-call may miss time-sensitive threats. Score of 3 reflects this gap.

---

### D7. Endpoint Security

**Response:** All employee laptops run CrowdStrike Falcon EDR. FileVault (macOS) or BitLocker (Windows) full disk encryption is enforced via our Jamf MDM. USB storage is blocked on all endpoints. Automated OS and application patching is managed through Jamf/Intune.

**Evidence Provided:** Endpoint security policy; Jamf compliance dashboard screenshot showing 100% encryption compliance.

**Assessor Score:** 5 / 5
**Assessor Notes:** EDR, full disk encryption, MDM, USB blocking, and automated patching. Comprehensive endpoint security.

---

### D8. Physical Security

**Response:** CloudWidget does not operate its own data centers -- all infrastructure is on AWS, which maintains SOC 2 and ISO 27001 certifications for their data centers. Our offices in San Francisco use badge access with camera surveillance. Visitors must sign in at reception and are escorted at all times.

**Evidence Provided:** Office security policy; AWS compliance page reference.

**Assessor Score:** 4 / 5
**Assessor Notes:** Reliance on AWS for data center physical security is appropriate and well-documented. Office security is adequate.

---

## Section E: Application Security and SDLC

### E1. Secure Development Lifecycle

**Response:** CloudWidget follows a secure SDLC that includes security requirements review at design, automated SAST (Semgrep) and SCA (Snyk) in our CI/CD pipeline, peer code review for all merges, and security team sign-off for changes touching authentication, authorization, or data processing logic. We do not yet perform formal threat modeling for all new features, but it is on our 2026 roadmap.

**Evidence Provided:** SSDLC documentation; CI/CD pipeline diagram showing security checks.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good SSDLC with automated tooling in CI/CD. Security sign-off for sensitive changes. Threat modeling is not yet systematic (planned), which prevents a 5.

---

### E2. Code Review

**Response:** All code changes require at least one peer review before merge. Our CI/CD pipeline runs Semgrep (SAST) and Snyk (SCA) on every pull request. PRs that fail security checks cannot be merged. For changes to security-sensitive code, a second review from the security team is required.

**Evidence Provided:** Code review policy; CI/CD pipeline configuration showing required checks.

**Assessor Score:** 5 / 5
**Assessor Notes:** Mandatory peer review with automated SAST/SCA blocking merge. Security team review for sensitive changes. Strong.

---

### E3. Dependency Management

**Response:** We use Snyk for automated software composition analysis (SCA) integrated into our CI/CD pipeline. Critical vulnerability alerts in dependencies are addressed within 48 hours. We maintain a lockfile (package-lock.json, Gemfile.lock) for all services. We generate an SBOM quarterly using Syft.

**Evidence Provided:** Snyk dashboard summary; SBOM generation process documentation.

**Assessor Score:** 5 / 5
**Assessor Notes:** Automated SCA in CI/CD, 48-hour critical SLA, lockfile enforcement, and SBOM generation. Excellent dependency management.

---

### E4. Change Management

**Response:** All production deployments go through our change management process: 1) Developer creates a PR, 2) Peer review and automated testing, 3) Merge to main triggers staging deployment, 4) QA validation in staging, 5) Production deployment via automated pipeline. We use blue-green deployments with automatic rollback on health check failures. Emergency changes follow an expedited process with post-deployment review.

**Evidence Provided:** Change management policy; deployment pipeline documentation.

**Assessor Score:** 5 / 5
**Assessor Notes:** Formal change management with automated pipeline, blue-green deployments, automatic rollback, and emergency procedures. Mature process.

---

### E5. Environment Separation

**Response:** We maintain 3 environments: development, staging, and production. Each runs in a separate AWS account with separate credentials and networking. Production data is never used in development or staging. We use synthetic test data generated by a custom data factory tool.

**Evidence Provided:** Environment architecture diagram; data handling policy for non-production environments.

**Assessor Score:** 5 / 5
**Assessor Notes:** Strict environment separation with separate AWS accounts. No production data in non-production. Synthetic data used.

---

### E6. API Security

**Response:** Our APIs are served through an API gateway (Kong) that handles authentication, rate limiting, request validation, and logging. API endpoints are documented in OpenAPI 3.0 specification. We run DAST scans against our APIs quarterly using OWASP ZAP. API versioning is maintained with deprecation notices.

**Evidence Provided:** API documentation (OpenAPI spec); DAST scan summary.

**Assessor Score:** 4 / 5
**Assessor Notes:** API gateway with security controls, documented APIs, and periodic DAST. Good API security posture.

---

### E7. Secrets Management

**Response:** All application secrets are stored in AWS Secrets Manager. No secrets are stored in source code. We use pre-commit hooks (TruffleHog) to detect and block secrets before they reach the repository. Secret rotation varies by type: database credentials every 90 days, API keys every 6 months.

**Evidence Provided:** Secrets management policy; pre-commit hook configuration.

**Assessor Score:** 4 / 5
**Assessor Notes:** Dedicated secrets manager with pre-commit scanning. Rotation schedules defined. Good secrets hygiene.

---

## Section F: Incident Response and Business Continuity

### F1. Incident Response Plan

**Response:** CloudWidget has a documented Incident Response Plan aligned with NIST SP 800-61. The plan covers detection, analysis, containment, eradication, recovery, and post-incident review. We conduct tabletop exercises annually; our most recent exercise was in March 2026. The exercise simulated a supply chain compromise scenario.

**Evidence Provided:** IRP executive summary; tabletop exercise summary (March 2026).

**Assessor Score:** 4 / 5
**Assessor Notes:** NIST-aligned IRP with annual tabletop exercises. March 2026 exercise is recent. Annual testing (not semi-annual) keeps this at 4.

---

### F2. Breach Notification

**Response:** CloudWidget will notify affected customers within 48 hours of confirming a data breach. Notifications include the nature of the breach, data affected, remediation actions taken, and recommended customer actions. We provide regular status updates during active incidents and a post-incident report within 30 days.

**Evidence Provided:** Breach notification policy; notification template.

**Assessor Score:** 4 / 5
**Assessor Notes:** 48-hour notification with structured communication. Post-incident report is a good practice.

---

### F3. Business Continuity Plan

**Response:** Our BCP was last tested in March 2026 alongside our DR test. RTO is 4 hours and RPO is 1 hour. We operate active-passive across two AWS regions with automated failover at the database layer (RDS Multi-AZ + cross-region read replica). A business impact analysis was completed in January 2026.

**Evidence Provided:** BCP summary; BIA executive summary; most recent BCP/DR test results.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good RTO/RPO. Annual testing. Multi-region architecture. BIA completed recently.

---

### F4. Disaster Recovery

**Response:** Our DR plan covers region-level failure, database failure, and application-level failures. DR is tested annually (most recent: March 2026). In our last test, we achieved failover to the secondary region in 2.5 hours, which is within our 4-hour RTO target. The test revealed a minor issue with DNS propagation that was subsequently fixed.

**Evidence Provided:** DR test results (March 2026) showing 2.5-hour recovery time.

**Assessor Score:** 4 / 5
**Assessor Notes:** Annual DR testing with documented results. 2.5-hour recovery within RTO. Issue identified and fixed -- shows the process works.

---

### F5. SLA and Uptime Commitment

**Response:** Our SLA guarantees 99.9% uptime. Over the past 12 months, our actual uptime has been 99.95%. We maintain a public status page at status.cloudwidget.example.com with real-time and historical availability data. SLA credits are provided for any month where uptime falls below 99.9%.

**Evidence Provided:** SLA documentation; 12-month uptime report; status page URL.

**Assessor Score:** 4 / 5
**Assessor Notes:** 99.9% SLA with actual performance exceeding it. Public status page with history. Credit mechanism for outages.

---

### F6. Incident History

**Response:** In October 2025, CloudWidget experienced a 3-hour service degradation due to an AWS RDS failover event that was not handled gracefully by our application. No data was lost or compromised. Root cause analysis was completed, application resilience improvements were deployed, and the issue was communicated transparently through our status page and direct customer notification.

**Evidence Provided:** October 2025 incident post-mortem (redacted); status page history showing the event.

**Assessor Score:** 4 / 5
**Assessor Notes:** One availability incident in the past 3 years, no security breach. Transparent handling with post-mortem and remediation. This is actually a positive signal -- it shows the incident process works.

---

## Section G: Third-Party and Subprocessor Management

### G1. Subprocessor Inventory

**Response:** CloudWidget maintains a public subprocessor list on our Trust Center page. Current subprocessors include: AWS (infrastructure), Datadog (monitoring), SendGrid (email delivery), Stripe (billing), and Snowflake (analytics). The list was last updated in April 2026.

**Evidence Provided:** Subprocessor list URL; subprocessor details with data access descriptions.

**Assessor Score:** 4 / 5
**Assessor Notes:** Public subprocessor list on Trust Center. Includes data access descriptions for each. Recently updated.

---

### G2. Subprocessor Assessment

**Response:** All subprocessors are assessed before engagement and annually thereafter. We require SOC 2 Type II or ISO 27001 certification from all subprocessors. Security requirements are included in our contracts with subprocessors, and they are required to notify us of any security incidents.

**Evidence Provided:** Subprocessor assessment policy; evidence that SOC 2 reports are collected annually.

**Assessor Score:** 4 / 5
**Assessor Notes:** Annual assessment with SOC 2/ISO requirement is good. Contractual security obligations in place.

---

### G3. Subprocessor Change Notification

**Response:** We notify customers at least 30 days before adding a new subprocessor that will access customer data. Customers can object, and we will work to find an alternative or allow the customer to terminate if no alternative is available. Notifications are sent via email and posted on our Trust Center.

**Evidence Provided:** Subprocessor change notification policy; DPA clause referencing notification process.

**Assessor Score:** 5 / 5
**Assessor Notes:** 30-day advance notification with objection right. Clearly documented. This is the GDPR-compliant approach.

---

### G4. Supply Chain Security

**Response:** We scan all software dependencies using Snyk (as noted in E3). We generate an SBOM quarterly. For critical technology partners (AWS, Datadog), we review their SOC 2 reports annually. We do not have a formal supply chain risk management framework beyond these measures.

**Evidence Provided:** Cross-reference to E3 evidence; SOC 2 report review schedule.

**Assessor Score:** 3 / 5
**Assessor Notes:** Good SCA practices (covered in E3). SOC 2 review for key partners. However, no formal supply chain risk management framework. Adequate but room for improvement.

---

### G5. Fourth-Party Risk

**Response:** We are aware of fourth-party risk but do not have a formal program to manage it. We know that our subprocessors (e.g., AWS) also use subprocessors, and we rely on their SOC 2 reports to provide assurance. We track concentration risk -- AWS is our primary concentration risk.

**Evidence Provided:** Verbal response; no formal documentation.

**Assessor Score:** 3 / 5
**Assessor Notes:** Awareness without formal management. Concentration risk identified (AWS) but not formally tracked. Adequate given the maturity level.

---

## Section H: Compliance and Certifications

### H1. SOC 2 Report

**Response:** Yes. CloudWidget has a SOC 2 Type II report covering Security and Availability Trust Services Criteria. Our most recent report covers the period from April 1, 2025 to March 31, 2026. The report contains one exception related to the timeliness of access reviews for a subset of systems during Q3 2025 (since remediated). We can share the full report under NDA.

**Evidence Provided:** SOC 2 Type II report (April 2025 - March 2026) shared under NDA.

**Assessor Score:** 3 / 5
**Assessor Notes:** SOC 2 Type II is present, which is good. However, one exception (access review timeliness) is noted. The exception has been remediated. Score of 3 reflects the exception -- vendor should demonstrate clean report in next period to improve to 4. Confidentiality criteria not yet included.

---

### H2. ISO 27001 Certification

**Response:** CloudWidget is not currently ISO 27001 certified. We are in the process of implementing an ISMS aligned with ISO 27001:2022 and plan to undergo certification audit in Q4 2026.

**Evidence Provided:** ISO 27001 implementation project timeline.

**Assessor Score:** 3 / 5
**Assessor Notes:** Not certified but actively working toward it. Q4 2026 target is reasonable. Score of 3 reflects the "in progress" status.

---

### H3. Additional Certifications

**Response:** We are SOC 2 Type II certified (as described above). We do not hold PCI DSS, HIPAA, or FedRAMP certifications. We have completed the CSA STAR Level 1 self-assessment.

**Evidence Provided:** CSA STAR self-assessment on CSA registry.

**Assessor Score:** 3 / 5
**Assessor Notes:** SOC 2 Type II plus CSA STAR Level 1 self-assessment. Additional certifications would strengthen the posture.

---

### H4. Regulatory Compliance

**Response:** CloudWidget complies with CCPA (California Consumer Privacy Act), COPPA (we do not knowingly collect data from children), and Canadian PIPEDA. We track regulatory changes through external counsel and industry groups. We have a compliance monitoring process that reviews regulatory updates monthly.

**Evidence Provided:** Regulatory compliance matrix; monthly review process description.

**Assessor Score:** 4 / 5
**Assessor Notes:** Clear awareness of applicable regulations. Monthly monitoring through external counsel. Good compliance governance.

---

### H5. Audit Rights

**Response:** Our standard contract includes audit rights. Customers can satisfy their annual audit right by reviewing our SOC 2 Type II report. For additional assurance, we accommodate security questionnaires and virtual assessments upon reasonable request. On-site audits can be arranged with 30 days notice, subject to reasonable scope and confidentiality terms.

**Evidence Provided:** Contract language regarding audit rights (excerpt).

**Assessor Score:** 4 / 5
**Assessor Notes:** SOC 2 report as primary audit mechanism with additional assessment accommodation. On-site available. Reasonable and cooperative approach.

---

## Section I: AI/ML Specific Questions

### I1. AI/ML Model Overview

**Response:** CloudWidget uses machine learning in two features: 1) Smart project prioritization -- uses a ranking model to suggest task priority based on project history and deadlines, and 2) Document search -- uses embeddings for semantic search across project documents. Both features are optional and can be disabled by the customer admin.

**Evidence Provided:** AI feature documentation; admin toggle documentation.

**Assessor Score:** 4 / 5
**Assessor Notes:** Clear documentation of AI usage. Both features are optional (can be disabled). Appropriate transparency.

---

### I2. Training Data

**Response:** Our ranking model is trained on aggregated, anonymized historical project patterns (not individual customer data). The semantic search embeddings are generated on a per-tenant basis and are not shared across customers. Customers can opt out of AI features entirely. We do not use customer data to train shared/global models.

**Evidence Provided:** AI/ML data usage policy.

**Assessor Score:** 4 / 5
**Assessor Notes:** Clear data usage policy. No cross-customer training data. Opt-out available. Per-tenant embeddings ensure isolation.

---

### I3. AI Output and Decision-Making

**Response:** Our AI features make suggestions only -- they do not make automated decisions that affect individuals. Task priority suggestions require human confirmation. We monitor model accuracy metrics monthly. We have not implemented formal bias testing as the features do not involve demographic data or consequential decisions.

**Evidence Provided:** AI feature descriptions; model accuracy metrics.

**Assessor Score:** 3 / 5
**Assessor Notes:** AI is suggestions-only with human confirmation, which is the right approach. No formal bias monitoring, but given the non-consequential nature of the features, this is acceptable.

---

### I4. AI Security

**Response:** We validate and sanitize all inputs to our AI models. The semantic search feature uses input length limits and content filtering to prevent prompt injection. We do not currently perform adversarial robustness testing specific to our AI features. Our models are hosted on dedicated infrastructure with the same security controls as our production environment.

**Evidence Provided:** Input validation documentation; AI infrastructure description.

**Assessor Score:** 3 / 5
**Assessor Notes:** Basic AI security controls (input validation, content filtering). No adversarial testing. The limited scope of AI usage makes this acceptable, but improvement would be welcome.

---

### I5. AI Transparency and Explainability

**Response:** Both AI features include documentation of how they work, their limitations, and how to disable them. The priority ranking feature shows the factors that contributed to each suggestion. Known limitations (e.g., the model works best with 6+ months of project history) are documented in our help center.

**Evidence Provided:** Help center documentation for AI features; limitations disclosure.

**Assessor Score:** 4 / 5
**Assessor Notes:** Good transparency. Factor attribution for priority suggestions is a nice touch. Limitations clearly documented.

---

## Assessment Summary

**See the accompanying [Example Risk Report](example-risk-report.md) for the full assessment analysis and scoring.**

---

*This example is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca).*
