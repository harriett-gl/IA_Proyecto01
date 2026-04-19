from functools import lru_cache
from pathlib import Path

from src.preprocessing import limpiar_texto
from src.vectorizer import vectorizar_corpus
from src.naive_bayes import NaiveBayes


@lru_cache(maxsize=1)
def cargar_modelo():
    base_dir = Path(__file__).resolve().parent.parent
    ruta_modelo = base_dir / "model" / "naive_bayes_model.pkl"
    return NaiveBayes.cargar_modelo(ruta_modelo)


def predecir_texto(texto):
    modelo = cargar_modelo()
    documento = limpiar_texto(texto)
    vector = vectorizar_corpus([documento], modelo.vocabulario)[0]
    categoria, confianza, probabilidades = modelo.predecir_con_confianza(vector)

    probabilidades_ordenadas = dict(
        sorted(
            (
                (clase, round(prob * 100, 2))
                for clase, prob in probabilidades.items()
            ),
            key=lambda item: item[1],
            reverse=True
        )
    )

    return {
        "categoria": categoria,
        "confianza": confianza,
        "probabilidades": probabilidades_ordenadas,
    }


def obtener_categorias_modelo():
    modelo = cargar_modelo()
    return modelo.clases