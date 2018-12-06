# Complete the countingValleys function below.
def countingValleys(n, s):
    
    tuple_list = []
    temp = 0

    for i in range (0,len(s)):
        if s[i] == 'U':
            temp+=1
            tuple_list.append((i, temp))
        else:
            temp-=1
            tuple_list.append((i, temp))

    valley = 0
    last_step = 0

    for x, y in tuple_list:
        if y != 0:
            last_step = y
        if last_step < 0 and y == 0:
            valley+=1
            
    return valley