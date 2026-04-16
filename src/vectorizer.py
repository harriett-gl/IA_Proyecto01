def construir_vocabulario(documentos):
    """
    documentos: lista de listas de palabras
    devuelve: diccionario {palabra: indice}
    """
    vocabulario = {}
    indice = 0

    for doc in documentos:
        for palabra in doc:
            if palabra not in vocabulario:
                vocabulario[palabra] = indice
                indice += 1

    return vocabulario


def vectorizar_documento(documento, vocabulario):
    """
    documento: lista de palabras
    vocabulario: diccionario {palabra: indice}
    devuelve: lista de frecuencias
    """
    vector = [0] * len(vocabulario)

    for palabra in documento:
        if palabra in vocabulario:
            indice = vocabulario[palabra]
            vector[indice] += 1

    return vector


def vectorizar_corpus(documentos, vocabulario):
    """
    documentos: lista de listas de palabras
    vocabulario: diccionario {palabra: indice}
    devuelve: lista de vectores
    """
    return [vectorizar_documento(doc, vocabulario) for doc in documentos]