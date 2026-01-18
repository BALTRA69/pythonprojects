import tkinter as tk

calculation =""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_space.delete(1.0,"end")
    text_space.insert(1.0,calculation)
    
def evaluate_calculation():
    global calculation
    try:
        if "/" in calculation:
            parts = calculation.split("/")
            if len(parts)>1 and parts[-1].strip() == '0':
                raise ZeroDivisionError("Cant divide by zero!!")
        calculation=str(eval(calculation))
        text_space.delete(1.0,"end")
        text_space.insert(1.0,calculation)
    except ZeroDivisionError as a:
        clear_field()
        text_space.insert(1.0,a)
    except SyntaxError:
        clear_field()
        text_space.insert(1.0,"Syntax Error")
    except Exception as e:
        clear_field
        text_space.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation =""
    text_space.delete(1.0,"end")


root = tk.Tk()
root.geometry("400x350")
root.title("Calculator")
text_space = tk.Text(root,font=("Aerial",24),height=2,width=20)
text_space.grid(row=0, column=0, columnspan=5,padx=0,pady=0)

b1=tk.Button(root,text=1,font=("Aerial","10"),command=lambda:add_to_calculation(1),width=8,height=2)
b1.grid(row=2,column=0,padx=0,pady=0,sticky='nsew')
b2=tk.Button(root,text=2,font=("Aerial","10"),command=lambda:add_to_calculation(2),width=8,height=2)
b2.grid(row=2,column=1,padx=0,pady=0,sticky='nsew')
b3=tk.Button(root,text=3,font=("Aerial","10"),command=lambda:add_to_calculation(3),width=8,height=2)
b3.grid(row=2,column=2,padx=0,pady=0,sticky='nsew')
b4=tk.Button(root,text=4,font=("Aerial","10"),command=lambda:add_to_calculation(4),width=8,height=2)
b4.grid(row=3,column=0,padx=0,pady=0,sticky='nsew')
b5=tk.Button(root,text=5,font=("Aerial","10"),command=lambda:add_to_calculation(5),width=8,height=2)
b5.grid(row=3,column=1,padx=0,pady=0,sticky='nsew')
b6=tk.Button(root,text=6,font=("Aerial","10"),command=lambda:add_to_calculation(6),width=8,height=2)
b6.grid(row=3,column=2,padx=0,pady=0,sticky='nsew')
b7=tk.Button(root,text=7,font=("Aerial","10"),command=lambda:add_to_calculation(7),width=8,height=2)
b7.grid(row=4,column=0,padx=0,pady=0,sticky='nsew')
b8=tk.Button(root,text=8,font=("Aerial","10"),command=lambda:add_to_calculation(8),width=8,height=2)
b8.grid(row=4,column=1,padx=0,pady=0,sticky='nsew')
b9=tk.Button(root,text=9,font=("Aerial","10"),command=lambda:add_to_calculation(9),width=8,height=2)
b9.grid(row=4,column=2,padx=0,pady=0,sticky='nsew')
b0=tk.Button(root,text=0,font=("Aerial","10"),command=lambda:add_to_calculation(0),width=8,height=2)
b0.grid(row=5,column=1,padx=0,pady=0,sticky='nsew')

bplus=tk.Button(root,text="+",font=("Aerial","10"),command=lambda:add_to_calculation("+"),width=8,height=2)
bplus.grid(row=2,column=3,padx=0,pady=0,sticky='nsew')
bsub=tk.Button(root,text="-",font=("Aerial","10"),command=lambda:add_to_calculation("-"),width=8,height=2)
bsub.grid(row=3,column=3,padx=0,pady=0,sticky='nsew')
bmul=tk.Button(root,text="x",font=("Aerial","10"),command=lambda:add_to_calculation("*"),width=8,height=2)
bmul.grid(row=4,column=3,padx=0,pady=0,sticky='nsew')
bdiv=tk.Button(root,text="/",font=("Aerial","10"),command=lambda:add_to_calculation("/"),width=8,height=2)
bdiv.grid(row=5,column=3,padx=0,pady=0,sticky='nsew')

bleftparen=tk.Button(root,text="(",font=("Aerial","10"),command=lambda:add_to_calculation("("),width=8,height=2)
bleftparen.grid(row=5,column=0,padx=0,pady=0,sticky='nsew')
brightparen=tk.Button(root,text=")",font=("Aerial","10"),command=lambda:add_to_calculation(")"),width=8,height=2)
brightparen.grid(row=5,column=2,padx=0,pady=0,sticky='nsew')

bcal=tk.Button(root,text="=",font=("Aerial","10"),command=evaluate_calculation,width=18,height=2)
bcal.grid(row=6, column=2, columnspan=2,padx=0,pady=0,sticky='nsew')
bclear=tk.Button(root,text="CE",font=("Aerial","10"),command=lambda:clear_field(),width=24,height=2)
bclear.grid(row=6, column=0, columnspan=2,padx=0,pady=0,sticky='nsew')
root.mainloop()
