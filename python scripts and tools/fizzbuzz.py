"""
This is a FizzBuzz function that
prints F for Fizz, B for Buzz and
FB for FizzBuzz.
It receives a list of lists.  Each
list contains three numbers:
first_number --> will print F
second_number --> will print B
third_number --> will be the limit of the counter

For example: given '1 3 10'
will count until 10 and will check
which numbers are divisible between
1 to print 'F' and 3 to print 'B'
and 'FB' if the number is divisible by
1 and 3.
"""


def fizz_buzz(fname):

    for eachLine in fname:
        eachLine = [int(x) for x in eachLine.split()]
        
        first_num = eachLine[0]
        second_num = eachLine[1]
        superior_limit = eachLine[2]

        if first_num > 20 or second_num > 20:
            raise Exception("Limits cannot be greater than 20")

        #If you want to put a limit to the third number
        #uncomment this part
        
        #if superior_limit < 21 or superior_limit > 100:
        #    raise Exception("Superior limit cannot be lower than 21 or greater than 100")
        
        ln = ""        
        for num in range(1,superior_limit+1):
            if num % first_num == 0 and num % second_num == 0:
                ln += "FB "
            elif num % second_num == 0:
                ln += "B "
            elif num % first_num == 0:
                ln += "F "
            else:
                ln = ln + str(num) + " "
        print ln.strip()

    return 0


if __name__ == '__main__':
    tests = [["3 5 10"]]
    for eachTest in tests:
        fizz_buzz(eachTest)

