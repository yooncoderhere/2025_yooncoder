import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
cards = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
targets = list(map(int,sys.stdin.readline().split()))

# target 숫자 카드를 몇 개 가지고 있는지

card_count = Counter(cards)
#print(card_count)

result = [str(card_count[target]) for target in targets] 

print(" ".join(result))