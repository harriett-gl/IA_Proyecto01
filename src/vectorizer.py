def construir_vocabulario(documentos, min_freq=2):
    frecuencias = {}

    for doc in documentos:
        for palabra in doc:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    vocabulario = {}
    indice = 0

    for palabra, freq in frecuencias.items():
        if freq >= min_freq:
            vocabulario[palabra] = indice
            indice += 1

    return vocabulario


def vectorizar_documento(documento, vocabulario):
    vector = {}

    for palabra in documento:
        if palabra in vocabulario:
            indice = vocabulario[palabra]
            vector[indice] = vector.get(indice, 0) + 1

    return vector


def vectorizar_corpus(documentos, vocabulario):
    return [vectorizar_documento(doc, vocabulario) for doc in documentos]