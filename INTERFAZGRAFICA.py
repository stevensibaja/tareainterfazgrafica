import tkinter



#codigo de fibonacci

def fibonac():
     return fibonac()
    

    

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

    
#funcion para informacion.
def info():
    return info
# funcion para animacion.
ani=6
def ani():
    return ani()
# crear funcion para atras
def atras():
    return atras()



#creamos las ventanas

    
def main():
    # Window settings
    window = tkinter.Tk()
    window.title("interfas grafica")
    window.geometry("800x450")
 #   window.iconbitmap("icon.ico")
    window.resizable(False, False)
    window.config(cursor='heart')


    
# Canvas settings
    pannel_canvas = tkinter.Canvas(window, width=274, height=446, borderwidth=0, highlightthickness=0, bg="orange")
    pannel_canvas.place(x=0, y=2)

    anim_canvas = tkinter.Canvas(window, width=524, height=446, borderwidth=0, highlightthickness=0, bg="red")
    anim_canvas.place(x=276, y=2)

   

     #Canvas components
    label = tkinter.Label(pannel_canvas, text="Press to start the animation", font=("Haettenschweiler", 15), bg="#606060", fg=White)
    label.place(x=25, y=25)
    boton_fibonacci = tkinter.Button(pannel_canvas, text="fibonacci", command=fibonac,bg=("red"))
    boton_fibonacci.place(x=25, y=50)
    boton_informacion= tkinter.Button(pannel_canvas,text= "informacion personal",command=info, bg = "sky blue")
    boton_informacion.place(x=25, y=150)
    boton_animacion= tkinter.Button(pannel_canvas,text= "animacion",command= ani, bg = "orange")
    boton_animacion.place(x=25, y=250)
    boton_atras= tkinter.Button(pannel_canvas,text="atras",command=atras,bg="white")
    boton_atras.place(x=25,y=350)
main()
main.mainloop()
      
