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

## Problem 4: Largest Palindrome Product

**Problem Statement:**
> A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 \times 99$.
> Find the largest palindrome made from the product of two 3-digit numbers.

**Solution Approach:**

Let's denote a 6-digit palindrome as $abccba$, where $a$, $b$, and $c$ are digits. Note that $a$ cannot be 0, as it is the leading digit. 

Note that the largest 3-digit number is 999. Thus, the largest possible product of two 3-digit numbers is $999 \times 999 = 998001$.

To find the largest satisfying palindrome, we iterate through all possible values of $a$, $b$, and $c$ in descending order, starting from 9 down to 0 (or 1 for $a$). For each combination of $a$, $b$, and $c$, we first check if the constructed palindrome is less than or equal to 998001. If it is, we construct the palindrome and check if it can be expressed as a product of two 3-digit numbers.

To check if a palindrome can be expressed as a product of two 3-digit numbers, we iterate through possible factors starting from 999 down to 100. For each factor $i$, we check if the palindrome is divisible by $i$. If it is, we calculate the corresponding factor $j = \frac{\text{palindrome}}{i}$ and check if $j$ is also a 3-digit number (i.e., between 100 and 999). If both conditions are satisfied, we have found a valid pair of factors.

A small optimization for checking if a number is a product of two 3-digit numbers is when interating $i$ through possible factors starting from 999 down to 100, we check if $i \times 999$ is at least as large as the palindrome. If it is not, we can break early since further decreasing $i$ will only yield smaller products.

## Problem 5: Smallest Multiple

**Problem Statement:**
> 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
> What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

**Solution Approach:**

Note that the smallest number that is evenly divisible by all of the numbers from 1 to $n$ is the least common multiple (LCM) of the numbers from 1 to $n$. Thus, the answer is the LCM of the numbers from 1 to 20, which is **232792560**.