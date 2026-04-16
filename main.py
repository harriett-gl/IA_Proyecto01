from src.preprocessing import limpiar_texto

texto = "Hello, I have a problem with my internet connection!"
resultado = limpiar_texto(texto)

print(resultado)

from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus

textos = [
    "My internet is not working",
    "I want to cancel my subscription",
    "I have a billing problem",
    "The service is very bad"
]

documentos_procesados = [limpiar_texto(texto) for texto in textos]

vocabulario = construir_vocabulario(documentos_procesados)
vectores = vectorizar_corpus(documentos_procesados, vocabulario)

print("Documentos procesados:")
for doc in documentos_procesados:
    print(doc)

print("\nVocabulario:")
print(vocabulario)

print("\nVectores:")
for vector in vectores:
    print(vector)

    from src.preprocessing import limpiar_texto
    from src.vectorizer import construir_vocabulario, vectorizar_corpus
    from src.naive_bayes import NaiveBayes

    # Datos de ejemplo
    textos = [
        "My internet is not working",
        "I want to cancel my subscription",
        "I have a billing problem",
        "The service is very bad"
    ]

    etiquetas = [
        "soporte",
        "cancelacion",
        "facturacion",
        "queja"
    ]

    # Preprocesamiento
    docs = [limpiar_texto(t) for t in textos]

    # Vocabulario
    vocabulario = construir_vocabulario(docs)

    # Vectorización
    X = vectorizar_corpus(docs, vocabulario)

    # Entrenar modelo
    modelo = NaiveBayes()
    modelo.entrenar(X, etiquetas, vocabulario)

    # Probar predicción
    nuevo_texto = "I cannot connect to the internet"
    nuevo_doc = limpiar_texto(nuevo_texto)
    nuevo_vector = vectorizar_corpus([nuevo_doc], vocabulario)[0]

    prediccion = modelo.predecir(nuevo_vector)

    print("Texto:", nuevo_texto)
    print("Predicción:", prediccion)

    from src.metrics import accuracy, matriz_confusion, precision_recall_f1
    from src.kfold import kfold_split

    # K-Folds
    folds = kfold_split(X, etiquetas, k=2)  # usamos 2 solo para prueba

    y_true_total = []
    y_pred_total = []

    for i in range(len(folds)):
        test = folds[i]
        train = [item for j in range(len(folds)) if j != i for item in folds[j]]

        X_train = [x for x, _ in train]
        y_train = [y for _, y in train]

        X_test = [x for x, _ in test]
        y_test = [y for _, y in test]

        modelo = NaiveBayes()
        modelo.entrenar(X_train, y_train, vocabulario)

        for x, y_real in zip(X_test, y_test):
            y_pred = modelo.predecir(x)

            y_true_total.append(y_real)
            y_pred_total.append(y_pred)

    # Accuracy
    acc = accuracy(y_true_total, y_pred_total)
    print("\nAccuracy:", acc)

    # Matriz de confusión
    clases = set(etiquetas)
    matriz = matriz_confusion(y_true_total, y_pred_total, clases)

    print("\nMatriz de Confusión:")
    for c in matriz:
        print(c, matriz[c])

    # Métricas por clase
    print("\nMétricas por clase:")
    for c in clases:
        p, r, f1 = precision_recall_f1(matriz, c)
        print(f"{c} -> Precision: {p:.2f}, Recall: {r:.2f}, F1: {f1:.2f}")