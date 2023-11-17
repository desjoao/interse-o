a = [0]*10
b = [0]*10
qnt = 0

for i in range(10):
    a[i] = int(input(f'Informe o {i+1}º número inteiro para o vetor A: '))
    b[i] = int(input(f'Informe o {i+1}º número inteiro para o vetor B: '))
    if a[i] == b[i]:
        qnt += 1
c = [0]*qnt

for i in range(10):
    if a[i] == b[i]:
        for count in range(qnt):
            if c[count] == 0:
                c[count] = a[i]
                break

print(f'A interseção dos vetores A e B forma o seguinte vetor: {c}.')
