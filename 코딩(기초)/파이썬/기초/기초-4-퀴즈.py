링크 = "https://naver.com"
# 링크 = "https://google.com"
# 링크 = "https://daum.com"
앞제거 = 링크.replace("https://", "")
com제거 = 앞제거.index(".")
기본 = 앞제거[:com제거]
글자수 = (len(기본))
글자내e수 = (기본.count("e"))
기본 = 기본[:3]
print(기본 + str(글자수) + str(글자내e수) + "!")