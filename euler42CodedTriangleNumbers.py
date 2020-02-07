'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''


def TriangleNumbers(n):
    # generating a list of triangle numbers till nth observation
    final_list = []
    for i in range(1, n+1):
        final_list.append(int(0.5*i*(i+1)))
    return final_list

def ReadingFile(filename):
    f = open(filename,'r')    
    for line in f:
        line = line.replace('"',"")
        fields = line.split(",")
    return fields

def CodedTriangleNumbers(filename):
    my_list = ReadingFile(filename)
    max_length = len(max(my_list, key=len))
    triangle_list = TriangleNumbers(max_length*26)
    count = 0
    for eachWord in my_list:
        sum = 0
        for eachLetter in eachWord:
            sum += ord(eachLetter) - 64
        if sum in triangle_list:
            count += 1
    return count

final = CodedTriangleNumbers('p042_words.txt')
print(final)