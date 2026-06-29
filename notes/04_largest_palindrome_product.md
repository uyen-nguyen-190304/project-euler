# Problem 4: Largest Palindrome Product

**Problem Statement:**
> A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 \times 99$.
> Find the largest palindrome made from the product of two 3-digit numbers.

**Solution Approach:**

Treat the answer as a 6-digit palindrome of the form $abccba$.
1. Generate palindromes in descending order so larger candidates are tested first.
2. Skip values above the largest possible product of two 3-digit numbers, $999 \times 999 = 998001$.
3. For each palindrome, test whether it can be written as a product of two 3-digit numbers.
4. Use the fact that once $i \times 999$ is smaller than the palindrome, smaller factors cannot work either, so the search can stop early.

The answer was **906609**.
