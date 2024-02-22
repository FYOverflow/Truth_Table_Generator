from customtkinter import *    # Importar todas las funciones de customtkinter
from CTkTable import CTkTable
from itertools import product  # Importar la función product de itertools
from tabulate import tabulate  # Importar la función tabulate de tabulate

set_appearance_mode("grey")

app = CTk()

app.title("Truth Table")
app.geometry("1000x650")

title_frame = CTkFrame(master=app,width=1000,height=150,fg_color="black")
title_frame.grid_propagate(False)
title_frame.grid(row=0)
specs_frame = CTkFrame(master=app,width=200,height=200,fg_color="black")
specs_frame.grid_propagate(False)
specs_frame.grid(row=1,sticky="w")
input_frame = CTkFrame(master=app,width=800,height=200,fg_color="black")
input_frame.grid_propagate(False)
input_frame.grid(row=1,sticky="e")
output_frame = CTkFrame(master=app,width=1000,height=300,fg_color="black")
output_frame.grid_propagate(False)
output_frame.grid(row=2)

title = CTkLabel(master=title_frame,text="GENERATES TRUTH TABLES AND VERIFIES LOGICAL EQUIVALENCES\nBy FYOverflow && ToasterDEV",font=("console",25,"bold"))
title.place(anchor=CENTER,relx = .5, rely = .45)
input = CTkEntry(master=input_frame,placeholder_text="Enter the logical expression (without spaces)",width=500,height=60,fg_color="#F2F2F2",placeholder_text_color="black")
input.place(anchor=CENTER,relx = .5, rely = .4)
button = CTkButton(master=input_frame,text="Generate",fg_color="#7F7F7F",text_color="black")
button.place(anchor=CENTER,relx = .5, rely = .62)

values = [["Insert","Represent"],
          ["^"," and "],
          ["v"," or "],
          ["-"," not "],
          ["x"," xor"],
          ["/","inplication"],
          ["|","bicondicional"],
          [",","equivalence"]]

table = CTkTable(master=specs_frame, values=values, justify=True,height=24,width=30,border_color="#EF8354",header_color="#7F7F7F",text_color="black",colors=["#CCCCCC", "#A5A5A5"])
table.place(anchor=CENTER, relx=.5,rely=.5)


app.mainloop()