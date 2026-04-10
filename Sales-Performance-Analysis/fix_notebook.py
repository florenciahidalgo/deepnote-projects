import nbformat
import json

input_file = "Sales performance Analysis.ipynb"
output_file = "clean_notebook.ipynb"

# Leer como JSON bruto (sin validación)
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Forzar estructura válida
data["nbformat"] = 4
data["nbformat_minor"] = 5

# Convertir a notebook válido
nb = nbformat.from_dict(data)

# Guardar limpio
with open(output_file, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook cleaned successfully ✅")
