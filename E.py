from itertools import combinations
def maxpre(arr1, arr2):
    min_len = min(len(arr1), len(arr2))
    similarity = 0

    for i in range(min_len):
        if arr1[i] == arr2[i]:
            similarity += 1
        else:
            break

    return similarity

n = int(input())
A = [0] * n
for i in range(n):
  k = int(input())
  A[i] = list(map(int,input().split()))
  
combs = combinations(A, 2)
count = 0
for i in combs:
  first, second = i
  count += maxpre(first, second,)
print(count)