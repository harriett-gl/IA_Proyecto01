from flask import Flask, render_template, request
from datetime import datetime
import random

from src.predict import predecir_texto, obtener_categorias_modelo

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)

def generar_ticket_id():
    fecha = datetime.now().strftime("%Y%m%d")
    aleatorio = random.randint(1000, 9999)
    return f"TKT-{fecha}-{aleatorio}"

@app.route("/", methods=["GET", "POST"])
def index():

    prediccion = None
    ticket_id = generar_ticket_id()

    asunto_ingresado = ""
    texto_ingresado = ""

    categorias = obtener_categorias_modelo()

    if request.method == "POST":

        asunto_ingresado = request.form.get("asunto", "")
        texto_ingresado = request.form.get("texto", "")

        texto_completo = asunto_ingresado + " " + texto_ingresado

        if texto_completo.strip():
            prediccion = predecir_texto(texto_completo)

    return render_template(
        "index.html",
        ticket_id=ticket_id,
        prediccion=prediccion,
        categorias=categorias,
        asunto_ingresado=asunto_ingresado,
        texto_ingresado=texto_ingresado,
        probabilidades=None
    )

if __name__ == "__main__":
    app.run(debug=True)