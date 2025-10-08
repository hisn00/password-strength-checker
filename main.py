print("Password Strength Checker")

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(c in "@#$%&*!" for c in password):
    score += 1

if score >= 4:
    print("Strong password")
elif score == 3:
    print("Moderate password")
else:
    print("Weak password")
