from datasets import load_dataset
from src.preprocessing import limpiar_texto
from src.vectorizer import construir_vocabulario, vectorizar_corpus
from src.naive_bayes import NaiveBayes
from src.kfold import evaluate_kfold

dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset")
data = dataset["train"]

textos = []
etiquetas = []

for fila in data:
    textos.append(limpiar_texto(fila["instruction"]))
    etiquetas.append(fila["category"])

print("Total registros:", len(textos))

classes = sorted(list(set(etiquetas)))
print("Categorías:", classes)

vocabulario = construir_vocabulario(textos)
X = vectorizar_corpus(textos, vocabulario)

resultados = evaluate_kfold(X, etiquetas, vocabulario, classes, k=5)
promedio = sum(r["accuracy"] for r in resultados) / len(resultados)
print("Accuracy promedio:", round(promedio, 4))

modelo = NaiveBayes()
modelo.entrenar(X, etiquetas, vocabulario)
modelo.guardar_modelo("model/naive_bayes_model.pkl")

print("Modelo entrenado y guardado correctamente.")

# categorías
classes = sorted(list(set(etiquetas)))
print("Categorías:", classes)

# vocabulario
vocabulario = construir_vocabulario(textos)

# vectores
X = vectorizar_corpus(textos, vocabulario)

# evaluar KFold
resultados = evaluate_kfold(X, etiquetas, vocabulario, classes, k=5)

promedio = sum(r["accuracy"] for r in resultados) / len(resultados)
print("Accuracy promedio:", round(promedio, 4))

# entrenar modelo final
modelo = NaiveBayes()
modelo.entrenar(X, etiquetas, vocabulario)

# guardar modelo
modelo.guardar_modelo("model/naive_bayes_model.pkl")

print("Modelo entrenado y guardado correctamente.")