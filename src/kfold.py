import random
from collections import defaultdict

from src.naive_bayes import NaiveBayes
from src.metrics import (
    accuracy_score,
    macro_f1_score,
    precision_recall_f1_per_class,
)


def kfold_split_estratificado(X, y, k=5, seed=42):
    random.seed(seed)
    indices_por_clase = defaultdict(list)

    for i, etiqueta in enumerate(y):
        indices_por_clase[etiqueta].append(i)

    folds_indices = [[] for _ in range(k)]

    for _, indices in indices_por_clase.items():
        random.shuffle(indices)
        for posicion, indice in enumerate(indices):
            folds_indices[posicion % k].append(indice)

    folds = []
    for fold in folds_indices:
        folds.append([(X[i], y[i]) for i in fold])

    return folds


def evaluate_kfold(X, y, vocabulario, classes, k=5, alpha=1.0, seed=42):
    folds = kfold_split_estratificado(X, y, k=k, seed=seed)
    resultados = []

    for i in range(k):
        test_fold = folds[i]
        train_folds = []

        for j in range(k):
            if j != i:
                train_folds.extend(folds[j])

        X_train = [x for x, _ in train_folds]
        y_train = [label for _, label in train_folds]
        X_test = [x for x, _ in test_fold]
        y_test = [label for _, label in test_fold]

        modelo = NaiveBayes(alpha=alpha)
        modelo.entrenar(X_train, y_train, vocabulario)

        y_pred = [modelo.predecir(x) for x in X_test]

        resultados.append({
            "fold": i + 1,
            "accuracy": accuracy_score(y_test, y_pred),
            "macro_f1": macro_f1_score(y_test, y_pred, classes),
            "per_class": precision_recall_f1_per_class(y_test, y_pred, classes),
        })

    promedio_accuracy = sum(r["accuracy"] for r in resultados) / len(resultados)
    promedio_macro_f1 = sum(r["macro_f1"] for r in resultados) / len(resultados)

    return {
        "folds": resultados,
        "average_accuracy": promedio_accuracy,
        "average_macro_f1": promedio_macro_f1,
    }

