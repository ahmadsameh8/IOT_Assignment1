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


    # Calculating_Sum 
def calculate_sum(*args):
    total = sum(args)
    return total
    
def main():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci(N) 

    # calculate_sum 
    numbers = [float(x) for x in input("Enter any numbers : ").split()]
    result = calculate_sum(*numbers)
    print("Sum:", result)

if __name__ == "__main__":
    main()  

