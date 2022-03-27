'''
Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

spam = ['apples', 'bananas', 'tofu', 'cats']

def convert_to_sentence(arr: list) -> str:
    sentence = ', '.join(arr[:-1])
    if len(arr) > 1:
        sentence += ', and ' + arr[-1]
    elif len(arr) == 1:
        sentence += arr[-1]
    return sentence

print(convert_to_sentence(spam))
