n, m, q = map(int,input().split())
words = input().split()
table = [list(map(int,input().split())) for i in range(n)]

columns = {} 
for i, word in enumerate(words):
    columns[word] = [i, -float('infinity'), float('infinity')]

while q:
    stmnt = input().split()
    if stmnt[1] == '>':
        columns[stmnt[0]][1] = max(columns[stmnt[0]][1], int(stmnt[2]))
    else:
        columns[stmnt[0]][2] = min(columns[stmnt[0]][2], int(stmnt[2]))
    q -= 1
ans = set(range(n))
for i in columns:
    col_num = columns[i][0]
    for j in range(n):
        if not(table[j][col_num] > columns[i][1] \
                and table[j][col_num] < columns[i][2]) \
                and j in ans:
           ans.remove(j)
res = 0
for i in ans:
    res += sum(table[i])
print(res)