"""
List intersection: Finds intersections between various lists
"""


def check_intersection(first_list, second_list):
    #We use set builtin function to find the intersection between lists 
    return set(first_list).intersection(second_list)


def create_lists(line):
    #receive a line from the file containing ascending numbers
    #each line is of the form 'n,n,n;n,n,n' where n is a number
    #and the semi-colon separates the lists
    first, second = line.split(';')
    #Make sure that we have a list of numbers and not numbers and commas
    first = [x for x in first.split(',')]
    second = [x for x in second.split(',')]
    #look for the intersection
    intersected_number = check_intersection(first, second)
    
    if intersected_number:
        intersected_numbers_sorted = [eachNumber for eachNumber in intersected_number]
        intersected_numbers_sorted.sort()
        print ','.join(intersected_numbers_sorted)
    else:
        print ""
    #return 0


if __name__ == '__main__':
    #l = ["1,2,3;3,4,5", "1,2,3;0,4,5", "7,8,9;8,9,10,11,12"]
    l = ["1,2,3,4;4,5,6", "20,21,22;45,46,47", "7,8,9;8,9,10,11,12"]
    for eachLine in l:
        create_lists(eachLine)
    
