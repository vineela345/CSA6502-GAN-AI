print("========================================")
print(" AI WORKSHOP PROMOTIONAL POST")
print("========================================")

workshop = input("Enter workshop name: ")
date = input("Enter date: ")
venue = input("Enter venue: ")

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

    prompt = "Create a promotional social media post for an AI Workshop."

elif choice == "2":

    prompt = """
Example:
Join our Python Workshop!
Learn Python and build interesting projects.

Task:
Create a promotional post for an AI Workshop.
"""

else:

    prompt = """
Example 1:
Join our Python Workshop and learn programming.

Example 2:
Join our Data Science Workshop and learn data analysis.

Task:
Create a promotional post for an AI Workshop.
"""


print("\n========================================")
print(" GENERATED PROMPT")
print("========================================")
print(prompt)

print("\n========================================")
print(" SOCIAL MEDIA POST")
print("========================================")

print("🚀", workshop)
print()
print("Explore the exciting world of Artificial Intelligence!")
print()
print("Learn:")
print("• Machine Learning")
print("• Generative AI")
print("• Prompt Engineering")
print("• Real-world AI Applications")
print()
print("Date :", date)
print("Venue:", venue)
print()
print("Register now and enhance your AI skills!")
print()
print("#AI #MachineLearning #GenerativeAI #AIWorkshop")

print("\n========================================")
print(" RESULT")
print("========================================")

print("Promotional post generated successfully.")
