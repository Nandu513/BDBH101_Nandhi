def squares(n):
    square=[]
    for i in range(1, n+1):
        square.append(i**2)
    return square
def sum():
    sum=0
    num = int(input("Enter the range of number(like; 10 means for 1st 10 numbers): "))
    square=squares(num)
    print(square)
    for i in range(0,len(square)):
        sum+=square[i]
    print (sum)

if __name__=="__main__":
    sum()
