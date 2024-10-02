def check_prime(num):
    i=num-1
    while i > 1:
        if num % i == 0:
            return False
        i -= 1
    return True

def main():
    num=int(input("Enter a number to check if it is prime or not: "))
    prime=check_prime(num)
    if prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()
