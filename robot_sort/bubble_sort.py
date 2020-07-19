
def bubble_sort(arr):

    continue_sort = True

    while continue_sort:
        continue_sort = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                continue_sort = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


# simplified speed version to illustrate functional mechanics
def robo_sort(arr):
# rule:
# robo holds a value and swaps with values in list-place
# I cannot for loop, I hold an index and can only move 1 to right and 1 to left each time

    index = 0
    held = None
    continue_sort = True

# grab 1st item, I start loop with one held
# this way I can conditionally put it down at the end when the looping is complete
    held, arr[index] = arr[index], held
    while continue_sort:
        continue_sort = False

        while index < len(arr) - 1:
            index += 1
            if held < arr[index] and index < len(arr) - 1:
                held, arr[index] = arr[index], held
            elif not held < arr[index]: continue_sort = True

# at the last item, I don't want to grab the larger one
# I want the smaller one so I can put the larger one down
        if held > arr[index]: 
            continue_sort = True
            held, arr[index] = arr[index], held

# while moving backwards, I want to pick up the smaller ones
        while index > 1:
            index -= 1
            if held > arr[index]:
                held, arr[index] = arr[index], held
            else: continue_sort = True

        index -= 1
        if not continue_sort: 
            held, arr[index] = arr[index], held

    return arr

unsorted = [5, 4, 3, 2, 1]

print(robo_sort(unsorted))