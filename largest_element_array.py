def LE(arr):
    print('Given Array:', arr)
    # arr[]= {}
    n = len(arr)
    max = arr[0]
    for i in  range(1,n):
        if arr[i]> max:
            max = arr[i]
    return max
