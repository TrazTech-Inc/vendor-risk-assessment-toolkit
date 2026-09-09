# Vendor Offboarding Checklist

**Secure Vendor Termination Procedures**

**Version:** 1.0
**Maintained by:** [TrazTech](https://traztech.ca)
**Compliance Mapping:** SOC 2 CC9.2 | ISO 27001 A.5.19-A.5.20 | GDPR Art. 28(3)(g) | HIPAA 164.308(b)

---

## Instructions

Complete this checklist when terminating a vendor relationship. Vendor offboarding must be as structured as onboarding -- improper termination can leave orphaned access, undeleted data, and compliance gaps.

The urgency and completeness of offboarding should reflect the vendor's tier:
- **Tier 1-2:** Complete all items within 30 days of termination decision
- **Tier 3:** Complete all applicable items within 60 days
- **Tier 4:** Complete required items (**) within 90 days

---

## Vendor Information

| Field | Value |
|-------|-------|
| Vendor Name | |
| Vendor Tier | |
| Services Provided | |
| Contract End Date | |
| Termination Reason | [ ] Contract expiration [ ] Replacement vendor [ ] Breach/cause [ ] Cost reduction [ ] Other: _____ |
| Offboarding Lead | |
| Date Initiated | |
| Target Completion Date | |

---

## 1. Contractual and Legal

- [ ] ** Termination notice sent per contract terms
  - Date sent: _____________
  - Notice period: _____ days
  - Method: [ ] Email [ ] Letter [ ] Portal
- [ ] ** Confirm termination effective date: _____________
- [ ] Review contract for post-termination obligations (both parties)
- [ ] Review DPA for data return/deletion requirements
- [ ] Confirm transition/migration period terms (if applicable)
- [ ] Outstanding invoices identified and resolved
- [ ] Confirm any perpetual license rights (if applicable)
- [ ] Legal team notified of termination

**Notes:**

---

## 2. Data Return and Deletion

- [ ] ** Data return/export requested from vendor
  - Data format: _____________
  - Date requested: _____________
  - Date received: _____________
- [ ] ** Data export validated (completeness and integrity check)
- [ ] ** Written confirmation of data deletion requested from vendor
  - Date requested: _____________
  - Date received: _____________
- [ ] Confirmation covers:
  - [ ] Production data
  - [ ] Backup data (with deletion timeline for backup rotation)
  - [ ] Logs containing personal data
  - [ ] Test/staging environments
  - [ ] Any copies held by subprocessors
- [ ] Certificate of data destruction obtained (if available)
- [ ] Vendor confirmed no data retained except as required by law
  - If data retained by law, document: _____________

**Notes:**

---

## 3. Access Revocation

### 3.1 Vendor Access to Our Systems

- [ ] ** All vendor user accounts in our systems disabled/deleted
  - Systems affected: _____________
  - Date revoked: _____________
- [ ] ** VPN access revoked
- [ ] ** API keys/tokens for vendor integrations revoked or rotated
- [ ] SSH keys or certificates associated with vendor removed
- [ ] IP allowlist entries for vendor removed
- [ ] Service accounts used by vendor disabled/deleted
- [ ] Multi-factor authentication tokens for vendor users deregistered
- [ ] Vendor removed from SSO/identity provider groups

### 3.2 Our Access to Vendor Systems

- [ ] ** Our user accounts on vendor platform documented before deletion
- [ ] Confirm our data has been exported before accounts are closed
- [ ] Our API keys/tokens on vendor platform revoked
- [ ] Shared credentials rotated (any credentials the vendor may have seen)
- [ ] Browser sessions and cached credentials cleared

### 3.3 Shared Resources

- [ ] Shared folders, drives, or repositories access revoked
- [ ] Shared communication channels (Slack channels, Teams groups) archived/closed
- [ ] Shared email distribution lists updated
- [ ] Shared calendar entries removed
- [ ] Shared dashboards or reports decommissioned

**Notes:**

---

## 4. Technical Integration Removal

- [ ] ** API integrations disconnected
  - Integration points: _____________
  - Date disconnected: _____________
- [ ] ** SSO/SAML integration removed
- [ ] SCIM provisioning disabled
- [ ] Webhook endpoints deregistered
- [ ] Vendor's SDK/agent/plugins removed from our environment
  - Software removed: _____________
  - Date removed: _____________
- [ ] DNS records pointing to vendor updated or removed
- [ ] Firewall rules for vendor-specific traffic removed
- [ ] Network peering or VPN tunnels torn down
- [ ] Load balancer configurations updated
- [ ] CDN configurations updated (if vendor was CDN provider)
- [ ] Monitoring and alerting for vendor integrations removed or updated
- [ ] Logging pipeline configurations updated

**Notes:**

---

## 5. DNS and Domain Considerations

- [ ] Any DNS records delegated to vendor's nameservers reclaimed
- [ ] SPF/DKIM/DMARC records updated if vendor was email provider
- [ ] SSL/TLS certificates issued through vendor rotated
- [ ] Domain registrar access reviewed (if vendor had access)
- [ ] Redirects or CNAME records pointing to vendor services updated

**Notes:**

---

## 6. Financial

- [ ] ** Outstanding invoices paid or disputed
- [ ] Recurring payment/subscription cancelled
  - Date cancelled: _____________
  - Last billing date: _____________
- [ ] Refund or credit requested for prepaid unused services (if applicable)
- [ ] Purchase orders closed
- [ ] Accounts payable notified to stop future payments
- [ ] Credit card on file removed from vendor's billing portal

**Notes:**

---

## 7. Communication

- [ ] ** Internal stakeholders notified of vendor termination:
  - [ ] Engineering/IT team
  - [ ] Security team
  - [ ] Compliance team
  - [ ] Finance/procurement
  - [ ] Business owner
  - [ ] Affected end users
- [ ] Replacement vendor or alternative solution communicated (if applicable)
- [ ] Vendor's support/account team acknowledged termination
- [ ] Transition plan communicated to all affected parties
- [ ] Knowledge transfer completed (if migrating to replacement vendor)

**Notes:**

---

## 8. Documentation Updates

- [ ] ** Vendor removed from vendor inventory ([vendor-inventory.csv](vendor-inventory.csv)) or marked as "Terminated"
  - Status updated: _____________
- [ ] ** Risk register updated
- [ ] System inventory / asset register updated
- [ ] Data flow diagrams updated to remove vendor
- [ ] Network diagrams updated
- [ ] Business continuity plan updated (if vendor was part of BCP)
- [ ] Incident response contacts updated (remove vendor escalation paths)
- [ ] Privacy notices updated (if vendor was listed as a processor)
- [ ] Security policies updated (if they reference the vendor specifically)
- [ ] Compliance documentation updated for next audit cycle

**Notes:**

---

## 9. Compliance and Audit Trail

- [ ] ** All offboarding activities documented with dates and responsible parties
- [ ] ** Evidence of data deletion/return archived
- [ ] Vendor assessment history archived (retain per retention policy)
  - Retention period: _____ years
- [ ] Contracts and agreements archived
- [ ] Correspondence related to offboarding archived
- [ ] Offboarding checklist filed as compliance evidence

**Notes:**

---

## 10. Post-Offboarding Verification

*Complete 30 days after termination effective date:*

- [ ] Confirm no active sessions or connections to/from vendor
- [ ] Confirm no data flowing to/from vendor systems
- [ ] Confirm all vendor user accounts are fully deprovisioned
- [ ] Confirm no recurring charges from vendor
- [ ] Confirm replacement solution is fully operational (if applicable)
- [ ] Spot-check that integrations are fully disconnected (test API endpoints, etc.)
- [ ] Confirm data deletion certification has been received

**Verification Date:** _____________
**Verified By:** _____________

**Notes:**

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Offboarding Lead | | | |
| Business Owner | | | |
| Security Lead | | | |
| IT Lead | | | |

**Offboarding Complete:** [ ] Yes [ ] No -- Outstanding items: _____________

**Date Completed:** _____________

---

*This checklist is part of the [Vendor Risk Assessment Toolkit](https://github.com/TrazTech-Inc/vendor-risk-assessment-toolkit), maintained by [TrazTech](https://traztech.ca). For guidance on scheduling recurring compliance activities, see [Compliance Calendar: What Actually Recurs](https://traztech.ca/blog/compliance-calendar-what-actually-recurs).*
