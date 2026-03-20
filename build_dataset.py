import os
import email
import random
import csv
import re
from email import policy

def parse_email_file(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            msg = email.message_from_file(f, policy=policy.default)
        
        subject = str(msg['subject'] or '')
        
        body = ''
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_content()
                    break
        else:
            body = msg.get_content()
        
        # Clean up
        body = re.sub(r'<[^>]+>', '', str(body))  # strip HTML
        body = re.sub(r'\s+', ' ', body).strip()
        subject = re.sub(r'\s+', ' ', subject).strip()
        
        if len(body) > 30:
            return subject, body[:3000]
    except:
        pass
    return None, None

# Parse legitimate emails
print("Parsing legitimate emails...")
legit = []
ham_dir = 'data/raw/easy_ham'
for fname in os.listdir(ham_dir):
    if fname.startswith('.'): continue
    subj, body = parse_email_file(os.path.join(ham_dir, fname))
    if subj is not None:
        legit.append((subj, body))
print(f"  Found {len(legit)} usable legitimate emails")

# Parse phishing/spam emails
print("Parsing phishing emails...")
phish = []
spam_dir = 'data/raw/spam'
for fname in os.listdir(spam_dir):
    if fname.startswith('.'): continue
    subj, body = parse_email_file(os.path.join(spam_dir, fname))
    if subj is not None:
        phish.append((subj, body))
print(f"  Found {len(phish)} usable phishing emails")

# Sample 250 of each
random.seed(42)
legit_sample = random.sample(legit, 250)
phish_sample = random.sample(phish, 250)

# Build CSV
rows = []
for i, (subj, body) in enumerate(phish_sample):
    rows.append({'id': f'phish_{i+1:03d}', 'subject': subj, 'body': body, 'label': 1, 'label_text': 'phishing'})
for i, (subj, body) in enumerate(legit_sample):
    rows.append({'id': f'legit_{i+1:03d}', 'subject': subj, 'body': body, 'label': 0, 'label_text': 'legitimate'})

random.shuffle(rows)

out_path = 'data/processed/emails_dataset.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id','subject','body','label','label_text'])
    writer.writeheader()
    writer.writerows(rows)

print(f"\nDataset saved to {out_path}")
print(f"Total: {len(rows)} emails (250 phishing, 250 legitimate)")
