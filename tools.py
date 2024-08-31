import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from toolExecute import on_entry_click, on_focusout, create_progressbar, is_dark_mode

textSize = 15
paddingX = 5
paddingY = 5
margin = 5
window_width = 700
window_height = 500
size_components = 50

def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

def close_window():
    root.destroy()

#SI SE DEFINE UN TOPBAR PERSONALIZADO, USAR ESTE.
def create_custom_title_bar(root, bg_color, fg_color):
    title_bar = tk.Frame(root, bg=bg_color, relief='solid', bd=1)
    title_bar.pack(side=tk.TOP, fill=tk.X)
    
    title_label = tk.Label(title_bar, text=root.title(), bg=bg_color, fg=fg_color)
    title_label.pack(side=tk.LEFT, padx=2)

    close_button = tk.Button(title_bar, text='CLOSE', width=10, height=2, command=close_window, bg=bg_color, fg=fg_color, bd=0)
    close_button.pack(side=tk.RIGHT, padx=1)

    title_bar.bind('<B1-Motion>', move_window)
    title_label.bind('<B1-Motion>', move_window)

    return title_bar

def on_button_click():
    #progressBar.start(interval=10)
    if get_entry_text(entries=entries):
        messagebox.showinfo(title="Mensaje Validacion", message="¡Todos los campos son necesarios!")
    else:
        result = len(entries[0].get("1.0", tk.END).strip())
        set_entry_text(label=label0, text=result)
        
def get_entry_text(entries):
    isEmpty = False
    for entry in entries:
        text_content = entry.get("1.0", tk.END).strip()
        # Si el texto es igual al placeholder, considerar como vacío
        placeholder = getPlaceHolder(entry)
        if text_content == placeholder:
            text_content = ""
            isEmpty = True
        print(f"Texto del Entry: {placeholder}: '{text_content}'")
    
    #progressBar.stop()
    return isEmpty

def getPlaceHolder(entry):
    """Obtiene el texto del placeholder del widget Text."""
    return getattr(entry, 'placeholder_text', None)
    
# Create entry
def create_entry_with_placeholder(root, placeholder_text, bg_color, fg_color, placeholder_color):
    paddingX = 10
    paddingY = 10
    margin = 20
    #Create frame
    frame = tk.Frame(root)
    frame.pack(pady=margin, padx=margin, expand=True, fill=tk.BOTH)
    
    #Create entry
    entry = tk.Text(frame, bg=bg_color, fg=fg_color, width=size_components, height=10,font=('Helvetica', textSize))
    entry.insert("1.0", placeholder_text)
    entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipadx=paddingX, ipady=paddingY, pady=0)
    
    #Create scrollBar
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=entry.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    entry.config(yscrollcommand=scrollbar.set)
    
    #focus actions
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, placeholder_text, placeholder_color))
    entry.bind("<FocusOut>", lambda event: on_focusout(event, entry, placeholder_text, placeholder_color))
    return entry

def create_label(root, placeholder_text):
    label = tk.Label(root, text=placeholder_text, font=('Helvetica', textSize))
    label.pack(pady=10)
    return label

def set_entry_text(label, text):
    label.config(text=text)

# Create root view
root = tk.Tk()
root.title("TEXT SIZE TOOL")    
#root.overrideredirect(1)  # Oculta la barra de título nativa
root.minsize(width=window_width, height=window_height)
root.iconbitmap('icon.ico')

# apply theme
dark_mode = is_dark_mode()
bg_color = '#0e0f14' if dark_mode else '#f5f5f5'
fg_color = '#fafafa' if dark_mode else '#0f0f0f'
placeholder_color = '#dedede' if dark_mode else '#2b2a2a'

#create_custom_title_bar(root, bg_color, fg_color)

# El contenido de la ventana
#content_frame = tk.Frame(root, bg=bg_color)
#content_frame.pack(expand=True, fill=tk.BOTH)
    
root.configure(bg=bg_color)

# Screen Size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# canculate position for center
position_x = (screen_width - window_width) // 2
position_y = (screen_height - window_height) // 2

# Set root view geometry
root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

# Tittle
label = tk.Label(root, text="Ingrese el texto!", font=('Helvetica', textSize), bg=bg_color, fg=fg_color)
label.pack(pady=10)

# for create entry in list ## NOT USE FOR NOW
placeholders = ["TEXT"]

#Entry list
entries = []

# Create inputs by holders
for index, placeholder in enumerate(placeholders):
    entry = create_entry_with_placeholder(root, placeholder, bg_color, fg_color, placeholder_color)
    entry.placeholder_text = placeholder  # Guardar el texto del placeholder en el Entry
    entries.append(entry)
    
# Label to set tax 0
label0 = create_label(root, "0")
    
# Barra de progreso
#progressBar = create_progressbar(root, ttk)

# Crear un botón
button = tk.Button(root, text = "Check Length",  font=('Helvetica', textSize), width=size_components,  command=on_button_click,bg=bg_color, fg=fg_color )
button.pack(ipadx=paddingX, ipady=paddingY, pady=margin)  # padding horizontal y vertical

# Ejecutar el bucle principal de la aplicación
root.mainloop()