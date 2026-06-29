HIGH_CAP = 998_001

def largest_palindrome_product():
    """
    Largest palindrome product of two 3-digit numbers
    """
    # a cannot be 0 because it's the leading digit     
    for a in range(9, 0, -1):
        # b and c can be 0
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                # Dynamically generate palindrome number
                palindrome = int(f"{a}{b}{c}{c}{b}{a}")
                # Skip palindromes that are too large (greater than 998_001)
                if palindrome < HIGH_CAP:
                    # Check if this palindrome has two 3-digit factors
                    for i in range(999, 99, -1):
                        # Optimize: If x multiplied by the max 3-digit number (999)
                        # is less than the palindrome, no smaller x can possibly work
                        if i * 999 < palindrome:
                            break
                         
                        # Now check if i is a factor of the palindrome
                        if palindrome % i == 0:
                            # If yes, check if the corresponding factor is a 3-digit number
                            j = palindrome // i
                            if 100 <= j <= 999:
                                return palindrome
                            
    # Safety net to return None if no palindrome product is found (should not happen)
    return None

def main():
    result = largest_palindrome_product()
    print(f"The largest palindrome product of two 3-digit numbers is: {result}")
    
if __name__ == "__main__":
    main()