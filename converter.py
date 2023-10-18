while True:
    temp = float(input("Digite a temperatura: "))

    pergunta = int(input("Vc quer converter para celsius para Fahrenheit, ou Fahrenheit para celsius: 1/2  "))
    if pergunta == 1:
        print("{}°C".format((temp * 9/5) + 32))
    else:
        if pergunta == 2:
            print("{:.2f}°F".format((temp - 32) * 5/9))
        elif pergunta != 1 or pergunta != 2:
            print("Não existe essa função '-' ")
            break
