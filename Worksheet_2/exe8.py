def string(s):
    length= float(len(s)/2)
    if s.strip()=="":
        return 'String is empty'
    else:
        return s[:int(length)]

def main():
    string_half=input("Enter a string: ")
    half_string=string(string_half)
    print("The half of the", string_half, "is", half_string)

if __name__ == '__main__':
    main()
