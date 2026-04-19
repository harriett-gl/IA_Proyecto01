from pathlib import Path
import sys
import random

from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from src.predict import predecir_texto

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "web" / "templates"),
    static_folder=str(BASE_DIR / "web" / "static")
)


def generar_ticket_id():
    return random.randint(1000, 9999)


@app.route("/", methods=["GET", "POST"])
def index():
    prediccion = None
    texto_ingresado = ""
    asunto_ingresado = ""
    ticket_id = generar_ticket_id()

    if request.method == "POST":
        ticket_id = generar_ticket_id()
        asunto_ingresado = request.form.get("asunto", "")
        texto_ingresado = request.form.get("texto", "")

        texto_completo = f"{asunto_ingresado} {texto_ingresado}".strip()

        if texto_completo:
            prediccion = predecir_texto(texto_completo)

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
        texto_ingresado=texto_ingresado,
        asunto_ingresado=asunto_ingresado,
        ticket_id=ticket_id
    )


if __name__ == "__main__":
    app.run(debug=True)