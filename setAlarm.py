import time
import datetime
import winsound


def setAlarm(timeToSleep, filePath, message):
    while(timeToSleep > time.time()):
        pass
    print(message)
    winsound.PlaySound(filePath, winsound.SND_FILENAME)


filePath = ""
setAlarm(time.time() + 5, filePath,"Time's Up!")
