import json

# Load existing threads
with open('data/bec_threads/bec_conversations.json', 'r') as f:
    threads = json.load(f)

# Add 11 more threads

threads.append({
    "thread_id": "bec_020", "pattern": "foot_in_door",
    "emails": [
        {"turn": 1, "from": "richard.nguyen@ceo-office.com", "to": "admin@company.com",
         "subject": "Need your help", "body": "Hi, do you have a moment? I have something I need handled before the end of the day.", "is_phishing": False},
        {"turn": 2, "from": "richard.nguyen@ceo-office.com", "to": "admin@company.com",
         "subject": "Re: Need your help", "body": "Thanks for getting back to me. I need you to pick up 4 Apple gift cards at $250 each for employee rewards. Scratch them and email me photos of the codes. I am in back-to-back meetings so please handle this quietly.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_021", "pattern": "wire_transfer",
    "emails": [
        {"turn": 1, "from": "accounting@vendor-solutions.com", "to": "ap@company.com",
         "subject": "Payment status", "body": "Hello, I wanted to follow up on the status of our outstanding invoice from last month. Can you confirm whether it has been processed?", "is_phishing": False},
        {"turn": 2, "from": "accounting@vendor-solutions.com", "to": "ap@company.com",
         "subject": "URGENT: Bank change before payment", "body": "Before you process that payment, please note our banking information has changed effective immediately. New details: TD Bank, Account 9928374651, Routing 067014822. Please update and send today. Our old account is frozen due to a bank merger.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_022", "pattern": "credential_harvest",
    "emails": [
        {"turn": 1, "from": "admin@company-sharepoint.com", "to": "staff@company.com",
         "subject": "New document shared with you", "body": "A new document has been shared with you on the company SharePoint. You will receive access details shortly.", "is_phishing": False},
        {"turn": 2, "from": "admin@company-sharepoint.com", "to": "staff@company.com",
         "subject": "Re: New document shared - Access required", "body": "To view the shared document, please sign in at https://sharepoint-company-login.com/auth with your company email and password. This link expires in 6 hours. If you do not authenticate, the document will be permanently deleted from your account.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_023", "pattern": "payroll_diversion",
    "emails": [
        {"turn": 1, "from": "kevin.patel@company.com", "to": "payroll@company.com",
         "subject": "Quick payroll question", "body": "Hey payroll team, quick question. When is the cutoff date for making changes to direct deposit for this pay period? Just want to make sure I do not miss the window.", "is_phishing": False},
        {"turn": 2, "from": "kevin.patel@company.com", "to": "payroll@company.com",
         "subject": "Re: Quick payroll question", "body": "Perfect, I am just in time then. Please update my direct deposit to: Scotiabank, Transit 44372, Account 1109283745. I just switched banks last week and do not want my paycheck going to the closed account. I tried the self-service portal but it keeps timing out.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_024", "pattern": "vendor_impersonation",
    "emails": [
        {"turn": 1, "from": "renewals@saas-platform.com", "to": "it@company.com",
         "subject": "Annual license renewal reminder", "body": "Dear IT Administrator, this is a friendly reminder that your annual software license renewal is approaching on April 15th. Your current plan covers 100 seats. No action is needed at this time. We will send the renewal invoice two weeks before expiry.", "is_phishing": False},
        {"turn": 2, "from": "renewals@saas-platform.com", "to": "it@company.com",
         "subject": "CRITICAL: License violation detected", "body": "Our automated audit system detected that your organization is running 156 active seats against a 100-seat license. This is a material breach of your service agreement. To avoid immediate service termination and a compliance penalty of $67,000, please remit $22,400 for the additional seats via wire transfer to: Account 7734928156, Routing 021000021, JPMorgan Chase. Payment must be received within 48 hours.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_025", "pattern": "slow_burn",
    "emails": [
        {"turn": 1, "from": "diana.ross@acquisition-partners.com", "to": "founder@company.com",
         "subject": "Potential partnership inquiry", "body": "Good afternoon, I represent a private equity group that has been following your company with great interest. We believe there could be a mutually beneficial partnership opportunity. Would you be open to a preliminary conversation?", "is_phishing": False},
        {"turn": 2, "from": "diana.ross@acquisition-partners.com", "to": "founder@company.com",
         "subject": "Re: Potential partnership inquiry", "body": "Thank you for the productive call yesterday. Our team is very enthusiastic about moving forward. As discussed, the next step is a formal due diligence review. I will prepare the preliminary assessment report this week.", "is_phishing": False},
        {"turn": 3, "from": "diana.ross@acquisition-partners.com", "to": "founder@company.com",
         "subject": "Re: Re: Potential partnership inquiry", "body": "The due diligence report is ready. To proceed, we need a refundable engagement fee of $12,000 to cover legal costs for drafting the LOI and NDA. Wire to: Goldman Sachs Trust, Account 4456718293, Routing 021000021. This is standard practice and fully refundable should either party withdraw. Our window for Q1 commitments closes this Friday.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_026", "pattern": "data_exfiltration",
    "emails": [
        {"turn": 1, "from": "compliance@tax-authority.com", "to": "finance@company.com",
         "subject": "Annual regulatory filing reminder", "body": "Dear Finance Department, this is a reminder that your annual regulatory compliance filing is due within 60 days. Please ensure all required documentation is prepared. We will send detailed requirements in a follow-up communication.", "is_phishing": False},
        {"turn": 2, "from": "compliance@tax-authority.com", "to": "finance@company.com",
         "subject": "URGENT: Document submission required", "body": "As part of the mandatory compliance review, please submit the following within 24 hours: complete employee payroll records including SINs, all T4 summaries for 2024-2025, corporate banking statements, and client payment records. Email all documents directly to this address in Excel format. Failure to comply within the deadline will result in a $50,000 penalty and potential audit escalation.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_027", "pattern": "legitimate",
    "emails": [
        {"turn": 1, "from": "priya@realclient.com", "to": "sales@company.com",
         "subject": "Product demo request", "body": "Hi there, we came across your product at a recent conference and are interested in learning more. Would it be possible to schedule a 30-minute demo sometime next week? We are a team of about 50 and currently evaluating several vendors.", "is_phishing": False},
        {"turn": 2, "from": "priya@realclient.com", "to": "sales@company.com",
         "subject": "Re: Product demo request", "body": "Thanks for the quick response. Wednesday at 2pm works perfectly for us. Can you send a Zoom or Teams link? I will have our CTO and two team leads on the call as well. Looking forward to it.", "is_phishing": False}
    ]
})

threads.append({
    "thread_id": "bec_028", "pattern": "legitimate",
    "emails": [
        {"turn": 1, "from": "facilities@company.com", "to": "allstaff@company.com",
         "subject": "Office maintenance this weekend", "body": "Hi everyone, the building maintenance team will be doing HVAC repairs this Saturday from 8am to 4pm. The office will remain accessible but expect some noise on floors 3 and 4. Please plan accordingly if you were planning to come in.", "is_phishing": False},
        {"turn": 2, "from": "facilities@company.com", "to": "allstaff@company.com",
         "subject": "Re: Office maintenance - Update", "body": "Quick update on the weekend maintenance. The work has been extended to include elevator inspection on Sunday morning from 9am to 12pm. The stairs will be available during that time. Everything should be back to normal by Monday morning. Apologies for any inconvenience.", "is_phishing": False}
    ]
})

threads.append({
    "thread_id": "bec_029", "pattern": "wire_transfer",
    "emails": [
        {"turn": 1, "from": "legal@partner-firm.com", "to": "cfo@company.com",
         "subject": "Closing documents ready", "body": "Dear CFO, the closing documents for the property acquisition are finalized. Everything looks good on our end. We will coordinate payment details once you confirm readiness to proceed.", "is_phishing": False},
        {"turn": 2, "from": "legal@partner-firm.com", "to": "cfo@company.com",
         "subject": "Re: Closing documents - Wire instructions", "body": "We are ready to close. Please wire the deposit of $85,000 to our escrow account: Wells Fargo, Account 8837291045, Routing 121000248. This must be received by 5pm tomorrow to secure the closing date. Please do not use the old account details from our previous transaction as we have switched escrow providers.", "is_phishing": True}
    ]
})

threads.append({
    "thread_id": "bec_030", "pattern": "credential_harvest",
    "emails": [
        {"turn": 1, "from": "noreply@zoom-workspace.com", "to": "user@company.com",
         "subject": "Your Zoom account update", "body": "We are upgrading our platform to improve security and performance. All users will be migrated to the new system over the next two weeks. No action is required at this time. We will notify you when your account is ready for migration.", "is_phishing": False},
        {"turn": 2, "from": "noreply@zoom-workspace.com", "to": "user@company.com",
         "subject": "Action required: Complete your Zoom migration", "body": "Your account is scheduled for migration today. To ensure uninterrupted access to your meetings and recordings, please complete the verification process at https://zoom-secure-migration.com/verify. Enter your current email and password to link your account to the new system. Accounts not verified by midnight tonight will be permanently deactivated and all meeting history will be lost.", "is_phishing": True}
    ]
})

# Save
with open('data/bec_threads/bec_conversations.json', 'w') as f:
    json.dump(threads, f, indent=2)

print("Total threads: " + str(len(threads)))
patterns = {}
for t in threads:
    p = t['pattern']
    patterns[p] = patterns.get(p, 0) + 1
for p, c in sorted(patterns.items()):
    print("  " + p + ": " + str(c))
