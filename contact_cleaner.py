import csv

# Step 1: Load contacts from a CSV file
def load_contacts_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Step 2: Clean name formatting
def format_name(name):
    name = name.strip()
    parts = name.split()
    return " ".join(part.capitalize() for part in parts)

# Step 3: Check if email is valid (basic check)
def is_valid_email(email):
    return "@" in email and "." in email

# Step 4: Check if contact has a phone number
def has_phone_number(contact):
    return contact["phone"].strip() != ""

# Step 5: Load messy data
contacts = load_contacts_from_csv("contacts.csv")
print("📥 Original Contacts:")
for c in contacts:
    print(c)

# Step 6: Format names using map
formatted_contacts = list(map(
    lambda contact: {
        "name": format_name(contact["name"]),
        "email": contact["email"].strip(),
        "phone": contact["phone"].strip()
    },
    contacts
))
print("\n🧼 Formatted Contacts:")
for c in formatted_contacts:
    print(c)

# Step 7: Filter valid emails
valid_contacts = list(filter(
    lambda contact: is_valid_email(contact["email"]),
    formatted_contacts
))
print("\n📧 Valid Emails Only:")
for c in valid_contacts:
    print(c)

# Step 8: Filter contacts that have a phone number
contacts_with_phones = list(filter(has_phone_number, valid_contacts))
print("\n📞 Contacts with Phone Numbers:")
for c in contacts_with_phones:
    print(c)

# Step 9: Remove duplicate contacts by email
unique_contacts = []
seen_emails = set()

for contact in contacts_with_phones:
    email = contact["email"]
    if email not in seen_emails:
        unique_contacts.append(contact)
        seen_emails.add(email)

print("\n✅ Unique Cleaned Contacts (No Duplicates):")
for c in unique_contacts:
    print(c)

# Step 10: Save cleaned contacts to a new CSV file
def save_contacts_to_csv(contacts, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ["name", "email", "phone"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

save_contacts_to_csv(unique_contacts, "cleaned_contacts.csv")
print("\n✅ Cleaned contacts have been saved to 'cleaned_contacts.csv'")


