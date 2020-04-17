'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #Understand
    #Given a string, count the occurences of 'th' within recursively

    #Plan
    #My first pass attempt will involve reducing the string by 1 character
    #Each recurse. Starting from the left hand side, 
    # Determine if [0] + [1] == 'th'
    #If so: leave behind a return 1 + recurse(word[1:])
    #recurse case will remove
    #1 Character each time
    #Until it reaches the base case of (?) Determine duringg execution

    if(len(word) < 2):
        return 0 #Base case returns 0 after there are less characters than is possible to perform a 'th' check on. The returns need to add up to a count

    if(word[0] + word[1] == 'th'):
        return 1 + count_th(word[2:])

    return count_th(word[1:])