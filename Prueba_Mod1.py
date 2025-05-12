#saves each created dictionary as an element of a list
inventory:list = []

#Create a product in dictionary format with the key name and a tuple as a value 
#that has price and quantity, check if the product exists and that the values ​​are greater than 0
def add_product(name:str = "", price:float = 0, amount:int = 0):
    name:str = name.strip().lower()  
    for product in inventory:
        if name in product:
            return print(f"El producto {name} ya existe...")
    
    if price > 0 and amount > 0:
        product:dict = {
            name: (price, amount)
        }
        inventory.append(product)
        return print(f"Producto {name} añadido\n-------------------------------------")
    
    else:
        return print(f"El precio y la cantidad deben ser valores mayores a 0")


#Search for the product given its name, show its name, price and quantity, if it is not there it 
#shows that it is not found
def search_product(name:str = ""):
    name:str = name.strip().lower() 
    for product in inventory:
        if name in product:
            price, amount = product[name]
            return print(f"Nombre: {name} \nPrecio: {price} \nCantidad = {amount}")
    
    return print(f"El producto {name} no se encuentra...")


#Updates the price given a name, if the product is not there it indicates it and also verifies that 
#the new price is a positive value
def update_price(name:str = "", new_price:float = 0):
    name:str = name.strip().lower()
    if new_price > 0:
        for product in inventory:
            if name in product:
                _, amount = product[name]
                new_tup = (new_price, amount)
                product[name] = new_tup
                return print(f"El precio de {name} se ha actualizado correctamente a {new_price}")
        
        return print(f"El producto {name} no se encuentra...")
    else:
        return print(f"El valor del nuevo producto debe ser mayor a 0...")


#Delete a product according to the name received, if the product does not exist it indicates it with 
#a message
def delete_procut(name:str = ""):
    name:str = name.strip().lower()
    for product in inventory:
        if name in product:
            inventory.remove(product)
            return print(f"El producto {name} se ha eliminado correctamente...")
    
    return print(f"El producto {name} no se encuentra...")


#Calculates the total price of the inventory with a lambda function. This function takes each price
#and value of the product, seen as an Xi, being equal to price * amount, adds each Xi of the 
#inventory and returns its result.
calculate_total_price = lambda:sum(price * amount
for product in inventory
    for price, amount in product.values())


#Just displays a menu
def show_menu():
    print("========================= INVENTARIO ========================= \n" \
    "Por favor seleccione la opcion que desea realizar\n" \
    "1. Añadir productos nuevos\n" \
    "2. Consultar productos\n" \
    "3. Actualizar los precios\n" \
    "4. Eliminar productos\n" \
    "5. Calcular el valor total del inventario\n" \
    "6. Salir\n")


#main function where each of the functions is called depending on the selected
#option, this is where the data is collected for each case
def main():
    print("======BIENVENIDO AL SISTEMA PARA GESTIONAR SU INVENTARIO=======")

    while True:
        show_menu()
        try:
            option:int = int(input("Ingrese el numero de la opcion: "))
            if option == 1:
                size = len(inventory)
                if size < 5:
                    print("Debe ingresar al menos 5 productos")
                    for i in range(1, 5 +1):
                        name:str = str(input("Nombre del producto: "))
                        price:float = float(input("Precio del producto: "))
                        amount:int = int(input("Cantidad del producto: "))
                        print("---------------------------------------")
                        add_product(name, price, amount)
                else:
                    name:str = str(input("Nombre del producto: "))
                    price:float = float(input("Precio del producto: "))
                    amount:int = int(input("Cantidad del producto: "))
                    add_product(name, price, amount)
            
            elif option == 2:
                name:str = str(input("Nombre del producto a buscar: "))
                search_product(name)
            
            elif option == 3:
                name:str = str(input("Ingrese el nombre del producto para actualizar su precio: "))
                new_price:float = float(input("Nuevo precio: "))
                update_price(name, new_price)
            
            elif option == 4:
                name:str = str(input("Nombre del producto a eliminar: "))
                delete_procut(name)
            
            elif option == 5:
                total_price:float = round(calculate_total_price(),2 )
                print(f"El valor total del inventario es: {total_price}")
            
            elif option == 6:
                print("Saliendo del programa, hasta pronto...")
                break

            else:
                print("Oops! esa no es una opcion valida :c")

        except ValueError:
            print("Debes ingresar el numero de la accion a realizar o los datos que correspondan")


#causes the file to be executed directly in the code and not in case of importing as a module
#but you could also call the main() function in the traditional way without any problem
if __name__ == "__main__":
    main()