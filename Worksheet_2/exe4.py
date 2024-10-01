def decimal_converter(number):
    number=list(number)
    print(number)
    sum=0
    number.reverse()
    for i in range(0,len(number)):
        num=(2*(int(number[i])))**i
        sum=sum+num
    return sum

def main():
    binary_digits=input("Enter the binary digit numbers: ")
    x=decimal_converter(binary_digits)
    print(x)

if __name__=="__main__":
    main()
