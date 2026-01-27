email =input()
if(email.count("@")==0):
    print("No existe @ en el mail")
elif (email.find(".")== -1):
    print("El mail no tiene .")
elif (email.startswith("@") or email.endswith("@")):
    print("@ al inicio o al final")
elif (email.find("@")!= email.rfind("@")):
    print("Existe mas de una @")
elif(email.rfind(".") < email.find("@")):
    print("Debe existirr un punto despues de la @")
else:
    ultimoPunto = email.rfind(".")
    dominio = email[ultimoPunto + 1:]
    longDominio = len(dominio)
    if(longDominio >= 2 and longDominio <= 3):
        print("Email Correcto")

