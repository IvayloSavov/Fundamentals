import re

pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"
n = int(input())
count_valid_registrations = 0

for _ in range(n):
    registration = input()
    valid_registration = re.findall(pattern, registration)

    if len(valid_registration) == 0:
        print("Invalid username or password")
    else:
        print("Registration was successful")
        print(f"Username: {valid_registration[0][0]}, Password: {valid_registration[0][1]}")
        count_valid_registrations += 1

print(f"Successful registrations: {count_valid_registrations}")