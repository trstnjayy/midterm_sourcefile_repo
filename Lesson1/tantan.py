scores = [85, 72, 91, 64, 78]

passed = 0
failed = 0

print("Student Scores:")

for i, score in enumerate(scores):
    if score >= 75:
        if score >= 90:
            remark = "Excellent"
        elif score >= 80:
            remark = "Very Good"
        else:
            remark = "Good"
        print(f"Student {i+1}: {score} - {remark} - Passed")
        passed += 1
    else:
        print(f"Student {i+1}: {score} - Failed")
        failed += 1

print("\nTotal:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Passed:", passed)
print("Failed:", failed)