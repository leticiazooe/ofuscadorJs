import subprocess
import sys
import re
import random

# --- AUTO-INSTALAÇÃO DE DEPENDÊNCIAS ---
def preparar_ambiente():
    for lib in ["customtkinter", "pyperclip"]:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

preparar_ambiente()

import customtkinter as ctk
from tkinter import messagebox

class OfuscadorOWASP(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("JS Shield Ultra - OWASP Compliance Mode")
        self.geometry("900x700")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = ctk.CTkLabel(self, text="Ofuscador de Código JavaScript", font=("Impact", 30), text_color="#3B8ED0")
        self.label.grid(row=0, column=0, pady=20)

        self.textbox = ctk.CTkTextbox(self, font=("Consolas", 12), border_width=2, border_color="#1F6AA5")
        self.textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.textbox.insert("0.0", "// Digite ou cole seu código JS aqui...(apague essa linha)")

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=2, column=0, pady=20)

        self.btn_run = ctk.CTkButton(self.btn_frame, text="OFUSCAR E RENOMEAR", command=self.processar, fg_color="#3B8ED0", hover_color="#1F6AA5")
        self.btn_run.pack(side="left", padx=10)


    def renomear_variaveis(self, js):
        """Troca nomes de variáveis por identificadores _0x..."""
        # Lista de palavras que NÃO podemos renomear (Palavras reservadas do JS)
        reservadas = {'if', 'else', 'function', 'return', 'var', 'let', 'const', 'true', 'false', 'console', 'log', 'document', 'window', 'null', 'undefined', 'break', 'continue', 'while', 'for'}
        
        palavras = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]{2,}\b', js)
        mapeamento = {}
        contador = 1
        
        for p in set(palavras):
            if p not in reservadas:
                hex_id = f"_0x{random.randint(10, 99)}{contador}"
                mapeamento[p] = hex_id
                contador += 1
        
        for original, novo in mapeamento.items():
            js = re.sub(r'\b' + original + r'\b', novo, js)
        
        return js

    def ofuscar_completo(self, js):
        js = self.renomear_variaveis(js)
        
        js = re.sub(r"/\*.*?\*/", "", js, flags=re.DOTALL)
        js = re.sub(r"//.*", "", js)
        
        def to_hex(m):
            return "'" + "".join([f"\\x{ord(c):02x}" for c in m.group(1)]) + "'"
        js = re.sub(r"['\"](.*?)['\"]", to_hex, js)

        js = re.sub(r'\s+', ' ', js)
        for op in ['{', '}', '(', ')', ';', ',', '=', '+', '-', '*', '/', '>', '<', ':', '?']:
            js = js.replace(f' {op}', op).replace(f'{op} ', op)
        
        return js.strip()

    def processar(self):
        txt = self.textbox.get("0.0", "end").strip()
        if not txt or "// Digite" in txt: return
        
        resultado = self.ofuscar_completo(txt)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", resultado)
        messagebox.showinfo("Sucesso", "Ofuscação concluída com renomeação de variáveis!")

    

if __name__ == "__main__":
    app = OfuscadorOWASP()
    app.mainloop()
