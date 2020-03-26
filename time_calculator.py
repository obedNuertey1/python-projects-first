days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def next_day_in_week(num, current_day):
    comment = ''
    comma_and_space = ''
    
    if num == 1:
        comment = ' (next day)'
    elif num >= 2:
        comment = f' ({num} days later)'

