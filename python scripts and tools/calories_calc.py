DEBUG = False

def check_value(val):
    """
    This function helps to avoid empty calories values.
    In case one is found we assumed 0 calories
    """
    try:
        return int(val)
    except:
        return 0

def calculate_calories(each_column):
    """
    This function helps in calculating the calories
    eaten by the user and returning the correct value
    to take decisions more ahead.
    In case of 0 value the user ate less calories than expected,
    otherwise the user ate more than expected.
    """
    calorie_budget_for_day = check_value(each_column[0])
    calories_eaten_breakfast = check_value(each_column[1])
    calories_eaten_lunch = check_value(each_column[2])
    calories_eaten_dinner = check_value(each_column[3])
    #calculate total calories eaten by the user
    total_calories_eaten = calories_eaten_breakfast + calories_eaten_lunch + calories_eaten_dinner
    
    if total_calories_eaten < calorie_budget_for_day:
        if DEBUG:
            print "Calories consumed: " + str(total_calories_eaten)
            print "Budget for this day: " + str(calorie_budget_for_day)
        return 0
    return 1
                
            

if __name__ == "__main__":    
    longest_number_of_days = 0
    longest_number_of_days_list = []
    line_counter = 0
    #open file
    with open("food_diary.txt") as fp:       
        for each_line in fp.readlines():
            line_counter += 1
            each_column = each_line.split(',')                    
            if not calculate_calories(each_column):
                longest_number_of_days += 1
            else:
                longest_number_of_days_list.append(longest_number_of_days)
                longest_number_of_days = 0
        if line_counter < 3:
            print "Number of days must be greater than 2"
        elif line_counter > 50:
            print "Number of days must be less than 50 so this report is based on the first 50 days only so we can give you better perfomance in answering your question."
            longest_number_of_days_list.sort()
            print "The longest number of days that you ate under your calorie budget is " + str(longest_number_of_days_list[-1])
        else:
            longest_number_of_days_list.sort()
            print "The longest number of days that you ate under your calorie budget is " + str(longest_number_of_days_list[-1])


