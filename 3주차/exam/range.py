a = list(range(1, 5))
print(a)

n = int(input('n의 값을 입력해주세요: '))
m = int(input('m의 값을 입력해주세요: '))
b = list(range(n, m))
print('b: ' + str(b))
b.remove(n)
b.remove(m - 1)
print('b: ' + str(b))
