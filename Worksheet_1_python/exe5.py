def compute_power(x,y):
    result=x**y
    return result

def main():
    base=float(input("Enter the base: "))
    power=float(input("Enter the power to be raised to: "))
    result=compute_power(base,power)
    print(result, "is the result of ", base, "power", power)

if __name__=="__main__":
    main()
