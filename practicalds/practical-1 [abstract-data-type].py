#Abstract Data Type

from array import *

def insert(array1,index,element):
    array1.insert(index,element)

def traverse(array1):
    for x in array1:
        print(x,end=" ")

def delete(array1,element):
    array1.remove(element)

def search(array1, n, element):
    for i in range(n):
        if (array1[i] == element):
            return i
    return -1

if __name__ == '__main__':
    array1 = array('i', [10,20,30,40,50])
    traverse(array1)
    n = len(array1)
    index = int(input("\nEnter index at which element to be inserted:"))
    element = int(input("\nEnter element to be inserted:"))
    insert(array1,index,element)
    print("Array after Insertion")
    traverse(array1)
    element = int(input("\nEnter element to be deleted:"))
    delete(array1,element)
    print("Array after deletion")
    traverse(array1)
    element = int(input("\nEnter element to be searched:"))
    index = search(array1, n, element)
    if index !=-1:
        print("Element Found at position: " + str(index + 1))
    else:
        print("Element not found")
