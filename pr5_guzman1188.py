print("")
print("guzman jared 1188")
print("")
#abre documento de texto y muestra una nueva linea
f = open ("demosracion2.txt","a")
f.write("Now the file has more content!")
f.close()

f=open("demosracion2.txt","r")
print(f.read())