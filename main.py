import tkinter as tk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("Contacts") 
ventana.geometry("500x400+700+300")
#Componentes
class Etiqueta:
    def __init__(self,ventana,texto,x,y):
        self.label=tk.Label(ventana,text=texto)
        self.label.place(x=x,y=y)
class Entrada:
    def __init__(self,ventana,width,x,y):
        self.entry=tk.Entry(ventana,width=width)
        self.entry.place(x=x,y=y)
    def get(self):
         return self.entry.get() 
#Funcion clear
def clear():
     name_e.entry.delete(0, tk.END)
     number_e.entry.delete(0, tk.END)
    
#Funcion Create
def crear_contacto():
    nombre = name_e.get()
    numero = number_e.get()
    if not nombre or not numero:
        messagebox.showwarning("Advertencia", "Completa ambos campos.")
        return
    try:
        int(numero)
    except ValueError:
        messagebox.showerror("Error", "El número debe ser numérico.")
        return

    encontrado = False
    try:
        with open("friendsContact.txt", "r") as f   :
            for linea in f:
                partes = linea.strip().split("!")
                if len(partes) == 2:
                    if partes[0] == nombre or partes[1] == numero:
                        encontrado = True
                        break
    except FileNotFoundError:
     pass
    if not encontrado:
        with open("friendsContact.txt", "a") as f:
            f.write(f"{nombre}!{numero}\n")
        messagebox.showinfo("Éxito", "Contacto agregado.")
        print("Friend Added")
    else:
        messagebox.showwarning("Duplicado", "El contacto ya existe.")
        print("Input name or number already exist")
#Función Read
def leer_contactos():
    nombre_buscado = name_e.get().strip()
    if nombre_buscado:
        try:
            with open("friendsContact.txt", "r") as f:
                encontrado = False
                for linea in f:
                    partes = linea.strip().split("!")
                    if len(partes) == 2:
                        nombre, numero = partes
                        if nombre == nombre_buscado:
                            number_e.entry.delete(0, tk.END)
                            number_e.entry.insert(0, numero)
                            messagebox.showinfo("Contacto encontrado", f"Friend Name: {nombre}\nContact Number: {numero}")
                            encontrado = True
                            break
                if not encontrado:
                    messagebox.showwarning("No encontrado", "El nombre no existe.")
        except FileNotFoundError:
            messagebox.showinfo("Contactos", "No hay contactos registrados.")
    else:
        # Si no hay nombre, muestra todos los contactos
        try:
            with open("friendsContact.txt", "r") as f:
                contactos = []
                for linea in f:
                    partes = linea.strip().split("!")
                    if len(partes) == 2:
                        nombre, numero = partes
                        contactos.append(f"Friend Name: {nombre}\nContact Number: {numero}\n")
                if contactos:
                    messagebox.showinfo("Contactos", "".join(contactos))
                else:
                    messagebox.showinfo("Contactos", "No hay contactos registrados.")
        except FileNotFoundError:
            messagebox.showinfo("Contactos", "No hay contactos registrados.")
#Función Update
def actualizar_contacto():
    nombre = name_e.get()
    nuevo_numero = number_e.get()
    if not nombre or not nuevo_numero:
        messagebox.showwarning("Advertencia", "Completa ambos campos.")
        return
    try:
        int(nuevo_numero)
    except ValueError:
        messagebox.showerror("Error", "El número debe ser numérico.")
        return

    actualizado = False
    lineas_actualizadas = []
    try:
        with open("friendsContact.txt", "r") as f:
            for linea in f:
                partes = linea.strip().split("!")
                if len(partes) == 2:
                    if partes[0] == nombre:
                        lineas_actualizadas.append(f"{nombre}!{nuevo_numero}\n")
                        actualizado = True
                    else:
                        lineas_actualizadas.append(linea)
    except FileNotFoundError:
        messagebox.showinfo("Contactos", "No hay contactos registrados.")
        return

    if actualizado:
        with open("friendsContact.txt", "w") as f:
            f.writelines(lineas_actualizadas)
        messagebox.showinfo("Éxito", "Contacto actualizado.")
        print("Friend updated.")
    else:
        messagebox.showwarning("No encontrado", "El nombre no existe.")
        print("Input name does not exist.")
#Función Delete
def eliminar_contacto():
    nombre = name_e.get().strip()
    if not nombre:
        messagebox.showwarning("Advertencia", "Ingresa el nombre a eliminar.")
        return

    eliminado = False
    lineas_restantes = []
    try:
        with open("friendsContact.txt", "r") as f:
            for linea in f:
                partes = linea.strip().split("!")
                if len(partes) == 2:
                    if partes[0] == nombre:
                        eliminado = True  # No agregamos esta línea, la eliminamos
                    else:
                        lineas_restantes.append(linea)
    except FileNotFoundError:
        messagebox.showinfo("Contactos", "No hay contactos registrados.")
        return

    if eliminado:
        with open("friendsContact.txt", "w") as f:
            f.writelines(lineas_restantes)
        messagebox.showinfo("Éxito", "Contacto eliminado.")
        print("Friend deleted.")
        clear()  # Limpia los campos después de eliminar
    else:
        messagebox.showwarning("No encontrado", "El nombre no existe.")
        print("Input name does not exist.")
#Elementos de la interfaz
name_l=Etiqueta(ventana,"Name :",x=20,y=20)
number_l=Etiqueta(ventana,"Number :", x=20,y=50)
name_e=Entrada(ventana,35,x=100,y=20)
number_e=Entrada(ventana,35,x=100,y=50) 
create_b=tk.Button(ventana,width=10,text="Create",command=crear_contacto)
create_b.place(x=50,y=250)
read_b=tk.Button(ventana,width=10,text="Read",command=leer_contactos)
read_b.place(x=150,y=250)
update_b=tk.Button(ventana,width=10,text="Update",command=actualizar_contacto)
update_b.place(x=250,y=250)
delete_b=tk.Button(ventana,width=10,text="Delete",command=eliminar_contacto)
delete_b.place(x=350,y=250)
clear_b=tk.Button(ventana,width=10,text="Clear",command=clear)  
clear_b.place(x=200,y=300)

ventana.mainloop()          