# Funcionalidades principales: para alcanzar un resultado óptimo en esta prueba, deberás:
# 1. Añadir productos al inventario: permitir al usuario agregar productos con atributos como
# nombre, precio y cantidad disponibles.
# 2. Consultar productos en inventario: buscar un producto por su nombre y mostrar sus
# detalles (nombre, precio, cantidad).
# 3. Actualizar precios de productos: modificar el precio de un producto específico en el
# inventario.
# 4. Eliminar productos del inventario: permitir la eliminación de un producto que ya no está
# disponible.
# 5. Calcular el valor total del inventario: multiplicar el precio por la cantidad de cada producto
# y mostrar el total acumulado.
# Criterios de aceptación:
# • El programa debe permitir agregar al menos 5 productos iniciales.
# • Al consultar un producto, debe indicar si no existe en el inventario con un mensaje claro.
# • La actualización de precios debe validar que el nuevo precio sea un número positivo.
# • La eliminación de un producto debe confirmar su existencia antes de borrarlo.
# • El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos
# decimales.
# • El código debe estar estructurado en funciones para cada operación y debe incluir
# comentarios explicativos.
# • El código y los comentarios deben estar 100% sin excepción alguna en inglés.

inventory = {"Arroz":[1200, 5] }

#Valid entrie int
def validate_int(str = int):
    try:
        return int(str)
    except ValueError:
        return -1

#valid entrie str
def validate_string(string = str):
    if len(string) == 0:
        print("ERROR: enter a value")
        return False
    if not string.replace(" ", ""):
        print("Enter a validate value")
        return False
    return True

#Valid entrie float
def validate_float(str = float):
    try:
        return float(str)
    except ValueError:
        return -1

#valid inventory empy
def empty_inventory(inventory = dict):
    if len(inventory) == 0:
        print("ERROR: there are not products in the inventory")
        return True
    return False

#options of exit or again    
def opt_dict():
    while True:
        print("\n0. Return to main menu")
        print("1. Return to previous menu\n")
        opt = input("Enter an option (0-1): ")
        opt = validate_int(opt)
        if opt == 0 or opt == 1:
 
            return opt
#Option exit       
def opt_add_dict():
    while True:
        print("\n0. Return to main menu")
        opt = input("Enter an option (0): ")
        opt = validate_int(opt)
        if opt == 0 or opt == 1:
            return opt
        
#search the product into inventory
def product_inventory(name = str, inventory = dict):
    return inventory[name]

#add products to dict
def add_products():
    print("*****Add a products*****")
    cont = 1
    
    while True:
        while cont < 6:   
                name_product = input(f"\nEnter a product name: ").capitalize().strip()
                cont += 1
                if name_product in inventory:
                    cont -= 1
                
                if not validate_string(name_product):
                    print("Invalid value")
                    continue

                if name_product in inventory:
                    print("The product is in the inventory")
                    continue

                price_product = input("Enter a product price: ").strip()
                price_product = validate_float(price_product)
                if price_product < 0:
                    print("Invalid value")
                    continue
            
                amount_product = input("Enter a product amount: ").strip()
                amount_product = validate_float(amount_product)
                if amount_product < 0:
                    print("Invalid value")
                    continue
            
                inventory[name_product] = [price_product, amount_product]
                print(f"\n|{'name'.ljust(15)}|{'price'.ljust(15)}|{'amount'.ljust(15)}")
                print("="*40)
                for key, value in inventory.items():
                    price_product, amount_product = value
                    print(f"|{key.ljust(15)}|{str(price_product).ljust(15)}|{str(amount_product).ljust(15)}")

        opt = opt_add_dict()
        if opt == 0:
            print("Returning to main menu")
            return


#Delete Products into dict
def delete_product():
    print("\n*****Delete products*****")
    while True:
        print(f"\n**These are the products you can delete**\n")
        print(f"\n|{'name'.ljust(15)}|{'price'.ljust(15)}|{'amount'.ljust(15)}") 
        print("="*40)
        for key, value in inventory.items():
            price_product, amount_product = value
            print(f"|{key.ljust(15)}|{str(price_product).ljust(15)}|{str(amount_product).ljust(15)}")

        del_product = input("\nEnter a delete name: ").capitalize().strip()
        if not validate_string(del_product):
            print("INVALID VALUE")
            continue
        
        if del_product in inventory:
            inventory.pop(del_product)
            print(f"The {del_product} delete")
            print(f"\n|{'name'.ljust(15)}|{'price'.ljust(15)}|{'amount'.ljust(15)}") 
            for key, value in inventory.items():
                price_product, amount_product = value
                print(f"|{key.ljust(15)}|{str(price_product).ljust(15)}|{str(amount_product).ljust(15)}")
        else:
            print("PRODUCT NOT FOUND")
            continue

        opt = opt_dict()
        if opt == 0:
            print("Returning to main menu")
            return

#update products price into dict
def update_product():
    print("*****Update a product price*****")

    while True:
        print(f"\n**These are the products you can update**\n")
        print(f"{"name".ljust(15)}|{"price".ljust(15)}|{"amount".ljust(15)}")
        print("="*40)
        for key, value in inventory.items():
            price, amount = value
            print(f"{key.ljust(15)}|{str(price).ljust(15)}|{str(amount).ljust(15)}")
                

        edit = input("\nEnter a name product ").capitalize().strip()
        if not validate_string(edit):
            print("Invalid value")

        if edit in inventory:
            current_amount = inventory[edit][1]

            new_val = validate_float(input("Ingresa el nuevo valor a editar: ").strip())
            if new_val < 0:
                print("\nInvalid value\n")
                continue
            print("")
            inventory[edit] = (new_val, current_amount)

            print(f"{"name".ljust(15)}|{"price".ljust(15)}|{"amount".ljust(15)}")
            print("="*40)
            for key, value in inventory.items():
                price, new_val = value
                print(f"{key.ljust(15)}|{str(price).ljust(15)}|{str(new_val).ljust(15)}")                
        else:
            print("Enter a valid value")
            continue
        opt = opt_dict()
        if opt == 0:
            print("Returning to main menu")
            return

#Update products amount into dict
def update_amount_product():
    print("*****Update a product amount*****")
    print(f"\n**These are the products you can update**\n")
    print(f"{"name".ljust(15)}|{"price".ljust(15)}|{"amount".ljust(15)}")
    print("="*40)
    for key, value in inventory.items():
        price, amount = value
        print(f"{key.ljust(15)}|{str(price).ljust(15)}|{str(amount).ljust(15)}")
                
    while True:
        

        edit = input("\nEnter a name product ").capitalize().strip()
        if not validate_string(edit):
            print("Invalid value")

        if edit in inventory:
            price_amount = inventory[edit][0]

            new_val = validate_float(input("Ingresa el nuevo valor a editar: ").strip())
            if new_val < 0:
                print("\nInvalid value\n")
                continue
            print("")
            inventory[edit] = (new_val, price_amount)

            print(f"{"name".ljust(15)}|{"price".ljust(15)}|{"amount".ljust(15)}")
            print("="*40)
            for key, value in inventory.items():
                price, new_val = value
                print(f"{key.ljust(15)}|{str(new_val).ljust(15)}|{str(price).ljust(15)}")                
        else:
            print("Enter a valid value")
            
        opt = opt_dict()
        if opt == 0:
            print("Returning to main menu")
            return


#search products into dict
def view_product(inventory):
    if empty_inventory(inventory):
        return

    print("\n*****View products*****")
    while True:
        search_product = input("\nEnter product name: ").capitalize().strip()
        if not validate_string(search_product):
            print("Invalid value")
            continue
        if not search_product in inventory:
            print("Product is not inventory")
            continue
        price, amount = product_inventory(search_product, inventory)
        print(f"The product {search_product} has {amount} amount and a price of ${price:,.2f} pesos")
        
        opt = opt_dict()
        if opt == 0:
            print("Returning to main menu")
        return

#Calculate inventory total of products
def calculate_inventory():
    while True:
            print("You have chosen to calculate total inventory value\n")
            total_value = 0.0
            for key, value in inventory.items():
                price = value[0]
                quantity = value[1]
                total_value += price * quantity
                print(f"Product: {key} - Partial value: {price * quantity}")
            print(f"\nTotal inventory value: {total_value}")  

            opt = opt_dict()
            if opt == 0:
                print("Returning to main menu")
            return
#init program                 
while True:
    print("\n*****INVENTORY*****\n")
    print("1.Add products")
    print("2.Search products")
    print("3.Update products")
    print("4.Update amount product")
    print("5.Delete products")
    print("6.Calculate_inventory")
    print("7.Salir")


    opt = input("\nEnter a option: ")
    print("")
    opt = validate_int(opt)
#Options of program 
    match opt:
        case 1:
            add_products()
        case 2:
            view_product(inventory)
        case 3:
            update_product()
        case 4:
            update_amount_product()
        case 5:
            delete_product()
        case 6:
            calculate_inventory()
        case 7:
            print("See you later")
            exit()
        case _:
            print("Enter a valid value")