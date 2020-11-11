contador = 1
import pandas as pd
import datetime
lista_fecha = []
lista_nombre = []
lista_cantidad = []
lista_precios = []
precios_totales = []


while contador ==1:
    
    eleccion = int(input("Que accion deseas realizar?\n 1.Registrar una venta\n 2.Consultar ventas de un dia en especifico\n 3.Salir\n"))
    
    if eleccion == 1:
        cant = int(input("Cuantas ventas quieres registrar?"))
        for i in range(cant):
            nombre_prd = input("Nombre de producto\n")
            lista_nombre.append(nombre_prd)
            cantidad_prd = int(input("Dime la cantidad de productos vendidos\n"))
            lista_cantidad.append(cantidad_prd)
            precio_prd = float(input("Dime el precio del producto\n"))
            lista_precios.append(precio_prd)
            fecha_v = datetime.date.today()
            lista_fecha.append(fecha_v)
            precios_totales.append((cantidad_prd) * (precio_prd))
            total_venta = sum(precios_totales)
        ventas = {"Nombre":(lista_nombre), "Cantidad de productos":(lista_cantidad), "Precio":(lista_precios), "Fecha":(lista_fecha)}
        ventas_dt = pd.DataFrame(ventas)
        print(ventas_dt)
        print(f"El total a pagar es el siguiente: {total_venta}")
        ventas_dt.to_csv (r"AlmacenVentas.csv",index=False, header=True)
        print("exportado correctamente")

    
    
    
    
    
    
    
    
    
    if eleccion == 2:

        almacen = pd.read_csv("AlmacenVentas.csv", index_col=0)
        consulta = input("¿Cuál es la fecha de venta que quieres consultar? Escribe la fecha con el siguiente formato: yyyy-mm-dd: ")
        subconjunto = almacen[almacen.Fecha == consulta]
        print(subconjunto)
        print("Si no aparece nada quiere decir que no hay ventas en esa fecha sigue intentando con otra fecha")
        

    
    
    
    
    
    
    
    if eleccion == 3:

        print("Vuelva pronto :D")
        contador = 2