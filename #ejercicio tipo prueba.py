#ejercicio tipo prueba
import os
import msvcrt
import subprocess   #Esto es porque abro el archivo de texto, no es obligatorio
#from openpyxl import Workbook

cleanse=lambda: os.system('cls')
empleados=[]

def menu():
    
    while True:
        try:
            cleanse()
            print('''1. Registrar trabajador

2. Listar los todos los trabajadores

3. Imprimir planilla de sueldos

4. Salir del Programa
                  ''')
            x=int(input('Opcion: '))
            if x in [1,2,3,4,5]:
                return x
        except ValueError:
            print('Opcion no valida')
            pass
def registrar():  #aqui registro al usuario en la lista
    cleanse()
    nobre=input('Nombre: ').lower()
    while not nobre:
        print('El nombre no puede estar vacio.')
        nobre=input('Nombre:').lower()
    apellido=input('Apellido: ').lower()
    while not apellido:
        print('El apellido no puede estar vacio')
        apellido=input('Apellido: ').lower()
    cargo=input('Cargo: ').lower()
    while cargo not in ['ceo','desarrollador','analista de datos']:
        print('Cargo no valido')
        cargo=input('Cargo').lower()
    while True:
        try:
            sueldo=int(input('Sueldo Bruto: '))
            if sueldo>0:
                break
        except ValueError:
            pass

    nobre=nobre.capitalize()
    apellido=apellido.capitalize()
    cargo=cargo.capitalize()
    novato={'Nombre: ':nobre, 'Apellido: ':apellido,'Cargo: ':cargo,'Sueldo bruto: ':sueldo}
    empleados.append(novato)
def escribir(busqueda): #aqui ingreso los datos a un txt
    with open('lista_empleados.txt', 'w') as plantilla:
        plantilla.write("Lista de empleados:\n")
        for empleado in empleados:
            if empleado['Cargo: '] == busqueda:
                detalle_empleado = "Nombre: {} {} Cargo: {} Sueldo Bruto: {} Desc. Salud: {} Desc. AFP: {} Liquido: {}\n".format(empleado['Nombre: '], empleado['Apellido: '], empleado['Cargo: '], empleado['Sueldo bruto: '],int(empleado['Sueldo bruto: ']*0.07),int(empleado['Sueldo bruto: ']*0.12),int(empleado['Sueldo bruto: ']*0.81))
                plantilla.write(detalle_empleado)
def abrir():  #aqui abro el txt, completamente opcional e innecesario



    nombre_archivo = "lista_empleados.txt"


    try:
        subprocess.run(['xdg-open', nombre_archivo]) 
    except:
        try:
            subprocess.run(['open', nombre_archivo])  
        except:
            try:
                subprocess.run(['start', nombre_archivo], shell=True)  # Para Windows
            except:
                print("No se pudo abrir el archivo.")
'''
def escribire():
    wb = Workbook()
    ws = wb.active
    ws.title = "Empleados"
    
    # Escribir los encabezados
    ws.append(['Nombre', 'Apellido', 'Cargo', 'Sueldo Bruto'])
    
    # Escribir los datos de los empleados
    for empleado in empleados:
        ws.append([
            empleado['Nombre: '],
            empleado['Apellido: '],
            empleado['Cargo: '],
            empleado['Sueldo bruto: ']
        ])
    
    # Guardar el archivo Excel
    wb.save('lista_empleados.xlsx')
def abrire():
    nombre_archivo = "lista_empleados.xlsx"
    try:
        if os.name == 'nt':
            os.startfile(nombre_archivo)
        elif os.name == 'posix':
            subprocess.run(['xdg-open', nombre_archivo])
        else:
            subprocess.run(['open', nombre_archivo])
    except Exception as e:
        print(f"No se pudo abrir el archivo. Error: {e}")
'''
def menu_principal():
    while True:
        desiscion=menu()
        if desiscion==1:
            registrar()
        elif desiscion==2:
            cleanse()
            print("Lista de empleados:")
            for empleado in empleados:
                print("Nombre:", empleado['Nombre: '],end=' ')
                print( empleado['Apellido: '],end=' ')
                print( empleado['Cargo: '],end=' ')
                print( empleado['Sueldo bruto: '],end=' ')
                print(int( empleado['Sueldo bruto: ']*0.07),end=" ")
                print( int(empleado['Sueldo bruto: ']*0.12),end=" ")
                print( int(empleado['Sueldo bruto: ']*0.81),end=" ")
                print()
            msvcrt.getch()
        elif desiscion==4:
            break
        elif desiscion==3:
            cargobuscar=input('Cargo: ').lower()
            while cargobuscar not in ['ceo','desarrollador','analista de datos']:
                print('Cargo no valido')
                cargobuscar=input('Cargo').lower()
            cargobuscar=cargobuscar.capitalize()
            escribir(cargobuscar)
            abrir()
        '''elif desiscion==5:
            escribire()
            abrire()
'''
menu_principal()


