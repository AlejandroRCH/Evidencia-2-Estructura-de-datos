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
        ventas = {"Nombre":(lista_nombre), "Cantidad de productos":(lista_cantidad), "Precio":(lista_precios), "Fecha de venta":(lista_fecha)}
        ventas_dt = pd.DataFrame(ventas)
        print(ventas_dt)

    
    
    
    
    
    
    
    
    
    if eleccion == 2:
        pass
    
    
    
    
    
    
    
    if eleccion == 3:
        
        contador = 2