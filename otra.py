from customtkinter import *    # Importar todas las funciones de customtkinter
from CTkTable import ctktable as CTkTable
from itertools import product  # Importar la función product de itertools
from tabulate import tabulate  # Importar la función tabulate de tabulate

set_appearance_mode("grey")

app = CTk()

app.title("Truth Table")
app.geometry("1000x650")

title_frame = CTkFrame(master=app,width=1000,height=150,fg_color="#2D3142")
title_frame.grid_propagate(False)
title_frame.grid(row=0)
specs_frame = CTkFrame(master=app,width=200,height=200,fg_color="#2D3142")
specs_frame.grid_propagate(False)
specs_frame.grid(row=1,sticky="w")
input_frame = CTkFrame(master=app,width=800,height=200,fg_color="#4F5D75")
input_frame.grid_propagate(False)
input_frame.grid(row=1,sticky="e")
output_frame = CTkFrame(master=app,width=1000,height=300,fg_color="#4F5D75")
output_frame.grid_propagate(False)
output_frame.grid(row=2)

title = CTkLabel(master=title_frame,text="GENERA TABLAS DE VERDAD Y VERIFICA EQUIVALENCIAS LOGICAS",font=("console",25))
title.place(anchor=CENTER,relx = .5, rely = .45)
input = CTkEntry(master=input_frame,placeholder_text="Ingrese la expresion logica (sin espacios)",width=500,height=60,fg_color="#BFC0C0",placeholder_text_color="black")
input.place(anchor=CENTER,relx = .5, rely = .4)
button = CTkButton(master=input_frame,text="Generate",fg_color="#EF8354",text_color="black")
button.place(anchor=CENTER,relx = .5, rely = .62)

values = [["Insert","Equal"],
          ["^"," and "],
          ["v"," or "],
          ["-"," not "],
          ["x"," xor"],
          ["/","inplication"],
          ["|","bicondicional"],
          [",","equivalence"]]
table = CTkTable(master=specs_frame, row=8, column=2, values=values)
table.pack(expand=True, fill="both")


app.mainloop()