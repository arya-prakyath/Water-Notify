"""
    Author: THE_ARYA
    Application Name:   Water Notification System
    Desc:   This app notifies a 'Drink Water' reminder to the user every hour
"""

# External packages
from plyer import notification
import time

# main()
# Initialize reminder counter for the day
counter = 1

# Initialize previous notification day
dayLast = 0

# Initialize days list and dict
dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
daysDict = {x: y for y, x in enumerate(dayList)}

# Run program forever until stopped
while True:
    # Current time
    timeStamp = time.asctime(time.localtime(time.time()))

    # Current Day while notifying
    dayNow = daysDict[timeStamp.split(' ')[0]]

    # Time when notified
    timeNow = timeStamp.split(' ')[3]

    # Reset counter if current notification day and previous notification day are different
    if (dayNow > dayLast) or (dayLast == 6 and dayNow == 0):
        counter = 1

    # Deploy notification
    notification.notify(title='Water Reminder: '+str(counter), message='Time to drink water...',
                        app_icon='water-icon.ico', timeout=20)

    # Update DataBase
    with open("waterDB.txt", "a") as f:
        f.write(f"Reminder No: {str(counter)} - {timeStamp.split(' ')[0]} @ {timeNow}\n")
        f.close()

    # Increment counter
    counter += 1

    # Set previous Notification day
    dayLast = dayNow

    # Wait for one hour until next notification deploy
    time.sleep(3600)
