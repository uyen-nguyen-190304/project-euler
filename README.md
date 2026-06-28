# Project Euler - Solutions Archive

## Problem 3: Largest Prime Factor

**Problem Statement:**
> The prime factors of 13195 are 5, 7, 13 and 29.
> What is the largest prime factor of the number 600851475143?

**Solution Approach:**

For this problem, we use the prime factorization method:
1. We start by dividing the given number $n$ by the smallest prime number, and the only even prime, 2. We continue dividing by 2 until $n$ is no longer divisible by 2.
2. Next, we check for odd factors starting from 3 and continue checking up to the square root of $n$. For each odd factor, we divide $n$ as long as it is divisible by that factor.
3. If after checking all factors up to the square root of $n$, the remaining value of $n$ is greater than 2, then that remaining value is also a prime factor and is the largest prime factor of the original number.

This approach has a time complexity of $O(\sqrt{n})$. The answer was **6857**.