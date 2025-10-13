#!/usr/bin/env python3
from gpt4all import GPT4All

# Ruta al modelo descargado
model = GPT4All("ruta/al/modelo/pytorch_model-00001-of-00002.bin")

# Prompt tipo shell
try:
    pregunta = input("> ")
    respuesta = model.generate(pregunta)
    print(f"chatbot: {respuesta}")
except KeyboardInterrupt:
    print("\nSaliendo...")