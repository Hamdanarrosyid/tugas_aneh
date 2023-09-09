x = input().split(' ')
y = int(input())

if y > len(x):
    print('Maaf negara terlalu kuat')
elif len(x) == y:
    print('Semua sudah terjajah')
else:
    x.sort()
    x.reverse()
    print(x[y])