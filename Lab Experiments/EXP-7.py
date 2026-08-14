print("==============================================")
print(" AI IN HEALTHCARE - PROMPT ENGINEERING")
print("==============================================")

topic = input("Enter topic: ")

while True:
    print("\nChoose Prompt Type:")
    print("1. Zero-shot")
    print("2. One-shot")
    print("3. Few-shot")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice in ["1", "2", "3"]:
        break
    else:
        print("Invalid choice! Please enter 1, 2 or 3.")


# ZERO-SHOT
if choice == "1":

    prompt = "Write a 200-word blog about " + topic

    blog = """
Artificial Intelligence is changing the healthcare industry
in many useful ways. It helps doctors diagnose diseases,
analyze medical images and predict health risks. AI systems
can process large amounts of medical information quickly,
which helps healthcare professionals make better decisions.

One important application of AI is disease detection. AI can
analyze X-rays, CT scans and MRI images and help doctors
identify abnormal conditions. AI is also used in drug
discovery to find potential medicines more efficiently.

AI-powered chatbots can answer basic patient questions,
provide health information and help schedule appointments.
AI can also support personalized treatment by analyzing
individual patient information.

Another application is robotic surgery, where intelligent
systems can assist doctors during complex procedures.
Continuous patient monitoring is also possible using
AI-based systems.

However, AI in healthcare must be used carefully. Patient
privacy, data security and ethical issues are important
concerns. Doctors should continue to supervise important
medical decisions.

Overall, Artificial Intelligence has the potential to make
healthcare more accurate, efficient and accessible.
"""


# ONE-SHOT
elif choice == "2":

    prompt = """
Example:

Topic: AI in Education
Blog: Artificial Intelligence helps students through
personalized learning, automated assessment and intelligent
educational tools.

Task:
Write a 200-word blog about """ + topic

    blog = """
Artificial Intelligence is becoming an important technology
in modern healthcare. It supports doctors, nurses and
researchers in providing better healthcare services. AI can
analyze large amounts of medical information and identify
patterns quickly.

AI is widely used in medical diagnosis. It can analyze
medical images such as X-rays, CT scans and MRI scans and
assist doctors in detecting diseases. AI can also predict
patient risks by studying medical records.

Another major application is drug discovery. AI helps
researchers analyze biological information and identify
potential medicines faster. AI-powered chatbots can provide
basic information to patients and assist with appointments.

Artificial Intelligence is also used in robotic surgery.
Robotic systems can help surgeons perform precise movements
during complex operations. AI can continuously monitor
patients and alert healthcare professionals when unusual
conditions occur.

Despite these benefits, healthcare AI has challenges.
Patient privacy, security and ethical issues must be
carefully managed. Human doctors should remain involved
in important medical decisions.

In conclusion, AI can make healthcare faster, smarter and
more efficient while improving patient care and outcomes.
"""


# FEW-SHOT
else:

    prompt = """
Example 1:

Topic: AI in Education
Blog: AI provides personalized learning, automated evaluation
and intelligent educational support.

Example 2:

Topic: AI in Banking
Blog: AI helps banks detect fraud, analyze transactions
and provide better customer service.

Task:
Write a 200-word blog about """ + topic

    blog = """
Artificial Intelligence is revolutionizing healthcare by
supporting diagnosis, treatment and patient management.
Healthcare organizations generate huge amounts of data,
and AI can analyze this information quickly and efficiently.

One of the important applications of AI is medical diagnosis.
AI systems can examine X-rays, CT scans and MRI images and
assist doctors in detecting diseases. This can help identify
health problems at an early stage.

AI is also useful for predicting patient risks. By studying
patient records, AI can identify patterns and alert doctors
about possible health problems. Another important application
is drug discovery, where AI can help researchers find potential
medicines more efficiently.

AI-powered virtual assistants and chatbots can provide basic
health information and help patients schedule appointments.
AI can also support personalized treatment by analyzing
individual patient information.

Robotic surgery is another growing application. AI-supported
robots can assist surgeons in performing precise movements.
AI can also monitor patients continuously and identify
abnormal conditions.

However, healthcare AI must address privacy, security and
ethical concerns. Human professionals should supervise
important medical decisions.

Overall, Artificial Intelligence can improve healthcare by
making diagnosis faster, treatment more personalized and
healthcare services more efficient and accessible.
"""


print("\n==============================================")
print(" SELECTED PROMPT")
print("==============================================")
print(prompt)

print("\n==============================================")
print(" GENERATED 200-WORD BLOG")
print("==============================================")
print(blog)

print("\n==============================================")
print(" RESULT")
print("==============================================")

if choice == "1":
    print("Zero-shot prompting used.")
elif choice == "2":
    print("One-shot prompting used.")
else:
    print("Few-shot prompting used.")

print("Blog generated successfully.")
