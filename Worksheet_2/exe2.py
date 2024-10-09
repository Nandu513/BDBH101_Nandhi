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
    print(x[::-1], "is the binary number of", number)

if __name__=="__main__":
    main()
