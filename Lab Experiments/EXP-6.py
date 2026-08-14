print("SMART FITNESS WATCH")
print("-------------------")

product = input("Enter product name: ")

while True:
    print("\nChoose Prompt Type")
    print("1. Zero-shot")
    print("2. One-shot")
    print("3. Few-shot")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice in ["1", "2", "3"]:
        break
    else:
        print("Please enter only 1, 2, or 3.")

if choice == "1":

    prompt = "Write a product description for " + product

elif choice == "2":

    prompt = """
Example:
Smart Band: Tracks steps, heart rate and sleep.

Task:
Write a product description for """ + product

else:

    prompt = """
Example 1:
Smart Band: Tracks steps and heart rate.

Example 2:
Smart Watch: Provides notifications and fitness tracking.

Task:
Write a product description for """ + product


print("\n========== GENERATED PROMPT ==========")
print(prompt)

print("\n========== OUTPUT ==========")

if choice == "1":
    print(product, "is a modern smart wearable designed for fitness and health tracking.")

elif choice == "2":
    print(product, "helps users track steps, heart rate, calories and daily activities.")

else:
    print(product, "provides advanced fitness tracking, heart-rate monitoring,")
    print("sleep analysis, workout tracking and smart notifications.")
