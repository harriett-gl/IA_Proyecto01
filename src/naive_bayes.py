import math
import pickle


class NaiveBayes:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.clases = []
        self.vocabulario = {}
        self.prior = {}
        self.conteo_palabras = {}
        self.total_palabras_clase = {}
        self.tamano_vocabulario = 0

    def entrenar(self, X, y, vocabulario):
        self.clases = sorted(list(set(y)))
        self.vocabulario = vocabulario
        self.tamano_vocabulario = len(vocabulario)

        conteo_clases = {clase: 0 for clase in self.clases}
        self.conteo_palabras = {clase: {} for clase in self.clases}
        self.total_palabras_clase = {clase: 0 for clase in self.clases}

        for vector, clase in zip(X, y):
            conteo_clases[clase] += 1

            for indice, frecuencia in vector.items():
                self.conteo_palabras[clase][indice] = (
                    self.conteo_palabras[clase].get(indice, 0) + frecuencia
                )
                self.total_palabras_clase[clase] += frecuencia

        total_docs = len(y)
        self.prior = {
            clase: conteo_clases[clase] / total_docs
            for clase in self.clases
        }

    def _log_probabilidad_clase(self, vector, clase):
        log_prob = math.log(self.prior[clase])
        denominador = (
            self.total_palabras_clase[clase] +
            self.alpha * self.tamano_vocabulario
        )

        for indice, frecuencia in vector.items():
            numerador = self.conteo_palabras[clase].get(indice, 0) + self.alpha
            log_prob += frecuencia * math.log(numerador / denominador)

        return log_prob

    def predecir_probabilidades(self, vector):
        puntajes = {
            clase: self._log_probabilidad_clase(vector, clase)
            for clase in self.clases
        }

        max_log = max(puntajes.values())
        exp_scores = {
            clase: math.exp(valor - max_log)
            for clase, valor in puntajes.items()
        }
        suma_exp = sum(exp_scores.values())

        return {
            clase: exp_scores[clase] / suma_exp
            for clase in self.clases
        }

    def predecir(self, vector):
        probabilidades = self.predecir_probabilidades(vector)
        mejor_clase = max(probabilidades, key=probabilidades.get)
        return mejor_clase

    def predecir_con_confianza(self, vector):
        probabilidades = self.predecir_probabilidades(vector)
        mejor_clase = max(probabilidades, key=probabilidades.get)
        confianza = probabilidades[mejor_clase] * 100
        return mejor_clase, round(confianza, 2), probabilidades

    def guardar_modelo(self, ruta):
        with open(ruta, "wb") as archivo:
            pickle.dump(self, archivo)

    @staticmethod
    def cargar_modelo(ruta):
        with open(ruta, "rb") as archivo:
            return pickle.load(archivo)