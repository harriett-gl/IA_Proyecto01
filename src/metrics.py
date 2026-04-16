def accuracy(y_true, y_pred):
    correctos = sum(1 for i in range(len(y_true)) if y_true[i] == y_pred[i])
    return correctos / len(y_true)


def matriz_confusion(y_true, y_pred, clases):
    matriz = {c: {c2: 0 for c2 in clases} for c in clases}

    for real, pred in zip(y_true, y_pred):
        matriz[real][pred] += 1

    return matriz


def precision_recall_f1(matriz, clase):
    TP = matriz[clase][clase]
    FP = sum(matriz[c][clase] for c in matriz if c != clase)
    FN = sum(matriz[clase][c] for c in matriz if c != clase)

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0
    )

    return precision, recall, f1


def accuracy_score(y_true, y_pred):
    correctos = 0
    for real, pred in zip(y_true, y_pred):
        if real == pred:
            correctos += 1
    return correctos / len(y_true) if y_true else 0


def confusion_matrix(y_true, y_pred, classes):
    matrix = {real: {pred: 0 for pred in classes} for real in classes}

    for real, pred in zip(y_true, y_pred):
        matrix[real][pred] += 1

    return matrix


def precision_recall_f1_per_class(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred, classes)
    resultados = {}

    for clase in classes:
        tp = cm[clase][clase]

        fp = 0
        for otra in classes:
            if otra != clase:
                fp += cm[otra][clase]

        fn = 0
        for otra in classes:
            if otra != clase:
                fn += cm[clase][otra]

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0

        resultados[clase] = {
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    return resultados


def macro_f1_score(y_true, y_pred, classes):
    resultados = precision_recall_f1_per_class(y_true, y_pred, classes)
    suma = 0

    for clase in classes:
        suma += resultados[clase]["f1"]

    return suma / len(classes) if classes else 0