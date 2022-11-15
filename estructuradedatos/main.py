##estructura de datos
##listas
##metodos para estructura de dato tipo lista en python
# list=['deyanira']#una lista vacia
# list.append('diego')
# list.insert(0,'jamely')
# list.insert(2,'edith')
# list.insert(len(list),'lilian')
# print(list)

#numero del 1 a 20 solo pares
# list=[]
# for i in range(21):
#     if i%2==0:
#       list.append(i)
# print(list)

# unir listas
vocalesuno=["a","e"]
vocalesdos=["i","o","u"]

vocalesuno.extend(vocalesdos)
vocalesuno[3]="00"
vocalesuno.remove("u")
print(vocalesuno)