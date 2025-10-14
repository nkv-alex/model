#!/usr/bin/env python3
import os
from gpt4all import GPT4All
import getpass

# --- Configuración ---
destino = os.path.expanduser("~/Desktop/model")
os.makedirs(destino, exist_ok=True)

# URL del modelo
url = "https://huggingface.co/nomic-ai/gpt4all-j/resolve/main/pytorch_model-00001-of-00002.bin"
ruta_modelo = os.path.join(destino, "pytorch_model-00001-of-00002.bin")

# Descargar modelo si no existe
if not os.path.exists(ruta_modelo):
    print(f"📥 Descargando {os.path.basename(ruta_modelo)} ...")
    os.system(f"wget {url} -O {ruta_modelo}")
else:
    print(f"✅ {os.path.basename(ruta_modelo)} ya existe, omitiendo descarga.")

# --- Crear script ejecutable ---
script_cmd = "/usr/local/bin/chatbot-cmd"
script_content = f"""#!/usr/bin/env python3
from gpt4all import GPT4All
import os

model_path = r"{ruta_modelo}"
model = GPT4All(model_path)

try:
    pregunta = input("> ")
    respuesta = model.generate(pregunta)
    print(respuesta)
except KeyboardInterrupt:
    print("\\nSaliendo...")
"""

# Escribir el script
with open(script_cmd, "w") as f:
    f.write(script_content)

# Dar permisos de ejecución
os.system(f"sudo chmod +x {script_cmd}")

# --- Crear alias >= ---
bashrc_path = os.path.expanduser("~/.bashrc")
alias_line = "alias '>='='/usr/local/bin/chatbot-cmd'\\n"

# Evitar duplicados
with open(bashrc_path, "r") as f:
    if ">=\'" not in f.read():
        with open(bashrc_path, "a") as fa:
            fa.write(alias_line)

# Fuente del bashrc
os.system("source ~/.bashrc")

print("✅ Chatbot instalado como comando '>='")
print("Ejecuta '>= ' y escribe tu pregunta (solo una respuesta por ejecución).")
