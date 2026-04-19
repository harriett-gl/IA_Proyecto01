import random
from src.naive_bayes import NaiveBayes
from src.metrics import (
    accuracy_score,
    precision_recall_f1_per_class,
    macro_f1_score,
    confusion_matrix
)

def kfold_split(X, y, k=5, seed=42):
    datos = list(zip(X, y))
    random.seed(seed)
    random.shuffle(datos)

    n = len(datos)
    fold_size = n // k
    sobrante = n % k

    folds = []
    inicio = 0

    for i in range(k):
        extra = 1 if i < sobrante else 0
        fin = inicio + fold_size + extra
        folds.append(datos[inicio:fin])
        inicio = fin

    return folds


def evaluate_kfold(X, y, vocabulario, classes, k=5):
    folds = kfold_split(X, y, k)

    resultados = []

    for i in range(k):
        test_fold = folds[i]
        train_folds = []

        for j in range(k):
            if j != i:
                train_folds.extend(folds[j])

        X_train = [x for x, label in train_folds]
        y_train = [label for x, label in train_folds]

        X_test = [x for x, label in test_fold]
        y_test = [label for x, label in test_fold]

        modelo = NaiveBayes()
        modelo.entrenar(X_train, y_train, vocabulario)

        y_pred = [modelo.predecir(x) for x in X_test]

        acc = accuracy_score(y_test, y_pred)
        per_class = precision_recall_f1_per_class(y_test, y_pred, classes)
        macro_f1 = macro_f1_score(y_test, y_pred, classes)
        cm = confusion_matrix(y_test, y_pred, classes)

        resultados.append({
            "fold": i + 1,
            "accuracy": acc,
            "macro_f1": macro_f1,
            "per_class": per_class,
            "confusion_matrix": cm
        })

    return resultados
