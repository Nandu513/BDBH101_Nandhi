def division_error(n,d):
    try:
        res=n/d
        return res
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Input must be an integer"
    finally:
        print("Divide numerator by denominator")
if __name__=="__main__":
    numerator=int(input("Enter numerator: "))
    denominator=int(input("Enter denominator: "))
    result=division_error(numerator,denominator)
    print(result)
