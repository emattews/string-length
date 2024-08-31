import winreg
import tkinter as tk

def is_dark_mode():
    """Determina si el sistema está en modo oscuro consultando el registro de Windows."""
    try:
        key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
        value_name = 'AppsUseLightTheme'
        
        # Abre la clave del registro
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            value, _ = winreg.QueryValueEx(key, value_name)
        
        # 0 significa modo oscuro y 1 significa modo claro
        return value == 0
    except FileNotFoundError:
        print('La clave o el valor del registro no se encontraron.')
        return False
    except Exception as e:
        print(f'Error al determinar el modo oscuro: {e}')
        return False
    
# Event to entry click
def on_entry_click(event, entry, placeholder_text, placeholder_color):
    """Función que limpia el placeholder cuando se hace clic en el Entry."""
    if entry.get("1.0", tk.END).strip() == placeholder_text:
        entry.delete("1.0", tk.END)
        entry.config(fg=placeholder_color)

# Event to entry focus
def on_focusout(event, entry, placeholder_text, placeholder_color):
    """Función que restaura el placeholder si el Entry está vacío al perder el foco."""
    if not entry.get("1.0", tk.END).strip():
        entry.insert("1.0", placeholder_text)
        entry.config(fg=placeholder_color)
        
def create_progressbar(root, ttk):
    style = ttk.Style()
    styleName = "TProgressbar"
    # Configurar el estilo para un Progressbar circular
    style = ttk.Style()
    style.configure(styleName, mode="indeterminate", thickness=30)

    # Crear un Progressbar indeterminado con el estilo circular
    progressbar = ttk.Progressbar(root, style=styleName, length=600)
    progressbar.pack(pady=20)
    return progressbar