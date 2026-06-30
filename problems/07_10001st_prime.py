import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check for odd factors up to square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    if n == 1:
        return 2 # The first prime number is 2
    
    # Start counting from the second prime number
    count = 1
    num = 3
    
    while count < n:
        if is_prime(num):
            count += 1
        if count < n:
            num += 2 # Check only odd numbers
    return num
    
def main():
    n = 10001
    nth_prime = find_nth_prime(n)
    print(f"The {n}th prime number is: {nth_prime}")
    
if __name__ == "__main__":
    main()