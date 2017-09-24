#Write a function that merges two sorted lists into a new sorted list.
#  [1,4,6],[2,3,5] → [1,2,3,4,5,6].

def mergeAndSort(lst, lst2):
    lst.extend(lst2)        #extend to merge list 
    lst.sort() #Sorting list

    return lst

print(mergeAndSort([1,4,6], [2,3,5]))