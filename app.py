name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year
age_months= age*12
age_weeks= age*52
age_days= age*365
print(f"--- {name}, you are {age} years old.")
print(f" {age_months} months old.")
print(f" {age_weeks} weeks old.")
print(f"{age_days} days old.")
