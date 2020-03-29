def soma(s):
    while True:
        lido = int(input('lido: '))
        if lido==0: break
        s = s + lido
    print (s)


if __name__ ==  '__main__':
    s = 0
    soma(s)
