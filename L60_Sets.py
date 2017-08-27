string = 'this is a string'

vowels = {'a', 'e', 'i', 'o', 'u'}
newStr = set(string).difference(vowels)

sortedStr = sorted(newStr)
print(sortedStr)
