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

def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors



    
def main():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci(N) 
    count_vowels("ali")
    n = int(input("Enter a positive integer: "))
    prime_factors(n)

if __name__ == "__main__":
    main()  


