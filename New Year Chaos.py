'''
In this problem we have to guess the minimum number of bribes that took place in a line.
However, we say the line is "Too Chaotic" is a person bribed more than two other persons.

To solve this problem I used a bubble sort with an optimizer flag, telling whether the array is sorted or not.
Every time a bubble swap took place I added 1 to the number of bribes.

To check if the line is chaotic, you just look if the element is 2 positions further away from the original position to the left.
'''

def minimumBribes (q):
    for index, value in enumerate(q):
            if (value - 1) - index > 2:
                return print('Too chaotic')
        
    swaps = 0
    flag = False

    for i in range(0, len(q)):
        for j in range(0, len(q)-1):
            if q[j] > q[j+1]:
                swaps += 1
                q[j], q[j+1] = q[j+1], q[j]
                flag = True
        if flag:
            flag = False
        else:
            break

    return print(swaps)

minimumBribes(q)