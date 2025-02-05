import sys

S = sys.stdin.readline().strip()
count = [0] * 26 # 알파벳의 개수

for char in S:
    count[ord(char)-ord('a')] += 1
    
print(" ".join(map(str,count)))
