# Problem 6: Sum Square Difference

**Problem Statement:**
> The sum of the squres of the first ten natural numbers is,
>
> $1^2 + 2^2 + ... + 10^2 = 385$
>
> The square of the sum of the first ten natural numbers is,
>
> $(1 + 2 + ... + 10)^2 = 55^2 = 3025$
>
> Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
>
> Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

**Solution Approach:**

Note that the sum of the squares of the first $n$ natural numbers is given by the formula: $$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$

Meanwhile, the square of the sum of the first $n$ natural numbers is given by: $$\left(\sum_{i=1}^{n} i\right)^2 = \left(\frac{n(n+1)}{2}\right)^2$$

Thus, using these formulas, we can compute the difference for $n=100$ directly without needing to iterate through all numbers.

The answer was **25164150**.