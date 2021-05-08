# interchange first and last element of a list
def swapList(newList):
    print('Given list:', newList)
    # length of the list
    n = len(newList)
    print('Length:', n)
    # swapping first element with (n-1)th element
    temp = newList[0]
    print('Temp:', temp)
    newList[0] = newList[n-1]
    newList[n-1] = temp
    return newList
