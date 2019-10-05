import random
import string

keepPunc = False
keepNums = False
keepCase = False

contents = []
print("Enter some sample text (press enter then Ctrl-D to exit): ", end="")
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

print("")
inputString = ""

for i in range(0,len(contents)):
    inputString = inputString + contents[i]
punctuationTranslationMap = str.maketrans('', '', string.punctuation)
numMap = str.maketrans('','',"0123456789")
if keepPunc == False:
    inputString = inputString.translate(punctuationTranslationMap)

if keepNums == False:
    inputString = inputString.translate(numMap)
inputString = inputString.replace("  "," ")
inputString = inputString.replace("   "," ")

if keepCase == False:
    inputArr = inputString.lower().split(" ")
else:
    inputArr = inputString.split(" ")
   
words = []
followerWords = []
followerWordNum = []

for i in range(0,len(inputArr)-1):
    words.append(inputArr[i])
    followerWords.append(inputArr[i+1])
    followerWordNum.append(0)

for i in range(0,len(words)):
    for j in range(0,len(words)):
        if words[j] == words[i] and followerWords[j] == followerWords[i]:
            followerWordNum[i] += 1

repeat = [False]*len(words)

for i in range(0,len(words)):
    if repeat[i] == False:
        for j in range(0,len(words)):
            if j != i and words[j] == words[i] and followerWords[j] == followerWords[i] and followerWordNum[j] == followerWordNum[i]:
                repeat[j] = True
                
while True in repeat:
    index = repeat.index(True)
    words.pop(index)
    followerWords.pop(index)
    followerWordNum.pop(index)
    repeat.pop(index)
    
sentenceLen = int(input("Enter how many words you want in the sentence: "))
sentence = [words[random.randint(0,len(words))]]
usedIndices = []

for i in range(1,sentenceLen):
    currMax = 0
    currMaxIndex = 0
    for j in range(0,len(words)):
        if words[j] == sentence[i-1] and followerWordNum[j] > currMax and j not in usedIndices:
            currMaxIndex = j
            currMax = followerWordNum[j]
    
    if sentence[len(sentence)-1] == followerWords[currMaxIndex]:
        break
    
    sentence.append(followerWords[currMaxIndex])
    usedIndices.append(currMaxIndex)

for i in range(0, len(sentence)):
    print(sentence[i],end = " ")
