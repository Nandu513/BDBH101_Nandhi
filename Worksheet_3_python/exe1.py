def capitalize_fruits(fruit_list):
    capitalized_fruits = [i.capitalize() for i in fruit_list]
    return capitalized_fruits
def main():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    result=capitalize_fruits(fruits)
    print(result)
if __name__ == '__main__':
    main()
