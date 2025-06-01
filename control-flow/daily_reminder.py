# daily_reminder.py
# A simple reminder system using match-case and if statements

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please address it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to finish it when possible.")
    
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority but time-sensitive task. Don't delay too much.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        print("Invalid priority input. Please enter high, medium, or low.")
