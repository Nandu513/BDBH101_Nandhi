def binary_convert(quotient):
    remainder = ""
    while quotient >=1 :
        new_quotient=quotient//2
        remainder+=str((quotient%2))
        quotient=new_quotient
    return remainder

def main():
    number=int(input("Enter a decimal number: "))
    x=binary_convert(number)
    print("The binary number of 1s in binary representation", x[::-1]," of", number, ": ", x[::-1].count('1'))

if __name__=="__main__":
    main()
