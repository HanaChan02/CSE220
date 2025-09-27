def compute_sales_trends(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Compute the total sales for each product
    product_totals = []
    for j in range(cols):
        product_sum = 0
        for i in range(rows):
            product_sum += matrix[i][j]
        product_totals.append(product_sum)

    # Step 2: Compute the total sales across all products
    total_sales = sum(product_totals)

    # Step 3: Compute the percentage contribution of each product
    product_percentages = []
    for total in product_totals:
        percentage = (total / total_sales) * 100
        product_percentages.append(percentage)

    # Step 4: Compute the difference between consecutive product percentages
    differences = []
    for j in range(1, cols):
        diff = product_percentages[j] - product_percentages[j - 1]
        differences.append(diff)

    return differences

# Driver code
def main():
    # Sample Input
    matrix = [
        [100, 200, 300],
        [150, 250, 350],
        [120, 180, 290]
    ]

    print("Sales Trend Differences:", compute_sales_trends(matrix))

# Run the driver code
if __name__ == "__main__":
    main()
