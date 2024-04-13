aclNum=int(input("Ingrese el numero de la ACL IPv4:"))
if aclNum >= 1 and aclNum <=99:
    print ("Este es una ACL IPv4 Estandar.")
elif aclNum >= 100 and aclNum <=199:
    print ("Esta es una ACL IPv4 Extendida.")
else:
    print("El número de la ACL no es Estandar ni Extendida.")