from helpers import *
import math


def ParseRaces(lines):
    races = []
    times = lines[0][len('Time:'):].strip().split()
    distances = lines[1][len('Distance:'):].strip().split()
    for i in range(len(times)):
        races.append((int(times[i]), int(distances[i])))
    return races


def ParseRacesV2(lines):
    time = lines[0][len('Time:'):].replace(' ', '')
    distance = lines[1][len('Distance:'):].replace(' ', '')
    return [(int(time), int(distance))]


def ProductOfNumberOfWinningStrategies(races):
    result = 1
    for (time, distance) in races:
        speed1 = (time + math.sqrt((time*time) - (4*distance))) / 2
        speed2 = (time - math.sqrt((time*time) - (4*distance))) / 2
        winSpeed1 = speed1 - 1 if speed1.is_integer() else math.floor(speed1)
        winSpeed2 = speed2 + 1 if speed2.is_integer() else math.ceil(speed2)
        numStrategiesToWin = winSpeed1 - winSpeed2 + 1
        result *= numStrategiesToWin
    return result

# given:
# distance = runtime * speed
# runtime = totaltime - speed
# have distance and totaltime, need to find speed

# find speed:
#distance = (totaltime - speed)*speed
#distance = totaltime * speed - speed^2
#speed^2 - totaltime * speed + distance = 0
# quadratic equation:
#speed = totaltime +- sqrt(t^2 -4*distance) / 2
        
#ex 1: totaltime = 7, distance = 9
#speed = 7 +- sqrt(7^2 - 4*9) / 2
#speed = 7 +- sqrt(49 - 36) / 2
#speed = (7 +- sqrt(13)) / 2
#speed = (7 +- 3.605) / 2
#speed1 = 5.302
#speed2 = 1.697
#range = 5 to 2
#range = 
#num options = math.floor(speed1) - math.ceil(speed2) + 1
# - if the times are round ints, dont need round, and need to shorten the range by 1

#speed = distance/runtime
#speed = distance/(totaltime - speed)
        

#flaws: what if you cant win? the speed would be negative? not compute?

def Part1(file):
    lines = readFileAsLines(file)
    races = ParseRaces(lines)
    result = ProductOfNumberOfWinningStrategies(races)
    return result


def Part2(file):
    lines = readFileAsLines(file)
    races = ParseRacesV2(lines)
    result = ProductOfNumberOfWinningStrategies(races)
    return result





####################

day = get_day(__file__)

# Part 1 Sample Answer: 288
part1SampleResult = Part1(day + '/sample.txt')
log('Part 1 Sample: ' + str(part1SampleResult))
part1Result = Part1(day + '/input.txt')
log('Part 1: ' + str(part1Result))


# Part 2 Sample Answer: 71503
part2SampleResult = Part2(day + '/sample.txt')
log('Part 2 Sample: ' + str(part2SampleResult))
part2Result = Part2(day + '/input.txt')
log('Part 2: ' + str(part2Result))

# Output:

# 2023-12-19 21:24:34: day6
# 2023-12-19 21:24:34: Part 1 Sample: 288.0
# 2023-12-19 21:24:34: Part 1: 771628
# 2023-12-19 21:24:34: Part 2 Sample: 71503
# 2023-12-19 21:24:34: Part 2: 27363861