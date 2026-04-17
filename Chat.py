# Lab02_pairNumber
# Smart Classroom Quiz & Performance Analyzer

# Step 1: Store last two digits of student IDs
student1_last = 83   # Sonam
student2_last = 69   # Karma

# Step 2: Generate unique value
unique_value = (student1_last + student2_last) % 10

# Display the unique value
print("Unique Value Generated:", unique_value)

# Step 3: Create dictionary to store student names
students = {}

print("\nEnter student names (type 'exit' to stop):")

# Loop to take input
while True:
    name = input("Enter student name: ")
    
    # Stop when user types exit
    if name.lower() == "exit":
        break
    
    # Skip blank names
    if name.strip() == "":
        print("⚠️ Warning: Name cannot be empty. Skipping...")
        continue
    
    # Store name in dictionary
    students[name] = 0   # initial score = 0

# Display all student names
print("\nList of Students:")
for student in students:
    print("-", student)

# Step 4: Conduct Quiz
for student in students:
    print(f"\nQuiz for {student}")
    score = 0

    # Question 1
    ans1 = int(input(f"Q1: {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1

    # Question 2
    ans2 = int(input(f"Q2: {unique_value} * 3 = "))
    if ans2 == unique_value * 3:
        score += 1

    # Question 3
    ans3 = int(input(f"Q3: {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1

    # Store score
    students[student] = score

# Step 5: Analyze Performance
print("\n--- Performance Analysis ---")

for student, score in students.items():
    print(f"\nStudent: {student}")
    print("Score:", score)

    # Warning if score is 0
    if score == 0:
        print("⚠️ Warning: Very low performance!")

    # Performance Level
    if score == 3:
        level = "Excellent"
    elif score == 2:
        level = "Good"
    elif score == 1:
        level = "Average"
    else:
        level = "Poor"

    print("Performance Level:", level)

    # Certificate Eligibility
    if score >= 2:
        print("Certificate: Eligible ✅")
    else:
        print("Certificate: Not Eligible ❌")

    # Step 6: Star Pattern
    print("Stars Pattern:")
    for i in range(score):
        print("*")
        print("sonam")
        print()