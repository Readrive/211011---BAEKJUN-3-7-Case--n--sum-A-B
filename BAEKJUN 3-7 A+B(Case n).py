t = int(input("몇 번 하시겠습니까?"))

i = 0
for i in range(1, t + 1):
    a, b = map(int, input("원하는 숫자를 입력해주세요.").split())
    c = a + b
    print("Case #{0}: {1}".format(i, c))
