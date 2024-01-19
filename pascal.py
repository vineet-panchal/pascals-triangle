import math

def pascal(num):
    for i in range(num):
        for j in range(num - i + 1):
            print(" ", end="")
        for k in range(i + 1):
            print(math.factorial(i) // (math.factorial(k) * math.factorial(i - k)), end=" ")
        print("\r")

if __name__ == "__main__":
    pascal(10)