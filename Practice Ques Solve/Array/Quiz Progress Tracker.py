def compute_quiz_differences(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Compute the average score for each quiz
    quiz_averages = []
    for j in range(cols):
        quiz_sum = 0
        for i in range(rows):
            quiz_sum += matrix[i][j]
        quiz_avg = quiz_sum / rows
        quiz_averages.append(quiz_avg)

    # Step 2: Find the difference between consecutive quiz averages
    differences = []
    for j in range(1, cols):
        diff = quiz_averages[j] - quiz_averages[j - 1]
        differences.append(diff)

    return differences

# Driver code
def main():
    # Sample Input
    matrix = [
        [86, 90, 78],
        [88, 85, 80],
        [75, 95, 85],
        [92, 89, 82]
    ]

    print("Quiz Differences:", compute_quiz_differences(matrix))

# Run the driver code
if __name__ == "__main__":
    main()
