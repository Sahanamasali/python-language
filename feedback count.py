feedback = {
    "Positive": 45,
    "Neutral": 18,
    "Negative": 7
}

total_feedback = sum(feedback.values())
highest_feedback = max(feedback, key=feedback.get)

print("Total Feedback:", total_feedback)
print("Highest Feedback Type:", highest_feedback)
