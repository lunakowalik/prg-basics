time24 = input("Enter time (24-hour format): ")

[hours, minutes] = time24.split(":")
hours = int(hours)

am_pm = "am" if hours < 12 else "pm"

hours12 = hours - 12 if hours > 12 else hours
if hours == 0:
    hours12 = 12

print(f"Time in 12-hour format: {hours12}:{minutes}{am_pm}")
