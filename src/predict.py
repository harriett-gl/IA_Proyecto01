from pathlib import Path
from src.preprocessing import limpiar_texto
from src.vectorizer import vectorizar_corpus
from src.naive_bayes import NaiveBayes


def cargar_modelo():
    base_dir = Path(__file__).resolve().parent.parent
    ruta_modelo = base_dir / "model" / "naive_bayes_model.pkl"
    return NaiveBayes.cargar_modelo(ruta_modelo)


def predecir_texto(texto):
    modelo = cargar_modelo()
    documento = limpiar_texto(texto)
    vector = vectorizar_corpus([documento], modelo.vocabulario)[0]
    return modelo.predecir(vector)


def obtener_categorias_modelo():
    modelo = cargar_modelo()
    return sorted(list(modelo.clases))