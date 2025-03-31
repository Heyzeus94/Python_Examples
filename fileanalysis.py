

def loadFile(fileName):
    text = open(fileName, 'r').read().split()
    return set(text)

fileA = 'first_file.txt'
fileB = 'second_file.txt'

setA = loadFile(fileA)
setB = loadFile(fileB)

print(f'Unique Words in {fileA}:')
print(setA)

print(f'Unique Words in {fileB}:')
print(setB)

print()

print(f'Words That Appear In Both {fileA} & {fileB}:')
print(setA.intersection(setB))

print()

print(f'Words That Appear In {fileA} But Not {fileB}:')
print(setA.difference(setB))

print()

print(f'Words That Appear In {fileB} But Not {fileA}')
print(setB.difference(setA))

print()

print(f'Words That Appear In Either {fileA} Or {fileB} But Not Both:')
print(setA.symmetric_difference(setB))
