def negative_positive_sort(ar_list):
    x = sorted(ar_list, key=lambda x: (x, x <= 0))
    return x
if __name__ == '__main__':
    ar=[-5,-2,8,3,-1,2,0,-3,4,5,-6]
    print(negative_positive_sort(ar))
