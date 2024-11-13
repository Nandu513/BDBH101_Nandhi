Worksheet 3 for 
BDBH-101 Computer Programming and Operating Systems - Linux and Python
Semester 1: July - Dec 2024

Revised by
Shyam Rajagopalan & Nithya Ramakrishnan,
IBAB, Bengaluru, India

Python Programming

Worksheet release: 31 Oct 2023
Submission deadline: 11 Nov 2023
Comprehension, Lambda, Decorators & Exceptions

1. You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].  Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]. 

2. You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].Make a variable named fruits_with_only_two_vowels. Use list comprehension to produce ['mango', 'kiwi', 'strawberry'], a list of fruits with only two vowels.

3. Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"],  find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension. “Similar” means: similarity(seq1, seq2) > threshold

4. Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Create a dictionary of numbers and their squares, excluding odd numbers using dictionary comprehension

sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence. The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}

5. Write  a lambda function to sort a list of strings by the last character

6. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

7. Create a logging decorator to record function calls, arguments, and return values. For example, if we have an add function shown below and invoke it as add(2,3), create a decorator that prints the following:
	   # the decorator should print
	   Calling add with args: (2, 3), kwargs: {}
   add returned: 5

	    # add function
	    def add(a, b):
        		return a + b

8. Create a decorator to measure the execution time of a function. Please demonstrate using a sample function (add sleep for checking) and a decorator for this sample function that measures the execution time.

9. Write a function division() that accepts two arguments. The function should be able to catch an exception such as ZeroDivisionError, ValueError, or any unknown error you might come across when you are doing a division operation. Also, add a “finally” construct.

10. You're going to write an interactive calculator! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:

11. If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
If the second input is not '+' or '-', again raise a FormulaError
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

