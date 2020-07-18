'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# if 'th' return 1
# else return 0

# if 2 or more letters 'left' recurse
# else return 0
    if len(word) < 2:
        return 0
    
    elif word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])