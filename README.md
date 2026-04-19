# 📌 Proyecto 01 – Clasificador Inteligente de Solicitudes

## 🎓 Universidad Rafael Landívar
**Curso:** Inteligencia Artificial  
**Semestre:** Primer Semestre 2026

## 👥 Integrantes
- Harriett Guzmán
- Alejandro Ramos

---

# 📖 Descripción General

Este proyecto implementa un clasificador de texto para solicitudes de mesa de ayuda usando **Naïve Bayes Multinomial desarrollado desde cero**, sin depender de bibliotecas que resuelvan la clasificación automáticamente.

Ahora el sistema fue actualizado para usar el dataset **Bitext Customer Support**, que sí contiene etiquetas coherentes entre el texto y su categoría, tal como pide el proyecto del curso. Esto mejora drásticamente la calidad de predicción frente al dataset anterior.

---

# ✅ Dataset Utilizado

**Archivo usado:** `bitext_customer_support.csv`  
**Total de registros:** 26872  
**Número de categorías:** 11

## Categorías del modelo
- ACCOUNT
- CANCEL
- CONTACT
- DELIVERY
- FEEDBACK
- INVOICE
- ORDER
- PAYMENT
- REFUND
- SHIPPING
- SUBSCRIPTION

---

# 🛠️ Tecnologías Utilizadas

- 🐍 Python
- 🌐 Flask
- 🎨 HTML
- 🎨 CSS
- 🧠 Naïve Bayes Multinomial
- 📊 Validación K-Fold manual
- 💾 Pickle para guardar el modelo

---

# 🧹 Preprocesamiento Aplicado

El texto pasa por varias etapas antes de clasificarse:

- Conversión a minúsculas
- Eliminación de placeholders como `{Order Number}`
- Eliminación de caracteres especiales
- Normalización de acentos
- Eliminación de stopwords en inglés y español
- Stemming simple
- Generación de bigramas
- Normalización básica de términos frecuentes en español hacia tokens útiles del modelo

Esto permite que el sistema trabaje mejor con entradas reales de usuario y con el dataset actualizado.

---

# 📊 Representación del Texto

Se utiliza la técnica **Bag of Words** construida manualmente.

Además, se aplica un filtro de frecuencia mínima para evitar ruido en el vocabulario.

**Tamaño final del vocabulario:** 5058 palabras

---

# 🧠 Algoritmo Utilizado

## Naïve Bayes Multinomial

El modelo calcula:

- Probabilidades a priori por clase
- Probabilidades condicionales por palabra
- Laplace Smoothing
- Suma de logaritmos para evitar underflow numérico

También se añadió el cálculo de **probabilidades normalizadas por clase**, para mostrar en la web el porcentaje de confianza o fiabilidad de cada predicción.

---

# 📈 Resultados del Modelo

## Evaluación K-Fold manual
- **Accuracy promedio:** 99.43%
- **Macro F1 promedio:** 99.43%

## Evaluación Holdout
- **Accuracy holdout:** 99.57%
- **Macro F1 holdout:** 99.53%

## Conclusión de rendimiento
Con el dataset actualizado y las mejoras aplicadas, el sistema supera el **99% de accuracy**, por lo que el cambio de dataset sí resolvió el problema principal de calidad del modelo.

---

# 🌐 Funcionalidades de la Web

La aplicación web permite:

- Generar un ID de ticket automáticamente
- Ingresar asunto
- Ingresar descripción del problema
- Clasificar el ticket en tiempo real
- Mostrar la **categoría predicha**
- Mostrar el **porcentaje de fiabilidad**
- Mostrar la **distribución de probabilidades por categoría**

---

# 📁 Estructura del Proyecto

```text
Proyecto 01/
│
├── app.py
├── train.py
├── bitext_customer_support.csv
├── README.md
│
├── model/
│   ├── naive_bayes_model.pkl
│   └── metrics.json
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── naive_bayes.py
│   ├── metrics.py
│   ├── kfold.py
│   └── predict.py
│
└── web/
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html
```

---

# 🚀 Instalación y Ejecución

## 1️⃣ Instalar dependencias

```bash
pip install flask pandas
```

## 2️⃣ Entrenar el modelo con el dataset nuevo

```bash
python train.py
```

Esto generará:

- `model/naive_bayes_model.pkl`
- `model/metrics.json`

## 3️⃣ Ejecutar la aplicación web

```bash
python app.py
```

## 4️⃣ Abrir en el navegador

```text
http://127.0.0.1:5001
```

---

# 💡 Ejemplos de uso

## Entrada
**Asunto:** Refund request  
**Descripción:** I want my money back because I returned the item.

## Salida esperada
- Categoría: `REFUND`
- Confianza: porcentaje mostrado por la web

---

## Entrada
**Asunto:** Late package  
**Descripción:** My package has not arrived and the tracking has not changed.

## Salida esperada
- Categoría: `SHIPPING` o `DELIVERY`

---

## Entrada
**Asunto:** Wrong invoice  
**Descripción:** I was charged the wrong amount on my invoice.

## Salida esperada
- Categoría: `INVOICE` o `PAYMENT`

---

# ⭐ Mejoras realizadas en esta actualización

- Se reemplazó el dataset anterior por uno semánticamente correcto
- Se actualizó el entrenamiento para leer el archivo CSV local
- Se mejoró el preprocesamiento
- Se cambió la vectorización a una forma más eficiente
- Se añadió cálculo de probabilidades por clase
- Se añadió porcentaje de fiabilidad en la interfaz web
- Se agregaron métricas reales guardadas en `metrics.json`
- Se actualizó el README con resultados actuales

---

# 🏁 Conclusión

Este proyecto ahora cumple mejor con los requisitos del curso, porque:

- usa un dataset adecuado,
- mantiene la implementación manual del modelo,
- evalúa el sistema con K-Fold,
- guarda el modelo entrenado,
- y muestra resultados entendibles para el usuario final.

La actualización permitió obtener un clasificador mucho más confiable y visualmente más completo.

---

# 👨‍💻 Autoría

Proyecto académico desarrollado para el curso de Inteligencia Artificial – Universidad Rafael Landívar.
