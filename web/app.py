from pathlib import Path
import sys

from flask import Flask, render_template, request

# Agregar la raíz del proyecto al path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.predict import predecir_texto

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    prediccion = None
    texto_ingresado = ""

    if request.method == "POST":
        texto_ingresado = request.form["texto"]
        if texto_ingresado.strip():
            prediccion = predecir_texto(texto_ingresado)
            if prediccion == "soporte":
                prediccion = "Soporte Técnico"
        elif prediccion == "facturacion":
            prediccion = "Facturación"
        elif prediccion == "cancelacion":
            prediccion = "Cancelación"
        elif prediccion == "queja":
            prediccion = "Queja"
    return render_template(
        "index.html",
        prediccion=prediccion,
        texto_ingresado=texto_ingresado
    )


if __name__ == "__main__":
    app.run(debug=True)