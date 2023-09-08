x = input().split(' ')
y = int(input())

if y > len(x):
    print('Maaf negara terlalu kuat')
else:
    x.sort()
    x.reverse()
    print(x[y])