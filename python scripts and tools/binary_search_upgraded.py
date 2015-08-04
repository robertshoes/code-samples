"""
Implementation of binary search algorithm in python.

by Roberto Zapata
"""

DEBUG = False

def binary_search(target, a_list=[]):
    if not a_list:
        return -1
    a_list.sort()
    max_index = arr_size = len(a_list)
    min_index = 0
    sum_searches = 0
    if DEBUG:
        print "Sorted list --> " + str(a_list)    
    while max_index >= min_index:
        avg_index = (max_index+min_index)/2
        
        if avg_index == arr_size:
            return -1

        if DEBUG:
            print "max_index: " + str(max_index)
            print "min_index: " + str(min_index)
            print "avg_index: " + str(avg_index)
            print "Value found: " + str(a_list[avg_index])
        if target == a_list[avg_index]:
            print "searches --> " + str(sum_searches) 
            return avg_index, target
        elif target < a_list[avg_index]:
            max_index = avg_index - 1
        else: #target > a_list[avg_index]:
            min_index = avg_index + 1

        sum_searches += 1
    return -1
        


if __name__ == '__main__':
    t = 41
    l = [9,7,6,5,0]
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #l = range(20)
    result = binary_search(t, l)
    if result == -1:
        print "Target " + str(t) + " not found on list --> " + str(l)
    else:
        print "Target " + str(t) + " was found on position " + str(result[0]) + " on list --> " + str(l)
    
            
            

    
