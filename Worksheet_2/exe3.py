def binary_convert(quotient):
    remainder = []
    while quotient >=1 :
        new_quotient=quotient//2
        remainder.append(quotient%2)
        quotient=new_quotient
    return remainder

def main():
    number=int(input("Enter a decimal number: "))
    x=binary_convert(number)
    x.reverse()
    print(x)
    print(x.count(1))

if __name__=="__main__":
    main()
