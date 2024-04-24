student_scores = {"Ivan": 5.00,
                  "Alex": 3.50,
                  "Maria": 5.50,
                  "Georgy": 5.00}

max_score = max(student_scores, key = student_scores.get)
min_score = min(student_scores, key = student_scores.get)

print(f"Student with max score: {max_score} ({student_scores[max_score]})")
print(f"Student with min score: {min_score} ({student_scores[min_score]})")