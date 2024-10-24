def squares(n):
    square=[]
    for i in range(1, n+1):
        square.append(i**2)
    return square
def sum_sq():
    sum_all=0
    num = int(input( "Enter the range of number(like; 10 means for 1st 10 numbers): "))
    if num<0:
        print("Please enter a valid range, enter only positive number as input")
    else:
        square=squares(num)
        print(square)
        for i in range(0,len(square)):
                sum_all+=square[i]
        print (sum_all, "is the sum of all squares of first", num, "numbers")

if __name__=="__main__":
    sum_sq()
