import math
import pickle
from collections import defaultdict


class NaiveBayes:
    def __init__(self):
        self.clases = set()
        self.vocabulario = {}
        self.prior = {}
        self.likelihood = {}
        self.total_palabras_clase = {}
        self.tamano_vocabulario = 0

    def entrenar(self, X, y, vocabulario):
        self.clases = set(y)
        self.vocabulario = vocabulario
        self.tamano_vocabulario = len(vocabulario)

        conteo_clases = defaultdict(int)
        conteo_palabras = {
            clase: [0] * self.tamano_vocabulario for clase in self.clases
        }

        for i in range(len(X)):
            clase = y[i]
            conteo_clases[clase] += 1

            for j in range(len(X[i])):
                conteo_palabras[clase][j] += X[i][j]

        total_docs = len(y)
        for clase in self.clases:
            self.prior[clase] = conteo_clases[clase] / total_docs

        for clase in self.clases:
            self.total_palabras_clase[clase] = sum(conteo_palabras[clase])

        self.likelihood = {}
        for clase in self.clases:
            self.likelihood[clase] = []

            for j in range(self.tamano_vocabulario):
                prob = (
                    conteo_palabras[clase][j] + 1
                ) / (
                    self.total_palabras_clase[clase] + self.tamano_vocabulario
                )
                self.likelihood[clase].append(prob)

    def predecir(self, vector):
        resultados = {}

        for clase in self.clases:
            log_prob = math.log(self.prior[clase])

            for i in range(len(vector)):
                if vector[i] > 0:
                    log_prob += vector[i] * math.log(self.likelihood[clase][i])

            resultados[clase] = log_prob

        return max(resultados, key=resultados.get)

    def guardar_modelo(self, ruta):
        with open(ruta, "wb") as archivo:
            pickle.dump(self, archivo)

    @staticmethod
    def cargar_modelo(ruta):
        with open(ruta, "rb") as archivo:
            return pickle.load(archivo)