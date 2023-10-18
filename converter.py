import codigo
while True:
    temp = float(input("Digite a temperatura: "))

    pergunta = int(input("Vc quer converter para celsius para Fahrenheit, ou Fahrenheit para celsius: 1/2  "))
    if pergunta == 1:
        print("{}°C".format(codigo.c(temp)))
    else:
        if pergunta == 2:
            print("{}°F".format(codigo.f(temp)))
        elif pergunta != 1 or pergunta != 2:
            print("Não existe essa função ('_') ")
            break
