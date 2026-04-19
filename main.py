from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus
from src.naive_bayes import NaiveBayes
from src.kfold import evaluate_kfold

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

nuevo_texto = "I cannot connect to the internet"
nuevo_doc = limpiar_texto(nuevo_texto)
nuevo_vector = vectorizar_corpus([nuevo_doc], vocabulario)[0]

prediccion = modelo.predecir(nuevo_vector)

print("Texto:", nuevo_texto)
print("Predicción:", prediccion)

classes = list(set(etiquetas))
resultados = evaluate_kfold(X, etiquetas, vocabulario, classes, k=4)

print("\nResultados K-Fold:")
for resultado in resultados:
    print(f"Fold {resultado['fold']}: Accuracy={resultado['accuracy']:.2f}, Macro F1={resultado['macro_f1']:.2f}")