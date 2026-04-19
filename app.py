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
    confianza = None
    probabilidades = None
    ticket_id = generar_ticket_id()

    asunto_ingresado = ""
    texto_ingresado = ""

    categorias = obtener_categorias_modelo()

    if request.method == "POST":
        asunto_ingresado = request.form.get("asunto", "")
        texto_ingresado = request.form.get("texto", "")

        texto_completo = f"{asunto_ingresado} {texto_ingresado}".strip()

        if texto_completo:
            resultado = predecir_texto(texto_completo)
            prediccion = resultado["categoria"]
            confianza = resultado["confianza"]
            probabilidades = resultado["probabilidades"]

    return render_template(
        "index.html",
        ticket_id=ticket_id,
        prediccion=prediccion,
        confianza=confianza,
        categorias=categorias,
        asunto_ingresado=asunto_ingresado,
        texto_ingresado=texto_ingresado,
        probabilidades=probabilidades
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)