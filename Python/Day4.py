from helperMethods import readFile

def findGuardTimesMinute(inputs):
    inputs.sort()
    guards = dict()
    currentGuard = ''
    guardAsleepTime = -1
    guardAwakeTime = -1
    for input in inputs:
        if input.__contains__('begins shift'):
            currentGuard = int(input.split('Guard #')[1].split(' ')[0])
            if currentGuard not in guards:
                guards[currentGuard] = []
        if input.__contains__('falls asleep'):
            guardAsleepTime = int(input.split(':')[1].split(']')[0])
        if input.__contains__('wakes up'):
            guardAwakeTime = int(input.split(':')[1].split(']')[0])
        if guardAsleepTime >= 0 and guardAwakeTime >= 0:
            for minute in range(guardAsleepTime, guardAwakeTime):
                guards[currentGuard].append(minute)
            guardAsleepTime = -1
            guardAwakeTime = -1
    
    guardWithMaxLength = currentGuard
    for guard in guards:
        if len(guards[guard]) > len(guards[guardWithMaxLength]):
            guardWithMaxLength = guard

    minutes = guards[guardWithMaxLength]
    mostCommonMinute = max(set(minutes), key=minutes.count)

    return guardWithMaxLength * mostCommonMinute

inputs = readFile("Day4Sample.txt")
output = findGuardTimesMinute(inputs)
print(output) #240

inputs = readFile("Day4.txt")
output = findGuardTimesMinute(inputs)
print(output)