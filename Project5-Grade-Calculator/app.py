print("GRADE CALCULATOR")
scores = []

while True:
    score = input("Enter a test score: ")
    if score.lower() == 'done':
        print("Goodbye")
        break

    scores.append(float(score))
    average = sum(scores) / len(score)
    print(f"Average: {average:.1f}")
    if average >= 90:
        print("Grade A")
    elif average >= 80:
        print("Grade B")
    elif average >= 70:
        print("Grade C")
    elif average >= 60:
        print("Grade D")
    else:
        print("Failed")
