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

def calculate_average(*args):
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)
print(average)   


    
def main():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    generate_fibonacci(N) 
    count_vowels("ali")
    average = calculate_average(2, 4, 6, 8)



if __name__ == "__main__":
    main()  


