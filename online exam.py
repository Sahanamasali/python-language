scores = [78, 85, 62, 90, 70]

total_score = sum(scores)
average_score = total_score / len(scores)

count_above_avg = 0
for score in scores:
    if score > average_score:
        count_above_avg += 1

print("Total Score:", total_score)
print("Average Score:", average_score)
print("Scores Above Average:", count_above_avg)
