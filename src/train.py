from pathlib import Path

from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus
from src.naive_bayes import NaiveBayes


def entrenar_y_guardar():
    textos = [
        "My internet is not working",
        "I cannot connect to WiFi",
        "I want to cancel my subscription",
        "Please cancel my plan",
        "I have a billing problem",
        "I was charged twice",
        "The service is very bad",
        "I am unhappy with the attention"
    ]

    etiquetas = [
        "soporte",
        "soporte",
        "cancelacion",
        "cancelacion",
        "facturacion",
        "facturacion",
        "queja",
        "queja"
    ]

    documentos = [limpiar_texto(texto) for texto in textos]
    vocabulario = construir_vocabulario(documentos)
    X = vectorizar_corpus(documentos, vocabulario)

    modelo = NaiveBayes()
    modelo.entrenar(X, etiquetas, vocabulario)

    base_dir = Path(__file__).resolve().parent.parent
    model_dir = base_dir / "model"
    model_dir.mkdir(exist_ok=True)

    ruta_modelo = model_dir / "naive_bayes_model.pkl"
    modelo.guardar_modelo(ruta_modelo)

    print(f"Modelo guardado en: {ruta_modelo}")


if __name__ == "__main__":
    entrenar_y_guardar()