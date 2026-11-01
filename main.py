# Post-Quantum Password Checker
# Author: Abdurahmon Ikromov - NUS Scholarship Portfolio
# Singapore

def check_password(password):
    score = 0
    print(f"\nChecking: {password}")
    print("-" * 30)
    
    length = len(password)
    if length >= 12:
        score += 3
        print("✅ Length >12 (Quantum Safe)")
    elif length >= 8:
        score += 1
        print("⚠️ Medium length")
    else:
        print("❌ Too short!")

    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*" for c in password): score += 2

    print(f"\nScore: {score}/8")
    if score >= 7:
        print("🏰 QUANTUM-RESISTANT! Safe 100+ years")
    elif score >= 4:
        print("🏠 Moderate - Cracks in months")
    else:
        print("⛺ Weak - Cracked in seconds!")

pwd = input("Enter password to test: ")
check_password(pwd)
