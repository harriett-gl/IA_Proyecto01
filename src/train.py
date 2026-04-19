import json
import random
from pathlib import Path

import pandas as pd

from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus
from src.naive_bayes import NaiveBayes
from src.kfold import evaluate_kfold
from src.metrics import accuracy_score, macro_f1_score


def entrenamiento_holdout(X, y, classes, alpha=1.0, seed=42):
    random.seed(seed)
    indices_por_clase = {}

    for i, etiqueta in enumerate(y):
        indices_por_clase.setdefault(etiqueta, []).append(i)

    train_indices = []
    test_indices = []

    for _, indices in indices_por_clase.items():
        random.shuffle(indices)
        corte = int(len(indices) * 0.8)
        train_indices.extend(indices[:corte])
        test_indices.extend(indices[corte:])

    X_train = [X[i] for i in train_indices]
    y_train = [y[i] for i in train_indices]
    X_test = [X[i] for i in test_indices]
    y_test = [y[i] for i in test_indices]

    modelo = NaiveBayes(alpha=alpha)
    modelo.entrenar(X_train, y_train, vocabulario)
    y_pred = [modelo.predecir(x) for x in X_test]

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "macro_f1": macro_f1_score(y_test, y_pred, classes),
    }


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    dataset_path = base_dir / "bitext_customer_support.csv"
    model_dir = base_dir / "model"
    model_dir.mkdir(exist_ok=True)

    df = pd.read_csv(dataset_path)
    df = df[["instruction", "category"]].dropna()

    documentos = [limpiar_texto(texto) for texto in df["instruction"].tolist()]
    etiquetas = df["category"].astype(str).tolist()
    classes = sorted(list(set(etiquetas)))

    vocabulario = construir_vocabulario(documentos, min_freq=2)
    X = vectorizar_corpus(documentos, vocabulario)

    resultados_kfold = evaluate_kfold(
        X, etiquetas, vocabulario, classes, k=5, alpha=1.0, seed=42
    )

    holdout = entrenamiento_holdout(X, etiquetas, classes, alpha=1.0, seed=42)

    modelo = NaiveBayes(alpha=1.0)
    modelo.entrenar(X, etiquetas, vocabulario)
    ruta_modelo = model_dir / "naive_bayes_model.pkl"
    modelo.guardar_modelo(ruta_modelo)

    resumen = {
        "dataset_rows": len(df),
        "num_classes": len(classes),
        "classes": classes,
        "vocab_size": len(vocabulario),
        "kfold_average_accuracy": round(resultados_kfold["average_accuracy"], 6),
        "kfold_average_macro_f1": round(resultados_kfold["average_macro_f1"], 6),
        "holdout_accuracy": round(holdout["accuracy"], 6),
        "holdout_macro_f1": round(holdout["macro_f1"], 6),
    }

    with open(model_dir / "metrics.json", "w", encoding="utf-8") as archivo:
        json.dump(
            {
                "summary": resumen,
                "kfold": resultados_kfold,
                "holdout": holdout,
            },
            archivo,
            ensure_ascii=False,
            indent=2,
        )

    print("Entrenamiento completado.")
    print(json.dumps(resumen, indent=2, ensure_ascii=False))