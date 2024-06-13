def fibonacci_sequence(n):
    if n <= 0:
        print("The number of terms must be a positive integer.")
        return
    elif n == 1:
        print([0])
        return
    elif n == 2:
        print([0, 1])
        return

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(fib_sequence)

def main():
    try:
        num_terms = int(input("Enter the number of terms: "))
        fibonacci_sequence(num_terms)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
