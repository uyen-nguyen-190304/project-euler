import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    # Naive approach: loop from 2 to n and check for prime factors
    """
    largest_factor = None
    for i in range(2, n + 1):
        if (n % i == 0) and is_prime(i):
            largest_factor = i
    return largest_factor
    """
    
    # Optimized approach: shrinking the number by dividing out factors
    largest_factor = -1
    
    # First, shrink n by dividing out the 2s (only even prime factor)
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
        
    # Now, n must be odd
    # We check for odd factors up to sqrt(n)
    i = 3
    while i * i <= n:
        # If i is a factor, divide n by i exhaustively and update largest_factor
        while n % i == 0:
            largest_factor = i
            n //= i
            
        # Increment by 2 to check only odd numbers
        i += 2
    
    # If, after all the divisions, n is strictly greater than 2
    # Then n itself now must be a prime number and is the largest prime factor
    if n > 2:
        largest_factor = n
    
    # Return the largest prime factor found, or -1 if no prime factors were found
    return largest_factor
    

def main():
    n = int(input("Enter a number: "))
    result = largest_prime_factor(n)
    print(f"The largest prime factor of the number {n} is: {result}")    
    
if __name__ == "__main__":
    main()
    