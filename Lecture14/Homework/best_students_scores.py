student_scores = {"Ivan": 5.00,
                  "Alex": 3.50,
                  "Maria": 5.50,
                  "Georgy": 5.00}
best_students_scores = {}
for student in student_scores:
    if student_scores[student] > 4:
        best_students_scores[student] = student_scores[student]

for student,score in best_students_scores.items():
    print(f"{student:<10}- {score}")