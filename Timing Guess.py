import random
from datetime import datetime
targetTime = random.randrange(2000, 4000)/1000
input(f"Your goal is to press enter as close as possible to {targetTime} seconds. Press enter to start timer.")
startTime = datetime.now()
input()
elapsedTime = (datetime.now() - startTime).total_seconds()
print(f"Your time is: {elapsedTime}")
if elapsedTime > targetTime:
    print(f"You waited {round(elapsedTime - targetTime, 3)} seconds too long!")
elif elapsedTime < targetTime:
    print(f"You waited {round(targetTime - elapsedTime, 3)} seconds too short!")
else:
    print("Wow you were right on the money! Congrats!")
