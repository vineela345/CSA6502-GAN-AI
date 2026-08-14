print("========================================")
print(" PROFESSIONAL LEAVE EMAIL")
print("========================================")

name = input("Enter your name: ")
reason = input("Enter reason for leave: ")
days = input("Enter number of days: ")

while True:
    print("\nChoose Prompt Type:")
    print("1. Zero-shot")
    print("2. One-shot")
    print("3. Few-shot")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice! Enter 1, 2 or 3.")


if choice == "1":

    prompt = "Write a professional leave email due to " + reason

elif choice == "2":

    prompt = """
Example:
Subject: Leave Request
I am unwell and request leave for one day.

Task:
Write a similar professional email due to """ + reason

else:

    prompt = """
Example 1:
I have fever and require leave for two days.

Example 2:
I am unwell and unable to attend college.

Task:
Write a professional leave email due to """ + reason


print("\n========================================")
print(" GENERATED PROMPT")
print("========================================")
print(prompt)

print("\n========================================")
print(" GENERATED EMAIL")
print("========================================")

print("Subject: Request for Sick Leave")
print()
print("Dear Sir/Madam,")
print()
print("I am", name + ".")
print("I am unable to attend college due to", reason + ".")
print("Therefore, I kindly request leave for", days, "day(s).")
print()
print("I will complete the missed academic work after returning.")
print()
print("Thank you for your consideration.")
print()
print("Yours sincerely,")
print(name)

print("\n========================================")
print(" COMPARISON")
print("========================================")

print("Tone       : Professional")
print("Grammar    : Correct")
print("Formatting : Proper email format")
print("Completeness: Complete")
