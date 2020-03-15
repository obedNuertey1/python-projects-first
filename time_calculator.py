days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def next_day_in_week(num, current_day):
    comment = ''
    comma_and_space = ''
    
    if num == 1:
        comment = ' (next day)'
    elif num >= 2:
        comment = f' ({num} days later)'

    if not current_day:
        return comment
    
    if current_day:
        comma_and_space = ', '

    index_of_current_day = days_of_the_week.index(current_day.lower())
    raw_newday_number = num + index_of_current_day
    newday_index = raw_newday_number % len(days_of_the_week) 
    next_day = days_of_the_week[newday_index]

    return comma_and_space + next_day.title() + comment

def get_new_time(start, duration):
