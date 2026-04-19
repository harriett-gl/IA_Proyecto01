def accuracy_score(y_true, y_pred):
    if not y_true:
        return 0.0
    correctos = 0
    for real, pred in zip(y_true, y_pred):
        if real == pred:
            correctos += 1
    return correctos / len(y_true)


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
        fp = sum(cm[otra][clase] for otra in classes if otra != clase)
        fn = sum(cm[clase][otra] for otra in classes if otra != clase)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0 else 0.0
        )

        resultados[clase] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    return resultados


def macro_f1_score(y_true, y_pred, classes):
    resultados = precision_recall_f1_per_class(y_true, y_pred, classes)
    if not classes:
        return 0.0
    return sum(resultados[clase]["f1"] for clase in classes) / len(classes)