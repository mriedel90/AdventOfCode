def readFileAsLines(filePath):
    lines = []
    with open(filePath) as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines
