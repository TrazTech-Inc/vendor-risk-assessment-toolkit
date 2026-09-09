# Vendor Due Diligence Checklist

**Pre-Onboarding Security and Compliance Review**

**Version:** 1.0  
**Maintained by:** [TrazTech](https://traztech.ca)  
**Compliance Mapping:** SOC 2 CC9.2 | ISO 27001 A.5.19-A.5.20 | HIPAA 164.308(b) | PCI DSS 12.8

---

## Instructions

Complete this checklist before onboarding any new vendor. The depth of review should be proportional to the vendor's tier (see [Vendor Risk Framework](../methodology/VENDOR_RISK_FRAMEWORK.md)).

- **Tier 1 (Critical):** All items required
- **Tier 2 (High):** All items required except those marked [Tier 1 Only]
- **Tier 3 (Medium):** Items marked with * are required; others recommended
- **Tier 4 (Low):** Items marked with ** are required; others optional

---

## Vendor Information

| Field | Value |
|-------|-------|
| Vendor Name | |
| Services/Products | |
| Vendor Website | |
| Primary Contact | |
| Business Owner (Internal) | |
| Proposed Tier | |
| Due Diligence Completed By | |
| Date | |

---

## 1. Business Justification

- [ ] ** Business need for the vendor is documented
- [ ] ** Alternatives were evaluated (list alternatives considered: _______________)
- [ ] * Cost-benefit analysis completed
- [ ] Data types the vendor will access/process are identified
- [ ] Business owner for the vendor relationship is assigned

**Notes:**

---

## 2. Security Assessment

- [ ] ** Vendor tier determined using the tiering methodology
- [ ] * Security questionnaire sent and received
- [ ] * Security questionnaire reviewed and scored
- [ ] SOC 2 Type II report requested and reviewed
  - Report period: _____ to _____
  - Opinion: [ ] Clean [ ] Qualified [ ] N/A
  - Exceptions noted: _____________
- [ ] ISO 27001 certificate reviewed
  - Certification body: _____________
  - Valid through: _____________
  - Scope covers relevant services: [ ] Yes [ ] No
- [ ] Penetration test report reviewed (most recent)
  - Date: _____________
  - Performed by: _____________
  - Open critical/high findings: [ ] Yes (describe) [ ] No
- [ ] [Tier 1 Only] Architecture and data flow review conducted
- [ ] [Tier 1 Only] Virtual or on-site security assessment conducted
- [ ] Risk assessment report completed (see [Report Template](vendor-risk-assessment-report.md))

**Risk Score:** _____ / 5.0  
**Risk Rating:** [ ] Low [ ] Moderate [ ] High [ ] Critical

**Notes:**

---

## 3. Legal and Contractual Review

- [ ] ** Master Services Agreement (MSA) or equivalent executed
- [ ] * Non-Disclosure Agreement (NDA) executed
- [ ] * Data Processing Agreement (DPA) reviewed and executed (see [DPA Checklist](data-processing-agreement-checklist.md))
- [ ] * Service Level Agreement (SLA) reviewed and acceptable
  - Uptime commitment: _____________
  - Support response times defined: [ ] Yes [ ] No
- [ ] Breach notification clause included (notification within: _____ hours)
- [ ] Right-to-audit clause included
- [ ] Data deletion upon termination clause included
- [ ] Indemnification clause reviewed
- [ ] Limitation of liability reviewed and acceptable
- [ ] [HIPAA] Business Associate Agreement (BAA) executed (if PHI involved)
- [ ] [PCI DSS] Attestation of Compliance (AOC) reviewed (if payment data involved)
- [ ] Subprocessor notification clause included
- [ ] Governing law and jurisdiction reviewed

**Legal Reviewer:** _____________  
**Date Reviewed:** _____________

**Notes:**

---

## 4. Data Protection

- [ ] * Data types to be accessed/processed are documented:
  - [ ] PII (names, emails, addresses, etc.)
  - [ ] Financial data (payment info, bank details)
  - [ ] PHI (health information)
  - [ ] Authentication credentials
  - [ ] Confidential business data
  - [ ] Internal data (non-sensitive)
  - [ ] Public data only
- [ ] * Data flow diagram reviewed (how data moves to/from vendor)
- [ ] * Data residency confirmed (countries where data will be stored/processed: _____________)
- [ ] Data minimization verified (vendor only accesses data necessary for the service)
- [ ] Cross-border transfer mechanisms in place (if applicable)
  - [ ] Standard Contractual Clauses
  - [ ] Adequacy decision
  - [ ] Other: _____________
- [ ] Data retention and destruction terms agreed upon
- [ ] Data portability/export capability confirmed

**Notes:**

---

## 5. Technical Integration

- [ ] * Integration method documented:
  - [ ] API (read-only)
  - [ ] API (read/write)
  - [ ] SSO/SAML integration
  - [ ] Agent/SDK installed in our environment
  - [ ] Vendor hosted (data uploaded to vendor)
  - [ ] Network connectivity (VPN, peering)
  - [ ] No technical integration
- [ ] * Authentication method for integration confirmed:
  - [ ] OAuth 2.0
  - [ ] API key
  - [ ] SAML/OIDC
  - [ ] Certificate-based
  - [ ] Other: _____________
- [ ] Network access requirements documented (IP ranges, ports, protocols)
- [ ] Vendor access to our environment is scoped to minimum necessary
- [ ] SSO integration tested (if applicable)
- [ ] SCIM provisioning configured (if applicable)
- [ ] API rate limits understood and acceptable

**Technical Reviewer:** _____________  
**Date Reviewed:** _____________

**Notes:**

---

## 6. Insurance

- [ ] * Cyber liability insurance certificate obtained
  - Coverage amount: _____________
  - Policy expiration: _____________
- [ ] Errors and omissions (E&O) insurance confirmed
- [ ] General liability insurance confirmed
- [ ] Insurance coverage is adequate for the risk level

**Notes:**

---

## 7. Financial Viability

- [ ] Company has been in business for: _____ years
- [ ] Employee count: _____________
- [ ] Funding status / financial stability reviewed:
  - [ ] Publicly traded (ticker: _____)
  - [ ] Privately held / funded (last round: _____)
  - [ ] Bootstrapped / profitable
- [ ] No material financial concerns identified
- [ ] [Tier 1 Only] Credit report or financial statements reviewed

**Notes:**

---

## 8. Regulatory Compliance

- [ ] * Vendor's applicable regulatory requirements identified
- [ ] Vendor compliance status confirmed:
  - [ ] SOC 2 Type II
  - [ ] ISO 27001
  - [ ] PCI DSS (Level: _____)
  - [ ] HIPAA
  - [ ] GDPR
  - [ ] PIPEDA
  - [ ] FedRAMP
  - [ ] Other: _____________
- [ ] Regulatory requirements aligned with our obligations

**Notes:**

---

## 9. Operational Readiness

- [ ] ** Internal team briefed on vendor capabilities and limitations
- [ ] * Escalation contacts at vendor documented:
  - Technical support: _____________
  - Account manager: _____________
  - Security contact: _____________
- [ ] * Vendor added to vendor inventory ([vendor-inventory.csv](vendor-inventory.csv))
- [ ] * Next review date scheduled: _____________
- [ ] Vendor onboarding documentation/training completed
- [ ] Internal access provisioned to vendor platform (users/roles documented)
- [ ] Monitoring/alerting configured for vendor service

**Notes:**

---

## 10. Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Assessor | | [ ] Recommend Approval [ ] Do Not Recommend | |
| Business Owner | | [ ] Approve [ ] Reject | |
| Security Lead | | [ ] Approve [ ] Approve w/ Conditions [ ] Reject | |
| CISO (if Tier 1-2) | | [ ] Approve [ ] Reject | |

**Conditions for Approval (if any):**

1.
2.
3.

---

*This checklist is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For a free SOC 2 readiness checklist, visit [traztech.ca/soc-2-readiness-checklist](https://traztech.ca/soc-2-readiness-checklist).*
