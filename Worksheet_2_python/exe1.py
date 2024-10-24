def find_sum(num_list):
    sum_all=0
    for i in num_list:
        sum_all+=i
    return sum_all

def average_num_list(sum_num,l):
    avg_num=sum_num/l
    return avg_num

def main():
    num_list=[1,2,3,4,5]
    print(f'Input: {num_list}')
    length=len(num_list)
    sum_num = find_sum(num_list)
    print("Output:")
    print("Sum of all numbers in numbers list is: ", sum_num)
    avg=average_num_list(sum_num,length)
    print("Average of all numbers in numbers list is: ", avg)

if __name__=="__main__":
    main()
