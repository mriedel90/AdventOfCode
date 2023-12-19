import os
from datetime import datetime

def readFileAsLines(filePath):
    lines = []
    with open(filePath) as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines

def is_even(number):
    return number % 2 == 0

def log(log):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + log)

def get_day(currentFileRef):
    day = os.path.splitext(os.path.basename(currentFileRef))[0]
    log(day)
    return day