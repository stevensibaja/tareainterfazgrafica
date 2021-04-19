
import tkinter

def fibonacci(num):
    if (isinstance (num,int) and (num>=0)):
        return fibonacci_aux(num)
    else:
        return ("el numero debe ser engtero y positivo")
def fibonacci_aux(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_aux (num-1) + fibonacci_aux (num-2)
# funcion para para cambiar a la ventana fibonacci
def ir_fibo():
    inicial.forget()
    ventana_fibo.pack(fill='both',expand=1)


#funcion para boton de atras
def atras():
    ventana_fibo.forget()
    ventana_info.forget()
    inicial.pack(fill='both',expand=1)

def ir_info():
    inicial.forget()
    ventana_info.pack(fill='both',expand=1)






 ###ventanas####
    
ventana =  tkinter.Tk() #ventana padre
ventana.geometry("600x400")
ventana.config(cursor='heart')
ventana.title("interfaz grafica-steven sibaja")

###ventanas hijas###
inicial= tkinter.Frame(ventana)# ventana principal
ventana_fibo = tkinter.Frame(ventana) #ventana fibo
ventana_info = tkinter.Frame(ventana)



 ####Label####
label_fibo=tkinter.Label(ventana_fibo,text='ventana nueva')# se crea una ventana nueva
label_fibo.pack(pady=20)# corre el texto con base al eje y
label_inicial = tkinter.Label(inicial,text= "botones de comando")# primer ventana en aparecer
label_inicial.pack(pady=20) # se utiliza para el espacio del texto hacai abajo
label_info = tkinter.Label(ventana_info,text= "info")# primer ventana en aparecer de info
label_info.pack(pady=20) # se utiliza pa

    #####botones####

boton_fibonacci= tkinter.Button(inicial,text= "fibonacci",command= ir_fibo, bg = "fuchsia") 
boton_info= tkinter.Button(inicial,text= "informacion personal",command= ir_info, bg = "sky blue")
boton_ani= tkinter.Button(inicial,text= "animacion", bg = "orange")
boton_atras_fibo= tkinter.Button(ventana_fibo,text="atras", command= atras, bg="white")
boton_atras_info= tkinter.Button(ventana_info,text="atras", command= atras, bg="white")


boton_fibonacci.pack(pady=10)
boton_info.pack(pady=20)
boton_ani.pack(pady=30)
boton_atras_fibo.pack(pady=40)
boton_atras_info.pack()
inicial.pack()


                       
ventana.mainloop()







#width=8,height=4)



'''
def fibonacci(num):
    if (isinstance (num,int) and (num>=0)):
        return fibonacci_aux(num)
    else:
        return ("el numero debe ser engtero y positivo")
def fibonacci_aux(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci_aux (num-1) + fibonacci_aux (num-2)
'''  
