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

    
def main():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci(N) 
    count_vowels("ali")
    calculate_average(numbers)
    numbers = [float(x) for x in input("Enter any numbers : ").split()]
    result = calculate_sum(*numbers)
    print("Sum:", result)


if __name__ == "__main__":
    main()  


