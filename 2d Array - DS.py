def num_of_hourglass(arr):
    hourglass_list = []
    val = 0
    for r in range (1,len(arr)-1):
        for c in range(1,len(arr[r])-1):
            val = arr[r][c] + arr[r-1][c] + arr[r+1][c] + arr[r-1][c-1] + arr[r-1][c+1] + arr[r+1][c-1] + arr[r+1][c+1]
            hourglass_list.append(val)
            val = 0 
    return max(hourglass_list)