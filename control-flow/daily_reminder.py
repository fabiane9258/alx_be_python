task = input("Enter your task: ")
time_bound = input("Is your task time bound? (yes, no)").lower()
priority = input("What is task's priority (high, medium, low): ").lower()


match priority:
    case "high":
        print("Do this task rightaway!: ")
    case "medium":
        print("You don't have much time left, accomplish task?: ")
    case "low":
        print("Remind me later.: ")
if time_bound == "yes":
    print("Be sure to beat the deadline!: ")
elif time_bound == "no":
    print("Take your time")