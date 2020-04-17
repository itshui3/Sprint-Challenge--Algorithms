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


c)

## Exercise II


