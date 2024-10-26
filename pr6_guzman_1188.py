print("")
print("guzman jared 1188")
print("")
#abre el documento de texto sobrescribhiendo el contenido
f=open("demosracion3.txt","w")
f.write("Woops! I have  deleted the content!")
f.close()

f=open("demosracion3.txt","r")
print(f.read())