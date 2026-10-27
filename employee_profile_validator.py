"""String-method practice based on a freeCodeCamp beginner workshop.

This is a combined learning example, not a production-grade validator.
"""

# Find a username in an email
email = "alice.johnson@company.com"
at_position = email.find("@")
print(f"Position of @: {at_position}")
username = email[:at_position]
print(f"Username: {username}")
has_at = "@" in email
print(f"Has @ symbol: {has_at}")
has_com = ".com" in email
print(f"Has .com: {has_com}")

# Clean an employee name
messy_name = "  sARaH dAVis  "
print(f"Original name: '{messy_name}'")
clean_name = messy_name.title()
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

# Clean an email and create a name badge
messy_email = "  SARAH.DAVIS@COMPANY.COM  "
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")
name_badge = clean_name.upper()
print(f"Name badge: {name_badge}")

# Extract a username and turn it into a display name
at_pos = clean_email.find("@")
email_user = clean_email[:at_pos]
print(f"Email: {clean_email}")
print(f"Username: {email_user}")
display_name = email_user.replace(".", " ").title()
print(f"Display name: {display_name}")

# Remove dashes from a phone number
phone = "123-456-7890"
phone_clean = phone.replace("-", "")
print(f"Phone with dashes: {phone}")
print(f"Phone without dashes: {phone_clean}")

# Split and rejoin a building address
full_address = "123 Main Street, Springfield, IL"
address_parts = full_address.split(", ")
print(f"Address parts: {address_parts}")
rejoined = " | ".join(address_parts)
print(f"Rejoined: {rejoined}")

# Check employee code and email suffixes
employee_code = "EMP-2024-SD"
starts_with_emp = employee_code.startswith("EMP")
ends_with_com = clean_email.endswith(".com")
print(f"Employee code: {employee_code}")
print(f"Starts with EMP: {starts_with_emp}")
print(f"Clean email: {clean_email}")
print(f"Ends with .com: {ends_with_com}")

# Count punctuation characters
dot_count = clean_email.count(".")
dash_count = employee_code.count("-")
print(f"Dots in email: {dot_count}")
print(f"Dashes in code: {dash_count}")
