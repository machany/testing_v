#
# Official Solution
# Author: Jongseo Lee (@leejseo)
#
n = int(input())
A = list(map(int, input().split()))
S = [0] * 2
ans = [0, 0]
for i in range(1, n+1):
    x = A[i-1] % 2
    S[x] += 1
    ans[x] += S[1-x]
print(min(ans))