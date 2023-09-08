A = input().split(' ')
B = input().split(' ')
C = input().split(' ')
D = input().split(' ')
E = input().split(' ')

mahasiswa = [A,B,C,D,E]

mahasiswa.sort(key=lambda x: (int(x[2]), int(x[1])))

terpilih = mahasiswa[len(mahasiswa) // 2][0]
print(terpilih)
