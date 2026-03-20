import json

threads = []

# === PATTERN 1: FOOT-IN-THE-DOOR (Gift Card Scams) ===
threads.append({
    "thread_id": "bec_001", "pattern": "foot_in_door",
    "emails": [
        {"turn": 1, "from": "james.wilson.ceo@company-corp.com", "to": "manpreet@company.com",
         "subject": "Quick question", "body": "Hey Manpreet, are you at your desk? I need a quick favor when you get a chance. Let me know.", "is_phishing": False},
        {"turn": 2, "from": "james.wilson.ceo@company-corp.com", "to": "manpreet@company.com",
         "subject": "Re: Quick question", "body": "Great thanks. I need you to purchase 5 Google Play gift cards at $200 each for a client appreciation event. Can you do this today and send me the codes? I will reimburse you. Please keep this between us for now.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_002", "pattern": "foot_in_door",
    "emails": [
        {"turn": 1, "from": "sarah.chen@execmail.com", "to": "accounting@company.com",
         "subject": "Are you available?", "body": "Hi, are you free right now? I need something handled quickly before end of day.", "is_phishing": False},
        {"turn": 2, "from": "sarah.chen@execmail.com", "to": "accounting@company.com",
         "subject": "Re: Are you available?", "body": "Perfect. I need you to buy 3 Amazon gift cards worth $500 each. Scratch the back and send photos of the codes to this email. This is for a surprise employee recognition so do not mention it to anyone.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_003", "pattern": "foot_in_door",
    "emails": [
        {"turn": 1, "from": "david.park@corp-hq.com", "to": "reception@company.com",
         "subject": "Checking in", "body": "Hello, just checking if the office is open today. I have a small request.", "is_phishing": False},
        {"turn": 2, "from": "david.park@corp-hq.com", "to": "reception@company.com",
         "subject": "Re: Checking in", "body": "Thanks for confirming. I am stuck in a meeting and cannot step out. Could you run to the store and get 4 iTunes gift cards at $100 each? I will pay you back this afternoon. Send me photos of the cards once you have them.", "is_phishing": True}
    ]
})

# === PATTERN 2: WIRE TRANSFER / INVOICE FRAUD ===
threads.append({
    "thread_id": "bec_004", "pattern": "wire_transfer",
    "emails": [
        {"turn": 1, "from": "cfo@globalpartners-inc.com", "to": "finance@company.com",
         "subject": "Upcoming payment", "body": "Hi team, we have a vendor payment coming up next week. I want to make sure everything is in order. Can you confirm our current payment process?", "is_phishing": False},
        {"turn": 2, "from": "cfo@globalpartners-inc.com", "to": "finance@company.com",
         "subject": "Re: Upcoming payment", "body": "Thanks for the info. Actually, our vendor has changed their banking details. Please update the wire transfer to: Account 4482991037, Routing 071000013, First National Bank. Process the $47,500 payment today. This is time-sensitive and already approved by the board.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_005", "pattern": "wire_transfer",
    "emails": [
        {"turn": 1, "from": "ap.department@supplier-co.net", "to": "accounts@company.com",
         "subject": "Invoice #INV-20260301", "body": "Dear Accounts Payable, Please find attached our invoice for services rendered in February. The total amount is $23,800. Standard NET-30 terms apply. Let us know if you have questions.", "is_phishing": False},
        {"turn": 2, "from": "ap.department@supplier-co.net", "to": "accounts@company.com",
         "subject": "URGENT: Updated banking for Invoice #INV-20260301", "body": "Important update - our company has switched banks effective immediately. Please update your records and send the $23,800 payment to: Wells Fargo, Account 7819304562, Routing 121000248. Please process today to avoid late fees. Our old account has been closed.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_006", "pattern": "wire_transfer",
    "emails": [
        {"turn": 1, "from": "margaret.liu@boardmember.org", "to": "treasurer@company.com",
         "subject": "Confidential acquisition", "body": "Hello, I need to discuss something confidential with you regarding a potential acquisition. Are you available for a quick call this afternoon?", "is_phishing": False},
        {"turn": 2, "from": "margaret.liu@boardmember.org", "to": "treasurer@company.com",
         "subject": "Re: Confidential acquisition", "body": "I could not reach you by phone. We need to move fast on this. Please wire $125,000 to the escrow account for the acquisition deposit. Account details: JPMorgan Chase, Account 3349201877, Routing 021000021. This is strictly confidential and must be completed by 3pm today. Do not discuss with other staff.", "is_phishing": True}
    ]
})

# === PATTERN 3: CREDENTIAL HARVESTING ===
threads.append({
    "thread_id": "bec_007", "pattern": "credential_harvest",
    "emails": [
        {"turn": 1, "from": "it.helpdesk@company-it.com", "to": "employees@company.com",
         "subject": "System maintenance notification", "body": "Dear staff, we will be performing scheduled maintenance on our email servers this weekend. No action is required at this time. We will send a follow-up with details.", "is_phishing": False},
        {"turn": 2, "from": "it.helpdesk@company-it.com", "to": "employees@company.com",
         "subject": "ACTION REQUIRED: Re-authenticate your email", "body": "Due to the server migration, all employees must re-verify their email credentials within 24 hours or lose access. Click here to verify: http://company-it-portal.com/verify. You will need to enter your current username and password. This is mandatory.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_008", "pattern": "credential_harvest",
    "emails": [
        {"turn": 1, "from": "security@office365-admin.com", "to": "user@company.com",
         "subject": "Security alert", "body": "We detected unusual sign-in activity on your Microsoft 365 account from an unrecognized device in another country. We have temporarily secured your account. We will send instructions shortly.", "is_phishing": False},
        {"turn": 2, "from": "security@office365-admin.com", "to": "user@company.com",
         "subject": "Re: Security alert - Verify identity now", "body": "To restore full access to your account, you must verify your identity immediately. Visit https://office365-secure-login.com/verify and sign in with your current credentials. If you do not complete verification within 12 hours, your account will be permanently locked and all data will be deleted.", "is_phishing": True}
    ]
})

# === PATTERN 4: PAYROLL DIVERSION ===
threads.append({
    "thread_id": "bec_009", "pattern": "payroll_diversion",
    "emails": [
        {"turn": 1, "from": "mike.johnson@company-hr.com", "to": "payroll@company.com",
         "subject": "Direct deposit update", "body": "Hi payroll team, I recently switched banks and need to update my direct deposit information before the next pay cycle. What is the process for that?", "is_phishing": False},
        {"turn": 2, "from": "mike.johnson@company-hr.com", "to": "payroll@company.com",
         "subject": "Re: Direct deposit update", "body": "Thanks for the info. Here are my new details: Bank of America, Routing 026009593, Account 4451029384. Please update this immediately so my next paycheck goes to the right place. I do not have access to the HR portal right now so I cannot do it myself.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_010", "pattern": "payroll_diversion",
    "emails": [
        {"turn": 1, "from": "emily.zhang@company.com", "to": "hr@company.com",
         "subject": "Banking change", "body": "Hello HR, hope you are doing well. I wanted to reach out about changing my direct deposit. I have been meaning to do this for a while. Is there a form I need to fill out?", "is_phishing": False},
        {"turn": 2, "from": "emily.zhang@company.com", "to": "hr@company.com",
         "subject": "Re: Banking change", "body": "I actually cannot access the portal because I am traveling. Can you just manually update it? New bank: TD Bank, Routing 031101266, Account 8827194530. Please make sure it takes effect before Friday payroll. Thanks so much.", "is_phishing": True}
    ]
})

# === PATTERN 5: VENDOR IMPERSONATION ===
threads.append({
    "thread_id": "bec_011", "pattern": "vendor_impersonation",
    "emails": [
        {"turn": 1, "from": "billing@cloudhost-services.com", "to": "it@company.com",
         "subject": "Your subscription renewal", "body": "Dear valued customer, your annual cloud hosting subscription is coming up for renewal on April 1st. Your current plan includes 500GB storage and 10 user licenses. We will send the renewal invoice next week.", "is_phishing": False},
        {"turn": 2, "from": "billing@cloudhost-services.com", "to": "it@company.com",
         "subject": "URGENT: Payment failure - service suspension", "body": "We attempted to charge your card on file but it was declined. Your services will be suspended in 24 hours unless payment is received. Please make an immediate wire transfer of $4,200 to avoid disruption. Bank: Citibank, Account 5529103847, Routing 021000089. Do not reply to this email, process the payment directly.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_012", "pattern": "vendor_impersonation",
    "emails": [
        {"turn": 1, "from": "support@enterprise-soft.com", "to": "procurement@company.com",
         "subject": "License audit", "body": "Hello, as part of our annual compliance process, we are conducting a license audit for all enterprise customers. We will be reviewing your current usage over the next two weeks. No action needed from your end at this time.", "is_phishing": False},
        {"turn": 2, "from": "support@enterprise-soft.com", "to": "procurement@company.com",
         "subject": "Re: License audit - Compliance violation found", "body": "Our audit found that your organization is using 47 licenses but only paying for 25. This is a serious compliance violation. To avoid legal action and a penalty of $89,000, please purchase the additional licenses immediately by wiring $31,500 to our accounts receivable: Account 6638201945, Routing 071921891, Chase Bank.", "is_phishing": True}
    ]
})

# === PATTERN 6: MULTI-TURN SLOW BURN (3 emails) ===
threads.append({
    "thread_id": "bec_013", "pattern": "slow_burn",
    "emails": [
        {"turn": 1, "from": "robert.taylor.ceo@megacorp.com", "to": "assistant@company.com",
         "subject": "Introduction", "body": "Hi, I am reaching out because I was referred to your company by a mutual contact. I would love to explore a potential partnership. Could we schedule a brief call this week?", "is_phishing": False},
        {"turn": 2, "from": "robert.taylor.ceo@megacorp.com", "to": "assistant@company.com",
         "subject": "Re: Introduction", "body": "Great speaking with you. I think there is real potential here. To move forward, our legal team needs a small good-faith deposit to draft the partnership agreement. This is standard for deals of this size.", "is_phishing": False},
        {"turn": 3, "from": "robert.taylor.ceo@megacorp.com", "to": "assistant@company.com",
         "subject": "Re: Re: Introduction", "body": "Here are the wire details for the $15,000 good-faith deposit: Bank of America, Account 7712304958, Routing 026009593. Once received, our attorneys will have the draft agreement to you within 48 hours. Please process today as we have other interested parties.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_014", "pattern": "slow_burn",
    "emails": [
        {"turn": 1, "from": "helen.ross@investment-group.com", "to": "cfo@company.com",
         "subject": "Investment opportunity", "body": "Dear CFO, our firm has been tracking your company growth and we are impressed. We specialize in growth-stage funding for companies like yours. Would you be open to a conversation about potential investment?", "is_phishing": False},
        {"turn": 2, "from": "helen.ross@investment-group.com", "to": "cfo@company.com",
         "subject": "Re: Investment opportunity", "body": "Thank you for your interest. After our initial review, we believe we can offer a $2M Series A investment at very favorable terms. Our due diligence process is straightforward. I will send over the preliminary term sheet this week.", "is_phishing": False},
        {"turn": 3, "from": "helen.ross@investment-group.com", "to": "cfo@company.com",
         "subject": "Re: Re: Investment opportunity", "body": "To proceed with due diligence, we require a refundable processing fee of $8,500. This covers legal review, background checks, and regulatory compliance. Wire to: Morgan Stanley Trust, Account 3318927456, Routing 036001808. This is fully refundable if we do not proceed. Time-sensitive as our Q1 funding window closes Friday.", "is_phishing": True}
    ]
})

# === PATTERN 7: DATA EXFILTRATION ===
threads.append({
    "thread_id": "bec_015", "pattern": "data_exfiltration",
    "emails": [
        {"turn": 1, "from": "auditor@external-compliance.com", "to": "hr@company.com",
         "subject": "Annual compliance review", "body": "Good morning, we have been engaged to conduct the annual compliance review for your organization. This is a routine process. We will need access to certain personnel records. I will send a detailed request list shortly.", "is_phishing": False},
        {"turn": 2, "from": "auditor@external-compliance.com", "to": "hr@company.com",
         "subject": "Re: Annual compliance review - Document request", "body": "Please provide the following by end of day: full employee roster with names, SSNs, dates of birth, home addresses, and salary information. Also include W-2 forms for all employees from the last two years. Please send as an Excel spreadsheet to this email. This is required for regulatory compliance and failure to provide may result in penalties.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_016", "pattern": "data_exfiltration",
    "emails": [
        {"turn": 1, "from": "legal@partner-lawfirm.com", "to": "admin@company.com",
         "subject": "Pending litigation matter", "body": "Dear Administrator, our firm represents a party in a matter that may involve your organization. This is a preliminary notification. We will be in touch with specific requests as the case develops.", "is_phishing": False},
        {"turn": 2, "from": "legal@partner-lawfirm.com", "to": "admin@company.com",
         "subject": "Re: Pending litigation - Preservation notice", "body": "As part of the litigation hold, we need complete copies of all financial records from 2024-2025, including bank statements, tax filings, client lists, and vendor contracts. Attach all documents to a reply to this email within 48 hours. Failure to comply may result in a court order and additional penalties.", "is_phishing": True}
    ]
})

# === PATTERN 8: LEGITIMATE THREADS (CONTROL) ===
threads.append({
    "thread_id": "bec_017", "pattern": "legitimate",
    "emails": [
        {"turn": 1, "from": "sarah@realcoworker.com", "to": "manpreet@company.com",
         "subject": "Team lunch Friday", "body": "Hey Manpreet, a few of us are planning to grab lunch at the new Thai place on Friday. Are you in? We are thinking 12:30.", "is_phishing": False},
        {"turn": 2, "from": "sarah@realcoworker.com", "to": "manpreet@company.com",
         "subject": "Re: Team lunch Friday", "body": "Awesome, glad you can make it. I made a reservation for 6 people at 12:30. The restaurant is on 5th Ave, about a 10-minute walk from the office. See you there!", "is_phishing": False}
    ]
})

threads.append({
    "thread_id": "bec_018", "pattern": "legitimate",
    "emails": [
        {"turn": 1, "from": "manager@company.com", "to": "team@company.com",
         "subject": "Q2 planning meeting", "body": "Hi team, I would like to schedule our Q2 planning meeting for next Tuesday at 2pm. Please review the Q1 results document I shared in our shared drive and come prepared with your department updates.", "is_phishing": False},
        {"turn": 2, "from": "manager@company.com", "to": "team@company.com",
         "subject": "Re: Q2 planning meeting", "body": "Quick update - we moved the meeting to Wednesday at 3pm since a few people had conflicts. Same agenda. Also, please submit your Q1 expense reports before the meeting so we can review budgets. Thanks everyone.", "is_phishing": False}
    ]
})

threads.append({
    "thread_id": "bec_019", "pattern": "legitimate",
    "emails": [
        {"turn": 1, "from": "vendor@realsupplier.com", "to": "purchasing@company.com",
         "subject": "Order confirmation #ORD-8847", "body": "Thank you for your order. We have received your purchase order for 50 units of the XR-200 component at $45 per unit, totaling $2,250. Estimated delivery is 5-7 business days. Your account representative is Tom at extension 4421.", "is_phishing": False},
        {"turn": 2, "from": "vendor@realsupplier.com", "to": "purchasing@company.com",
         "subject": "Re: Order confirmation #ORD-8847 - Shipping update", "body": "Good news, your order shipped early. FedEx tracking number 7849201384756. Expected delivery is this Thursday. Payment is due NET-30 per our standard terms. Invoice will be mailed to your billing address on file. Let Tom know if you need anything.", "is_phishing": False}
    ]
})

# Save
output_path = 'data/bec_threads/bec_conversations.json'
with open(output_path, 'w') as f:
    json.dump(threads, f, indent=2)

print(f"Saved {len(threads)} BEC conversation threads to {output_path}")
patterns = {}
for t in threads:
    p = t['pattern']
    patterns[p] = patterns.get(p, 0) + 1
for p, c in sorted(patterns.items()):
    print(f"  {p}: {c} threads")
