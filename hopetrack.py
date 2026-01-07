
# HopeTrack – Skill & Habit Consistency Tracker
# Beginner-friendly Python project (1st Semester)

items = {}  # stores habits/skills as: {name: [completed_days, total_days]}

while True:
    print("\n=== HopeTrack – Skill & Habit Consistency Tracker ===")
    print("1. Add Habit / Skill")
    print("2. Log Today’s Activity")
    print("3. View Consistency Report")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        name = input("Enter habit or skill name: ")

        if name not in items:
            items[name] = [0, 0]
            print(f"'{name}' registered successfully.")
        else:
            print("This habit/skill already exists.")

    elif choice == "2":
        name = input("Enter habit or skill name: ")

        if name in items:
            done = input("Was this completed today? (yes/no): ")

            items[name][1] += 1  # total days

            if done.lower() == "yes":
                items[name][0] += 1  # completed days

            print("Activity logged successfully.")
        else:
            print("Habit/Skill not found. Please add it first.")

    elif choice == "3":
        print("\n--- Consistency Report ---")

        if not items:
            print("No habits or skills added yet.")
        else:
            for name in items:
                completed = items[name][0]
                total = items[name][1]

                if total == 0:
                    percentage = 0
                else:
                    percentage = (completed / total) * 100

                status = "Needs Improvement" if percentage < 50 else "Good Consistency"

                print(f"{name}: {percentage:.2f}% → {status}")

    elif choice == "4":
        print("Application closed. Keep improving consistently!")
        break

    else:
        print("Invalid selection. Please choose a valid option (1–4).")