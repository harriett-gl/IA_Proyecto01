from pathlib import Path

from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus
from src.naive_bayes import NaiveBayes


def entrenar_y_guardar():
    textos = [

        # SOPORTE
        "My internet is not working",
        "I cannot connect to WiFi",
        "The modem is failing",
        "Mi internet no funciona",
        "No tengo conexión wifi",
        "El modem no responde",
        "No puedo conectarme a la red",
        "Se cayó el internet",

        # CANCELACION
        "I want to cancel my subscription",
        "Please cancel my service",
        "Close my account",
        "Quiero cancelar mi servicio",
        "Deseo cancelar mi suscripción",
        "Ya no quiero el plan",
        "Den de baja mi cuenta",

        # FACTURACION
        "I was charged twice",
        "Billing problem",
        "My invoice is wrong",
        "Me cobraron dos veces",
        "Problema de facturación",
        "La factura está incorrecta",
        "Cobro no reconocido",
        "Me llegó un cobro extra",

        # QUEJA
        "Bad customer service",
        "I am unhappy",
        "Worst support ever",
        "El servicio fue malo",
        "Quiero poner una queja",
        "Estoy inconforme",
        "Muy mala atención",
        "El agente fue grosero"
    ]

    etiquetas = [
        "soporte",
        "cancelacion",
        "facturacion",
        "queja",
    ]

    documentos = [limpiar_texto(t) for t in textos]

    vocabulario = construir_vocabulario(documentos)
    X = vectorizar_corpus(documentos, vocabulario)

    modelo = NaiveBayes()
    modelo.entrenar(X, etiquetas, vocabulario)

    base_dir = Path(__file__).resolve().parent.parent
    model_dir = base_dir / "model"
    model_dir.mkdir(exist_ok=True)

    ruta_modelo = model_dir / "naive_bayes_model.pkl"
    modelo.guardar_modelo(ruta_modelo)

    print("Modelo entrenado en español e inglés.")


if __name__ == "__main__":
    entrenar_y_guardar()