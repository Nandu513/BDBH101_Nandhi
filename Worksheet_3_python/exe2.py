fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
def count_vowels(string):
    vowel_count = 0
    for letter in string:
        if letter.lower() in 'aeiou':
            vowel_count += 1
    return vowel_count
if __name__ == '__main__':
    fruits_with_only_two_vowels=[ i for i in fruits if count_vowels(i)==2]
    print(fruits_with_only_two_vowels)
