def slice_simple():
    texto = "Awesome"

    primeras_tres = texto[:3]
    mitad = texto[len(texto)//2 - 1: len(texto)//2 + 2]
    parte_1 = texto[:4]
    parte_2 = texto[-3:]

    print(primeras_tres)
    print(mitad)
    print(parte_1 + parte_2)

slice_simple()
