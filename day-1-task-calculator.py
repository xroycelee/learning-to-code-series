
print("Lets find out what percentage of your day is spent doing a task.")

print("What is the name of this task?")
task_name = input()

print("how many minutes did you spend on it?")
duration = input()
duration = int(duration)

quantity = int(duration/(24*60)*100)

print(f"{quantity}% of your day was spent {task_name}")

