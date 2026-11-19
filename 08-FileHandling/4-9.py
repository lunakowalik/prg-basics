import csv

file_name = "it_company.csv"
target_role = "Graphic Designer"

print("GRAPHIC DESIGNERS")
print("=================")

try:
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Normalize keys/values slightly in case of extra spaces around headers or fields
            clean_row = {k.strip(): v.strip() for k, v in row.items() if k and v}
            job_title = clean_row.get("Job Title")

            if job_title == target_role:
                first_name = clean_row.get("First Name")
                last_name = clean_row.get("Last Name")
                email = clean_row.get("Email")
                print(f"{first_name} {last_name},{email}")

except FileNotFoundError:
    print(f"Error: '{file_name}' was not found.")