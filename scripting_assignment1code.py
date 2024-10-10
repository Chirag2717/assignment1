# Checking if number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Finding the prime number before the input number
def previous_prime(num):
    for i in range(num - 1, 1, -1):
        if is_prime(i):
            return i
    return None

# Finding next prime number after the input number
def next_prime(num):
    i = num + 1
    while True:
        if is_prime(i):
            return i
        i += 1

# Finding divisors if the number is not prime
def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


while True:
    # User Input
    user_input = input("Please enter the number to check: ")

    # Validation of input (must be a positive whole number)
    if not user_input.isdigit():
        print("That is not a positive whole number. Try again.")
        continue

    num = int(user_input)

    # To show previous prime
    prev_prime = previous_prime(num)
    if prev_prime:
        print(f"The prime number before {num} is {prev_prime}.")
    else:
        print(f"There is no prime number before {num}.")

    # Checking if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        # If not prime, display divisors
        divisors = find_divisors(num)
        print(f"{num} is not prime. Its factors are {', '.join(map(str, divisors))}.")

    # To Show the next prime number
    next_prime_num = next_prime(num)
    print(f"The next prime number after {num} is {next_prime_num}.")

    # Ask from the user if they want to exit
    exit_choice = input("Press Enter to check another number, or type 'exit' to quit: ")
    if exit_choice.lower() == 'exit':
        break
