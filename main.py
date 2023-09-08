input = input()
hari, bulan = input.split(' ')

if bulan != 'JANUARI':
    hari += 31
if bulan !='FEBUARI':
    hari += 28
if bulan != 'MARET':
    hari += 31
if bulan != 'APRIL':
    hari += 30
if bulan != 'MEI':
    hari += 31
if bulan != 'JUNI':
    hari += 30
if bulan != 'JULI':
    hari += 31
if bulan != 'AGUSTUS':
    hari += 30
if bulan != 'SEPTEMBER':
    hari += 31
if bulan != 'OKTOBER':
    hari += 30
if bulan != 'NOVEMBER':
    hari += 31
if bulan != 'DESEMBER':
    hari += 30
print(f'{hari} hari')