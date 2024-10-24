def decimal_converter(number):
    # print(number)
    sum=0
    number.reverse()
    for i in range(0,len(number)):
        num=((int(number[i]))*(2**i))
        sum+=num
    return sum

def main():
    binary_digits=input( " Enter the binary digit numbers: ")
    num = list(binary_digits)
    count_1s=num.count('1')
    #print(count_1s)
    count_0s=num.count('0')
    #print(count_0s)
    if (count_1s+count_0s)!=len(num):
        print("Please enter only binary digit numbers: 0 or 1, Try again")
        main()
    else:
        x = decimal_converter(num)
        print("The decimal number given binary number", binary_digits, " is: ", x)

if __name__=="__main__":
    main()
