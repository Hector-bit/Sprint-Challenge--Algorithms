'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): 
    num1 = len(word)
    num2 = len('th')

    if (num1 == 0 or num1 < num2):
        return 0
    if word[0:num2] == 'th':
        return count_th(word[num2 - 1:])+1
    return count_th(word[num2 - 1:])


