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
    new_am_or_pm = 'AM' if new_hour < 12 else 'PM'

    # Calculate the number of days passed
    days = total_hours // 24

    return {
        'hour_on_clock': display_hour,
        'new_minutes_str': f'{new_minutes:02d}',  # Ensures 2-digit format
        'new_am_or_pm': new_am_or_pm,
        'days': days
    }

def add_time(start, duration, day=""):
    time_dict = get_new_time(start, duration)
    day_in_week = next_day_in_week(time_dict['days'], day)

    return f'{time_dict["hour_on_clock"]}:{time_dict["new_minutes_str"]} {time_dict["new_am_or_pm"]}{day_in_week}'

# Examples:
print(add_time('3:00 PM', '3:10'))  # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # 2:02 PM, Monday
print(add_time('10:10 PM', '3:30'))  # 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # 7:42 AM (9 days later)
