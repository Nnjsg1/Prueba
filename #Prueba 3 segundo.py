#Segundo intento
import os
import random
import csv
import time
import msvcrt
import math
import json
cleanse=lambda: os.system('cls')
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
empleados=[]
def menu():
    while True:
        try:
            cleanse()
            print('''----------Menu----------
1.-Asignar sueldos aleatorios
2.-Clasificar sueldos
3.-Reporte de sueldos
4.-Estadisticas
5.-Salir del programa
''')
            miku=int(input('Opcion: '))
            if miku in [1,2,4,5]:
                return miku
            if miku==3:
                cleanse()
                print('Opciones de reporte\n1.-Csv\n2.-Json')
                miku=int(input('Opcion: '))
                if miku==1:
                    reporte()
                    print('Csv creado')
                    msvcrt.getch()
                elif miku==2:
                    viernes13()
                    print('Json creado')
                    msvcrt.getch()
                else:
                    print('Opcion no valida')
        except ValueError:
            print('Error')
            time.sleep(1)
def asignar():
    global empleados
    empleados=[]
    for ditto in trabajadores:
        noob={}
        sueldo=random.randint(300000,2500000)
        noob={'Nombre':ditto,'Sueldo':sueldo,'Desc.Salud':int(sueldo*0.07),'Desc.Afp':int(sueldo*0.12),'Desc.Liquid':int(sueldo*0.81)}
        empleados.append(noob)
def clasificar():
    total=0
    menor=[i for i in empleados if i['Sueldo']<=800000]
    mitad=[i for i in empleados if i['Sueldo']>800000 and i['Sueldo']<=2000000]
    mayor=[i for i in empleados if i['Sueldo']>2000000]
    print(f'Sueldos menores a $800.000 TOTAL: {len(menor)}')
    print('Nombre\t\tSueldo')
    for ditto in menor:
        print(f'{ditto['Nombre']}\t${ditto['Sueldo']:,}')
    print(f'Sueldos entre $800.000 y $2.000.000 Total:{len(mitad)}')
    print('Nombre\t\tSueldo')
    for ditto in mitad:
        print(f'{ditto['Nombre']}\t${ditto['Sueldo']:,}')
    print(f'Sueldos superiores a $2.000.000 TOTAL{len(mayor)}')
    print('Nombre\t\tSueldo')
    for ditto in mayor:
        print(f'{ditto['Nombre']}\t${ditto['Sueldo']:,}')
    for ditto in empleados:
        total+=ditto['Sueldo']
    print(f'TOTAL SUELDOS: ${total:,}')
def reporte():
    with open('Reporte.csv','w',newline='') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        for ditto in empleados:
            escritor.writerow([ditto['Nombre'],ditto['Sueldo'],ditto['Desc.Salud'],ditto['Desc.Afp'],ditto['Desc.Liquid']])
def viernes13():
        with open('empleados.json', 'w') as algo:
            json.dump(empleados, algo, indent=2)
def ivs():
    if not empleados:
        asignar()
    larga=max(empleados,key=lambda x: x['Sueldo'])
    corta=min(empleados,key=lambda x: x['Sueldo'])
    print(f'El que gana mas es {larga['Nombre']} con un sueldo de ${larga['Sueldo']:,}')
    print(f'El que gana menos es {corta['Nombre']} con un sueldo de ${corta['Sueldo']:,}')
    total2=sum(ditto['Sueldo'] for ditto in empleados)
    total2=int(total2/10)
    print(f'El promedio de sueldos es de ${total2:,}')
    total2=math.prod(ditto['Sueldo'] for ditto in empleados)
    total2=math.pow(total2,1/10)
    print(f'La media geometrica de los sueldos es ${int(total2):,}')
while True:
    nope=menu()
    if nope==1:
        asignar()
        print('Sueldos asignados!')
        msvcrt.getch()
    elif nope==2:
        cleanse()
        clasificar()
        msvcrt.getch()
    elif nope==4:
        cleanse()
        ivs()
        msvcrt.getch()
    else:
        cleanse()
        print("Finalizando programa")
        time.sleep(0.3)
        cleanse()
        print("Finalizando programa..")
        time.sleep(0.3)
        cleanse()
        print("Finalizando programa....")
        time.sleep(0.3)
        print('Desarrollador por Nash')
        print('RUT 00.000.000-1')
        time.sleep(1)
        break