productos=[]
opcion=1

while(opcion !=0):
    producto={}
    opcion=int(input("digite una opcion:"))
    if(opcion==1):
        producto["codigo"]=input("digite codigo del producto : ")
        producto["nombre"]=input("digite nombre del producto : ")
        producto["precio"]=int(input("digite precio del producto : "))

        productos.append(producto)

    elif(opcion==2):
       print(productos) 
    elif(opcion==3):
        print("")
    else:
        print("")
