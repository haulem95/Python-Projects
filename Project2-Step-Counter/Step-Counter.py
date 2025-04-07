print("🏃 STEP COUNTER 🏃")
steps__goal = int(input("♂️ What is your daily step goal: "))
steps = int(input("💫 How many steps have you taken today: "))

if steps < steps__goal:
    print(f"💪 You need {steps__goal - steps} more steps to reach your goals.")
elif steps > steps__goal:
    print(
        f"🎇 Congratulations, for exceeding your goals by {steps - steps__goal} steps")
elif steps == steps__goal:
    print('🎇 Congratulations, for reaching your goal!!')
