def rango_peticion(string_rango):
    lista_rango = []

    for lista_elemento in string_rango:
        lista_rango.append(lista_elemento)
    
    for i in range(len(lista_rango)):

        if lista_rango[i] == ' ':
            lista_rango_1 = lista_rango[0: i]
            lista_rango_2 = lista_rango[i+1 : len(lista_rango)]

    valor1 = lista_rango_1[0]
    valor2 = lista_rango_2[0]

    for rango in range(1, len(lista_rango_1)):
        valor1 += lista_rango_1[rango]

    for rango in range(1, len(lista_rango_2)):
        valor2 += lista_rango_2[rango]

    rango = [int(valor1), int(valor2)]
    rango.sort()

    return rango

def homogeneidad(string):
    string_lista = []
    for i in string:
        string_lista.append(i)
    check = True
    for j in range(len(string_lista)):
        if string_lista[j-1] != string_lista[j]:
            check = False
    return check

def print_res(check):
    if check == True:
        print('Yes')
    else:
        print('No')


string_binario = input()
peticiones = input()
ans = []

for peticion in range(int(peticiones)):
    peticion = input()
    
    string_peticion = string_binario[rango_peticion(peticion)[0] : rango_peticion(peticion)[1]+1]
    ans.append(homogeneidad(string_peticion))
print('Case :')
for i in ans:
    print_res(i)

    
    





