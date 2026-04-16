from pathlib import Path

from src.preprocessing import limpiar_texto
from src.vectorizer import vectorizar_corpus
from src.naive_bayes import NaiveBayes


def predecir_texto(texto):
    base_dir = Path(__file__).resolve().parent.parent
    ruta_modelo = base_dir / "model" / "naive_bayes_model.pkl"

    modelo = NaiveBayes.cargar_modelo(ruta_modelo)

    documento = limpiar_texto(texto)
    vector = vectorizar_corpus([documento], modelo.vocabulario)[0]

    prediccion = modelo.predecir(vector)
    return prediccion


if __name__ == "__main__":
    texto = "My internet connection is failing"
    resultado = predecir_texto(texto)
    print("Texto:", texto)
    print("Predicción:", resultado)