import re
with open('day04/input.txt') as input:
    lines = input.read().splitlines()

valid=0
for line in lines:
    words=line.split(' ')
    if len(words)==len(set(words)): valid+=1

answer1 = valid

def wordToSig(word):
    sig=''
    for i in range(26):
        cnt=int(word.count(chr(ord('a')+i)))
        sig+=f'{cnt}'
    return sig


valid=0
for line in lines:
    words=[wordToSig(i) for i in line.split(' ')]
    if len(words)==len(set(words)): valid+=1
answer2 = valid

print(answer1,answer2)