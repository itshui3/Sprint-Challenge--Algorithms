#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

If we consider that a necessarily begins at 0 in this problem, we can then refactor the logic to become: 
how many increments of n^2 does it take to reach n^3? 
and because n * n^2 = n^3, the time complexity of this problem is O(n)
It will take n amounts of n^2 increments to reach n^3
ie. if n = 3
3^2 = 9
3^3 = 27
27 / 9 = 3


b) O(n log n)
Within this problem are two iterative loops. The outer loop runs a time complexity of O(n) because the number of iterations in a for in with the range set to (n) will run in linear time respective to the size of 'n' input. 
The while loop inside also uses n to determine when to stop. However, the iterator is doubled each time. Because EACH iteration of this loop doubles the count of 'j', this makes the time complexity of the inner loop O(log n)
As it is nested within the n time complexity loop, the number of times this is run becomes multiplied by n, thus: O(n * log n)


c) O(n)
A recursive function is run that repeatedly passes in an integer of one less until the integer becomes 0, at which point the recursion ends. Written out this way, it is clear that the time complexity is : O(n)

## Exercise II

Given a building with 'n' amount of stories, and 'plenty' of eggs. 
If an egg gets broken thrown off floor f or higher:

if(thrown.floor >= floor.f):
    break()
else:
    notBreak()

Assuming the ability to determine the floor level break point of eggs
Devise a strat to determine value of f that will minimize the number of dropped/broken eggs. 

Questions: 
Can we consider this a problem of time complexity in relation to an input, and t hat input being 'n'? 
If I can break physics and determine which floor level the eggs will break out, what's stopping me from writing an algorithm that assigns f to whatever 'n' number of floors are present in the building? 

def get_floor(n): O(1)
    return n

#Understand
So the floor 'f' is determined by the laws of the world that the building inhabits. My goal is to determine which floor that is ggiven infinite eggs but with the intention of reducing the number I use to test where they can break. 

#Plan A
I start with a basic first pass solution that is also the worst solution. Iterate through the floors dropping eggs until one breaks. In this case I will necessarily drop f number of eggs. Highly inefficient solution. 

#Execute A
f = 0
for i in range(n):
    broken = dropEgg(i)

    if(broken):
        f = i

#Reflect Plan A
Rather than countingg individually towards 'n', perhaps there is a better way to take into account the size of 'n' and approach 'f' more broadly. For instance, if I split 'n' in half. With a mid integer, lower list, higher list of numbers and drop the egg at mid, this will show me if 'f' exists in the lower floors or the upper floors relative to n/2. 

f = None
mid = n//2
lower = 0 to n//2 - 1
upper = n//2 + 1 to n

while True:

    broken = dropEgg(n//2)

    if(broken):
        #f is in lower half, write logic to reassign mid/lower/upper
        if(not dropEgg(n//2) - 1): # I check one lower, and if it doesn't break then I have identified my f
            f = n//2 - 1

        mid = lower//2
        lower = 0 to lower//2
        upper = lower//2 + 1 to mid
    else:
        #f is in upper half, write logic to reassign mid/lower/upper
        if(not dropEgg(n//2) + 1): # I check one lower, and if it doesn't break then I have identified my f
            f = n//2 + 1

        mid = upper//2
        lower =  to upper//2
        upper = upper//2 + 1 to n

#Reflect Plan B
Each iteration:
Cut the total number of floors 'n' in half in each iteration
Drop egg on mid -> check one above or one below depending on if egg breaks
Determine whether to use lower or upper set of floors in next iteration
This logic should run at time complexity of O(log n)
Although there is an extra check, that will only add a constant multiplier of 2. O(2 * log n). 
However, we don't care about the 2 so it becomes O(log n)