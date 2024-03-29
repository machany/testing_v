"""
반복문

전에도 어려웠지만
이젠 더 어려워지는 구간!

우선 반복문은 말그 그대로
반복하는 형태입니다.

팔 벌려 뛰기할때
팔벌려뛰기 하나!
팔벌려뛰기 둘!
이런 식으로 세지 않는듯

팔벌려뛰기 하나!
둘!
셋!
이런식으로 반복해서 세듯

마찬가지로
컴퓨터에게도 반복을 시킬수 있습니다.

for 변수 in range(5):
    print(변수)

와

print(0)
print(1)
print(2)
print(3)
print(4)

는 동일합니다.

range(5)는 5보다 작으면 해~
라는 의미로
5랑 같아지면 멈추게 됩니다.

그러나 팔벌려 뛰기를 할때
0부터 안 세죠?
1부터 세게 하려면

for 변수 in range(1, 5):
    print(변수)

를 하면 (1, 5)

맨 앞에 있는 1는 1부터 세도록해 라는 의미입니다.
만약 2개씩 세게 하고싶으면

for 변수 in range(1, 5, 2):
    print(변수)
뒤에 2를 붙이면 됩니다.

for 변수 in range():
는 1번 끝낼때 마다 "변수"에 1씩 더하고

for 변수 in range(1, 5, 2):
    print(변수)
은 변수에 2씩 더합니다.





먼저 쉬고나서 ******************이어서
while 은 if와 비슷합니다.
대신에 if와 다르게 같으면 반복입니다.

용돈 = 1000
while 용돈 <= 100000:
    print("용돈 올려주세요")
    용돈 += 1000
print("안된다.")

같으면 실행, 다르면 반복 끝! 정말 간단하죠?
"""