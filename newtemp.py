string = input()
dic = {}

for letter in string:
    dic[letter] = dic.get(letter, 0) + 1

counter = 0
while len(dic) > 2:
    minim = sorted(dic.items(), key=lambda x:x[1])[0]
    del dic[minim[0]]
    counter+=minim[1]
print(counter)



'''For a string of letters, define the Simplicity of the string to be the number 
of distinct letters in the string. For example, the string string has simplicity 6
, and the string letter has simplicity 4
.

You like strings which have simplicity either 1
 or 2
. Your friend has given you a string and you want to turn it into a string that you like. 
You have a magic eraser which will delete one letter from any string. 
Compute the minimum number of letters you must erase in order to turn the string into 
a string with simplicity at most 
.

Input
Each input will consist of a single test case. Note that your program may be run multiple 
times on different inputs. The input will consist of a line with a single string consisting of at least 
 and at most 
 lowercase letters ‘a’-‘z’.

Output
Output a single integer, indicating the minimum number letters you need to erase 
in order to give the string a simplicity of 
 or 
.'''