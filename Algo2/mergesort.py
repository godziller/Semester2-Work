myList = [1,2,3,4,5,7,8,9]

def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(mylist):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        else:
            mylist[f1+f2] = list2[f2]
            f1+=1


def mergesort(mylist):
    n = len(mylist)
    if n>1:
        list1 = mylist[:n // 2]
        list2 = mylist[n // 2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)


list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8]
my_list = [0] * 10

merge(list1, list2, my_list)
print(my_list)

mergesort(myList)
print(myList)