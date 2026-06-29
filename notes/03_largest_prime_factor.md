# Problem 3: Largest Prime Factor

**Problem Statement:**
> The prime factors of 13195 are 5, 7, 13 and 29.
> What is the largest prime factor of the number 600851475143?

**Solution Approach:**

Use prime factorization by repeatedly dividing out factors from the number.
1. Divide by 2 until the number is no longer even.
2. Check odd factors starting at 3 and continue up to the square root of the remaining number.
3. If the remaining value is still greater than 2 after the loop, that value is the largest prime factor.

This runs in $O(\sqrt{n})$ time.

The answer was **6857**.
