from random import *
참여자 = range(1, 21)
참여자 = list(참여자)
shuffle(참여자)
shuffle(참여자)
당첨 = sample(참여자, 4)
print("\\!!축하합니다!!\\\n치킨 당첨자는 [" + str(당첨[0]) + "]입니다.\n커피 당첨자는 " + str(당첨[1:]) + "입니다.\n\\!!축하합니다!!\\")