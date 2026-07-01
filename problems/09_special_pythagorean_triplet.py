def main():
    for a in range(1, 333):
        for b in range(a + 1, 500):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                product = a * b * c
                print(f"The Pythagorean triplet that we are looking for is ({a}, {b}, {c})")
                print(f"Their corresponding product is: {product}")
                return

if __name__ == "__main__":
    main()