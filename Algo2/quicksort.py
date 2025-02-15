myList = [4,1,5,3,19,83,23,53,3,4]
size = len(myList)

def partition(array, low, high):
    pivot = array[high]
    i = low -1

    for j in range(low,high):
        if array[j] <= pivot:

            i = i+1
            (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1



