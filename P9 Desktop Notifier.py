# Project 9 : Desktop Notifier

from plyer import notification
import time

if __name__ == '__main__':
        while True:
            notification.notify(
                title = "*** Take Rest ***",
                message = "Rest is for better mental health, increased concentration, reduced stress",
                timeout=5)
            time.sleep(20)

#to run in background write pythonw filename.py
#terminate taskmanager>python file>task end