"""Calender-maker, by Kapil Kumar nehra3639@github.com.
Creates a monthly calenders, saved to a text file and fit for printing"""

import datetime

# Set up the constants:
Days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
Months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEPT', 'OCT', 'NOV',
          'DEC')


print('Calender_Maker')
print('Maker:   Kapil Kumar')
print('Email:   nehra3639@gmail.com')

while True:  # Loop to get a year from the user.
    print('Enter the year for the calender: ')
    current_year = input('> ')

    if current_year.isdecimal() and int(current_year) > 0:
        year = int(current_year)
        break

    print('Please enter a year, like 2022.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the numeric value of month, 1-12:')
    current_year = input('> ')

    if not current_year.isdecimal():
        print('Please enter a numeric value for month, like 6 for June.')
        continue
    month = int(current_year)
    if 1 <= month <= 12:
        break
    print('Please enter a number from 1 to 12.')

def getcalenderfor(year, month):
    # cal_text will contain the string of our calendar.
    cal_text = str('')

    # Put the month and year at the top of the calendar:
    cal_text += ('-' * 32) + Months[month - 1] + '-' + str(year) + ('-' * 32 + '\n')

    # Add the days of the week labels to the calendar:
    # Try changing this to abbreviations: SUN, MON, TUE, etc.
    cal_text += '|   SUN   |   MON   |   TUE   |   WED   |   THU   |   FRI   |   SAT   |' + '\n'

    # The horizontal line string that separate weeks:
    week_seperator = ('|_________' * 7) + '|\n'

    # The blank rows have ten spaces in between the | day separators:
    blank_row = ('|         ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all the
    # complicated calendar stuff for us here.)
    current_date = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        cal_text += week_seperator

        # day_number_row is the row with the day_number_label:
        day_number_row = ''
        for i in range(7):
            day_number_label = str(current_date.day).rjust(8)
            day_number_row += '|' + day_number_label + (' ' * 1)
            current_date += datetime.timedelta(days=1)  # Go to next day.
        day_number_row += '|\n'  # Add the vertical line after Saturday

        # Add the day number row and 3 blank rows to the calendar text.
        cal_text += day_number_row

        # (!) Try changing the 4 to a 5 or 10.
        for i in range(1):
            cal_text += blank_row

        # Check if we're done with the month:
        if current_date.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar
    cal_text += week_seperator
    return cal_text


cal_text = getcalenderfor(year, month)
print(cal_text)

# Save the calendar to a text file:
calendarFilename = str('calender_{}_{}.txt'.format(year, month))
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(cal_text)

print('Saved to ' + calendarFilename)
