"""Sample evaluation set for demonstration purposes.

This module contains sample test questions with expected answers.
Replace these with your actual evaluation set for production use.
"""

SAMPLE_EVAL_SET = [
    {
        "question": "How do I reset my password and make it more secure?",
        "expected": "Settings > Account > Security > Change Password with 12+ chars including uppercase, lowercase, numbers, special chars. Enable 2FA in Settings > Security > 2FA"
    },
    {
        "question": "What happens when my API key expires and how do I rotate it?",
        "expected": "API keys expire after 90 days. Generate new key in Developer Settings > API Keys > Create New Key before expiration. Keep keys secure and revoke compromised ones immediately"
    },
    {
        "question": "What is your refund policy for annual vs monthly plans?",
        "expected": "30-day money-back guarantee for all plans. Annual plans: 30 days, prorated monthly. Monthly: cancel anytime with prorated refunds. Issued in 5-7 business days to original payment method"
    },
    {
        "question": "Which authentication methods are available on my plan?",
        "expected": "All plans: OAuth 2.0, JWT tokens, password-less magic links. Paid plans: MFA with TOTP. Professional+: SAML 2.0 SSO. Enterprise: Full SSO and passwordless auth"
    },
    {
        "question": "How reliable are webhooks and what should I do if they fail?",
        "expected": "Webhooks retry 5 times with exponential backoff (1s, 2s, 4s, 8s, 16s). Must respond within 30 seconds. Failed webhooks after 5 retries are logged. Payloads signed with HMAC-SHA256"
    },
    {
        "question": "What compliance standards does your platform meet?",
        "expected": "GDPR, CCPA, SOC 2 Type II, ISO 27001. AES-256 encryption at rest, TLS 1.3 in transit. Annual security audits and penetration testing"
    },
    {
        "question": "What are the rate limits and how are they enforced?",
        "expected": "Free: 100 req/hr, Pro: 10k req/hr, Enterprise: Custom. Headers show X-RateLimit-Limit, Remaining, Reset. 429 errors when exceeded. Burst: 2x hourly rate for 1 minute"
    },
    {
        "question": "How do I manage my team and assign different permission levels?",
        "expected": "Settings > Team > Members to invite. Roles: Owner (full), Admin (manage users), Editor (modify), Viewer (read-only). Remove anytime for instant revocation. Audit logs track actions"
    },
]
