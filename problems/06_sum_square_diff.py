def main():
    """
    Naive approach: Depend on computational power of Python
    
    n = 100
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    difference = square_of_sum - sum_of_squares
    print(f"The difference between the square of the sum and the sum of the squares for the first {n} natural numbers is: {difference}")
    """
    # A more concise way to calculate the difference using known formulas
    n = 100
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum  = (n * (n + 1) // 2) ** 2
    difference = square_of_sum - sum_of_squares
    print(f"Difference between the square of the sum and the sum of the squares for the first {n} natural numbers is: {difference}")
    
if __name__ == "__main__":
    main()
    