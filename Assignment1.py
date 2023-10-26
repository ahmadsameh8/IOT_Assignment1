# write functions here
#fibonacci function
def generate_fibonacci(N):
    if N <= 0:
        print("Please enter a positive integer for N.")
        return

    if N == 1:
        print("0")
        return
    elif N == 2:
        print("0 1")
        return

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < N:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Convert the list to a space-separated string for printing
    fibonacci_str = ' '.join(map(str, fibonacci_sequence))
    print(fibonacci_str)

def count_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    print  (count)
    return count
def calculate_sum(*args):
    total = sum(args)
    return total
  
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
numbers = input("numbers: ").split()
numbers = [int(num) for num in numbers]

average = calculate_average(numbers)
print(average)   


def isPrime(n): #implemented by Muhammad Hesham
    if n == 2:
        return True
    #check if the num is even(not 2) or one so it is not a prime num.
    if n < 2 or n % 2 == 0: 
        return False
    # loop starting from 3 and move 2 steps and stope when i^2 is > n;
    # if the num didn't divided with any value of i so it is a prime num.
    for i in range(3, int(n**0.5) + 1, 2): 
        if n % i == 0:
            return False
    return True

    
def main():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci(N) 
    count_vowels("ali")
    calculate_average(numbers)
    numbers = [float(x) for x in input("Enter any numbers : ").split()]
    result = calculate_sum(*numbers)
    print("Sum:", result)

    #Test isPrime() function
    n = int(input("Enter any number to check isPrime() function: "))
    if(isPrime(n)) :
        print(n, "Is Prime num.")
    else:
        print(n, "Is not Prime num.")


if __name__ == "__main__":
    main()  


