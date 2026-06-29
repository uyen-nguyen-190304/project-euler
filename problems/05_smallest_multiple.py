import math

def main():
    lcm = math.lcm(*range(1, 21))
    print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {lcm}")

if __name__ == "__main__":
    main()
