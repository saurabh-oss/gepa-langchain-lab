"""Sample data for demonstration purposes.

This module contains realistic sample documents for the demo.
Replace these with your actual knowledge base for production use.
"""

from langchain_core.documents import Document

SAMPLE_DOCUMENTS = [
    Document(
        page_content="Account Security: To reset your password, navigate to Settings > Account > Security > Change Password. You will receive a verification email. Click the link in the email within 15 minutes. Set a new password with at least 12 characters including uppercase, lowercase, numbers, and special characters. For additional security, enable two-factor authentication in Settings > Security > 2FA."
    ),
    Document(
        page_content="API Keys Management: API keys are used to authenticate requests to our API. Keys expire after 90 days and must be rotated before expiration. To generate a new key, go to Developer Settings > API Keys > Create New Key. Each key has associated scopes controlling what actions it can perform. Keep keys secure and never commit them to version control. Revoke compromised keys immediately."
    ),
    Document(
        page_content="Billing and Refunds Policy: We offer a 30-day money-back guarantee for all plans. Refunds are available within 30 days of purchase for annual plans. Monthly plans can be cancelled anytime with refunds prorated to the day of cancellation. Refunds are issued to the original payment method within 5-7 business days. Enterprise customers can contact support for custom refund terms."
    ),
    Document(
        page_content="Authentication Methods: Single Sign-On (SSO) via SAML 2.0 is available on Professional and Enterprise plans. Standard OAuth 2.0 authentication works on all plans. We also support JWT token-based authentication for API access. Multi-factor authentication (MFA) with TOTP is available on all paid plans. Password-less authentication using magic links is available on Enterprise plans."
    ),
    Document(
        page_content="Webhook Configuration: Webhooks allow real-time event notifications. Configure webhooks in Settings > Integrations > Webhooks. Events are retried up to 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s). Webhook payloads are signed with HMAC-SHA256. Set appropriate timeouts; webhooks must respond within 30 seconds. Failed webhooks after 5 retries are logged in the Webhook Logs section."
    ),
    Document(
        page_content="Data Privacy and Compliance: We comply with GDPR, CCPA, SOC 2 Type II, and ISO 27001. All data is encrypted at rest using AES-256 and in transit using TLS 1.3. Users can request data exports in Settings > Privacy > Export Data. Account deletion is permanent and removes all data within 30 days. We conduct annual security audits and penetration testing."
    ),
    Document(
        page_content="Rate Limiting: API rate limits depend on your plan. Free plan: 100 requests/hour. Pro: 10,000 requests/hour. Enterprise: Custom limits. Rate limit headers show X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset. When exceeded, responses return HTTP 429 with retry information. Burst limits allow 2x the hourly rate for 1 minute."
    ),
    Document(
        page_content="Team Management: Invite team members in Settings > Team > Members. Assign roles: Owner (full access), Admin (manage users and settings), Editor (modify content), Viewer (read-only). Team members use their email addresses to log in. Remove members anytime; their access is revoked immediately. Teams on Pro+ plans can have unlimited members. Audit logs track all user actions."
    ),
]
