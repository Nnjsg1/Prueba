#Crear matriz

matriz = []
contador = 1
for i in range(8):
    fila = []
    for j in range(8):

        asiento={'Numero':contador,'Estado':'Disponible'}
        fila.append(asiento)
        contador += 1
    matriz.append(fila)

# Mostrar la matriz
for fila in matriz:
    for ditto in fila:
        if ditto['Numero']==6:
            ditto['Estado']='Ocupado'
            ditto['Datos']='Nash'

for ditto3 in matriz:
    print(ditto3)

for fila in matriz:
    for ditto in fila:
        if ditto['Numero']==6:
            ditto['Estado']='Disponible'
            del ditto['Datos']
for mamase in matriz:
    print(mamase)