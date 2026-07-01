# Problem 9: Special Pythagorean Triplet

**Problem Statement:**
> A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
>
> $$a^2 + b^2 = c^2$$
>
> For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
>
> There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. Find the product $abc$.

**Solution Approach:**

We use a brute-force approach. Since $a < b < c$, the most $a$ can be is 332 and the most $b$ can be is 499. We can iterate through all possible values of $a$ and $b$, calculate $c$ as $1000 - a - b$, and check if they satisfy the Pythagorean condition. If they do, we compute the product $abc$.

The complexity of this approach is $O(N^2)$, where $N$ is the maximum value of $a$ and $b$. The answer was **31875000**.