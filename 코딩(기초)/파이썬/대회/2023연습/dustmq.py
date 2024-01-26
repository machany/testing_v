N = int(input()) # 정수
S = input().split() # 받은 숫자값 (뛰어 쓰지 있이)
for i in range(0, N): # S내용을 숫자로 바꾸는 과정
    S2 = S
    S[i] = int(S2[i])
S2 = [0, 0]
dap = [0, 0]

for i in range(1, N + 1):
    x = S[i - 1] % 2
    S2[x] += 1
    dap[x] += S2[1 - x]

print(min(dap))