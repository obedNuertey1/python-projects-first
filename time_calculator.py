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
    [time_string, am_or_pm] = start.split(' ')
    [start_time_hour, start_time_min] = list(map(int, time_string.split(':')))
    [duration_hour, duration_min] = list(map(int, duration.split(':')))

    # Convert start time to 24-hour format
    if am_or_pm == 'PM':
        start_time_hour += 12
    
    # Calculate new total minutes and hours
    total_minutes = start_time_min + duration_min
    total_hours = start_time_hour + duration_hour + (total_minutes // 60)
    new_minutes = total_minutes % 60
    
    # Calculate the new hour in 12-hour format
    new_hour = total_hours % 24
    display_hour = new_hour % 12
    if display_hour == 0:
        display_hour = 12
    
    # Determine AM/PM
