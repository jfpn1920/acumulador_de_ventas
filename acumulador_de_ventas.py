ids = []
vendedores = []
productos = []
fechas = []
cantidades = []
precios = []
totales = []
metodos_pago = []
observaciones = []
#-----------------------------------------#
#--|menu_principal_acumulador_de_ventas|--#
#-----------------------------------------#
while True:
    print("menu principal acumulador de ventas")
    print("1) crear ventas")
    print("2) editar ventas")
    print("3) eliminar ventas")
    print("4) buscar ventas")
    print("5) lista de ventas")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_venta|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_venta = 1
        else:
            id_venta = ids[-1] + 1
        vendedor = input("nombre del vendedor: ")
        producto = input("nombre del producto: ")
        fecha = input("fecha de la venta: ")
        cantidad = int(input("cantidad vendida: "))
        precio = float(input("precio unitario: "))
        total = cantidad * precio
        metodo_pago = input("método de pago: ")
        observacion = input("observación: ")
        ids.append(id_venta)
        vendedores.append(vendedor)
        productos.append(producto)
        fechas.append(fecha)
        cantidades.append(cantidad)
        precios.append(precio)
        totales.append(total)
        metodos_pago.append(metodo_pago)
        observaciones.append(observacion)
        print("venta registrada correctamente.")
        print("id:", id_venta)
    #------------------#
    #--|editar_venta|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar venta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {vendedores[i]} | {productos[i]} | {fechas[i]} | {cantidades[i]} | {precios[i]} | {totales[i]} | {metodos_pago[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {vendedores[posicion]} | {productos[posicion]} | {fechas[posicion]} | {cantidades[posicion]} | {precios[posicion]} | {totales[posicion]} | {metodos_pago[posicion]} | {observaciones[posicion]}")
                vendedores[posicion] = input("nuevo vendedor: ")
                productos[posicion] = input("nuevo producto: ")
                fechas[posicion] = input("nueva fecha: ")
                cantidades[posicion] = int(input("nueva cantidad: "))
                precios[posicion] = float(input("nuevo precio unitario: "))
                totales[posicion] = cantidades[posicion] * precios[posicion]
                metodos_pago[posicion] = input("nuevo método de pago: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_venta|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar venta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {vendedores[i]} | {productos[i]} | {fechas[i]} | {cantidades[i]} | {precios[i]} | {totales[i]} | {metodos_pago[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {vendedores[posicion]} | {productos[posicion]} | {fechas[posicion]} | {cantidades[posicion]} | {precios[posicion]} | {totales[posicion]} | {metodos_pago[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    vendedores.pop(posicion)
                    productos.pop(posicion)
                    fechas.pop(posicion)
                    cantidades.pop(posicion)
                    precios.pop(posicion)
                    totales.pop(posicion)
                    metodos_pago.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_venta|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar venta")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {vendedores[posicion]} | {productos[posicion]} | {fechas[posicion]} | {cantidades[posicion]} | {precios[posicion]} | {totales[posicion]} | {metodos_pago[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = totales[0]
            menor = totales[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {vendedores[i]} | {productos[i]} | {fechas[i]} | {cantidades[i]} | {precios[i]} | {totales[i]} | {metodos_pago[i]} | {observaciones[i]}")
                suma += totales[i]
                if totales[i] > mayor:
                    mayor = totales[i]
                if totales[i] < menor:
                    menor = totales[i]
            promedio = suma / len(ids)
            print("estadísticas acumulador de ventas")
            print("cantidad de registros:", len(ids))
            print("ventas acumuladas: $", round(suma, 2))
            print("promedio de ventas: $", round(promedio, 2))
            print("venta mayor: $", round(mayor, 2))
            print("venta menor: $", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")