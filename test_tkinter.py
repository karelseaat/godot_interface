import tkinter as tk
from tkinter import ttk
from godot_parser import load


def puttree(item, tkparent ,treeview):
    script = 's' if item.get('script') else 'o'
    inherit = 'i' if item.is_inherited else 'o'
    texture = 't' if item.get('texture') else 'o'
    shape = 's' if item.get('shape') else 'o'


    if tkparent:
        parentitem = treeview.insert(tkparent, 0, text=f"{item.name}{item.type} {script} - {inherit}" )
    else:
        parentitem = treeview.insert("", 0, text=f"{item.name}{item.type} {script}-{inherit}")


    children = item.get_children()
    if children:
        for child in children:
            puttree(child, parentitem, treeview)



scene = load("./Player.tscn")

root = tk.Tk()
root.geometry("500x500")
root.title("Treeview in Tk")
treeview = ttk.Treeview(columns=('size','modified'))
treeview.grid()
treeview.column("#0", minwidth=0, width=500)

treeview.column('size', width=50, anchor='center')
treeview.heading('size', text='Size')
treeview.heading('modified', text='Modified')

with scene.use_tree() as tree:
    puttree(tree.root, "", treeview)

treeview.pack()
root.mainloop()

