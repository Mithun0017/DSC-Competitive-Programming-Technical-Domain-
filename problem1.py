# Competive Programming
# Problem 1
'''
Name : Mithun. T
Programme : B.Tech(CSE)
Section : 'D'
Year : 1st year
Register No. : RA2411003020254
'''

def sort_string(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=len)
    sorted_string = ' '.join(sorted_words)
    return sorted_string

input_string = input("Enter a sentence : ")
print(sort_string(input_string))
