import os
from time import sleep
"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE : Alfredo Minchez
"""

dic_empresas = {
    '12345678910':{
        'razon_social':'TECSUP S.A.C.',
        'direccion' : 'CALLE PERU 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("Ingrese RUC: ")
        razon_social = input("Ingrese Razón Social: ")
        direccion = input("Ingrese Dirección: ")
        dic_nueva_empresa = {
            'razon_social': razon_social,
            'direccion': direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("Empresa registrada exitosamente")
        
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        
        for ruc, info in dic_empresas.items():
            print(f"RUC: {ruc}")
            print(f"Razón Social: {info['razon_social']}")
            print(f"Dirección: {info['direccion']}")
            print('*' * ANCHO)
            
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("Ingrese Código de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa Encontrada: {dic_empresas[ruc]['razon_social']}")
            nueva_razon = input(f"NUEVA RAZÓN SOCIAL({dic_empresas[ruc]['razon_social']}): ")
            nueva_direccion = input(f"NUEVA DIRECCIÓN({dic_empresas[ruc]['direccion']}): ")
            if nueva_razon:
                dic_empresas[ruc]['razon_social'] = nueva_razon
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_direccion
            print("EMPRESA ACTUALIZADA EXITOSAMENTE!!!")
        else:
            print('No se encontró la empresa para el código ingresado')
            
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("Ingrese Código de la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print('EMPRESA ELIMINADA EXITOSAMENTE')
        else:
            print('No se encontró la empresa para el código ingresado')
            
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")