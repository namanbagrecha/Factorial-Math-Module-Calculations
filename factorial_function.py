from colorama import Fore

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input(f"{Fore.MAGENTA}Enter a number: "))
fact = factorial(num)
print(f"{Fore.MAGENTA}Factorial of {num} is: {fact}")
