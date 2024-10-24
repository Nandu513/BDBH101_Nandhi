def each_digit(number,i):
    digit=number[i]
    return digit

def main():
    num=input("Enter a number: ")
    num=num.strip()
    if num.isdigit():
        for i in range(0, len(num)):
            digit=each_digit(num,i)
            print(digit)
    else:
        print("Enter only the numbers: Try again")
        main()

if __name__ == '__main__':
    main()
