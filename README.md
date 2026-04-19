# 📌 Proyecto 01 – Clasificador Inteligente de Solicitudes

## 🎓 Universidad Rafael Landívar
**Curso:** Inteligencia Artificial  
**Semestre:** Primer Semestre 2026

## 👥 Integrantes
- Harriett Guzmán
- Alejandro Ramos

---

# 📖 Descripción General

Este proyecto consiste en el desarrollo de un sistema inteligente capaz de clasificar automáticamente solicitudes de clientes dirigidas a una mesa de ayuda.

El sistema recibe un texto escrito por el usuario y determina a qué categoría pertenece la solicitud.

---

# 🎯 Objetivo del Proyecto

Aplicar conceptos fundamentales de Inteligencia Artificial:

- ✅ Clasificación de texto
- ✅ Preprocesamiento de datos
- ✅ Bag of Words
- ✅ Naive Bayes
- ✅ Flask

---

# 📂 Categorías del Sistema

- 🛠️ Soporte Técnico
- 💳 Facturación
- ❌ Cancelación
- ⚠️ Quejas

---

# 🛠️ Tecnologías Utilizadas

- 🐍 Python
- 🌐 Flask
- 🎨 HTML
- 🎨 CSS
- ⚙️ JavaScript

---

# 🚀 Instalación y Ejecución

## 1️⃣ Instalar Flask

```bash
pip install flask

---
# 📁 Estructura del Proyecto

```text
Proyecto 01/
│
├── app.py
├── main.py
├── README.md
│
├── model/
│   └── naive_bayes_model.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── naive_bayes.py
│   ├── metrics.py
│   ├── kfold.py
│   ├── train.py
│   └── predict.py
│
└── web/
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html
````

# ⚙️ ¿Cómo Funciona?

## 🧹 1. Preprocesamiento

Cada texto ingresado pasa por:

* Conversión a minúsculas
* Eliminación de símbolos
* Tokenización
* Eliminación de palabras vacías
* Stemming básico

---

## 📊 2. Vectorización

El texto se convierte en números usando **Bag of Words**.

Ejemplo:

```text
internet no funciona
```

↓

```text
[1,0,2,1,0]
```

---

## 🧠 3. Clasificación

Se utiliza el algoritmo **Naïve Bayes** para calcular la categoría más probable.

---

## 🌐 4. Interfaz Web

El usuario puede:

✅ Ingresar ticket
✅ Escribir asunto
✅ Describir problema
✅ Obtener respuesta automática

---

# 📐 Algoritmo Utilizado

## Naïve Bayes Multinomial

```text
P(clase|texto) = P(clase) * P(palabras|clase)
```

Incluye:

✅ Laplace Smoothing
✅ Logaritmos para evitar underflow
✅ Probabilidades por categoría

---

# 🚀 Instalación y Ejecución

## 1️⃣ Instalar Flask

```bash
pip install flask
```

---

## 2️⃣ Entrenar Modelo

```bash
python -m src.train
```

---

## 3️⃣ Ejecutar Página Web

```bash
python app.py
```

---

## 4️⃣ Abrir Navegador

🔗 [http://127.0.0.1:5001](http://127.0.0.1:5001)

---

# 💡 Ejemplos de Uso

## Entrada:

```text
No tengo internet desde ayer
```

## Resultado:

```text
🔧 Soporte Técnico
```

---

## Entrada:

```text
Me cobraron dos veces este mes
```

## Resultado:

```text
💳 Facturación
```

---

## Entrada:

```text
Quiero cancelar mi cuenta
```

## Resultado:

```text
❌ Cancelación
```

---

## Entrada:

```text
Muy mala atención del agente
```

## Resultado:

```text
⚠️ Queja
```

---

# 📈 Evaluación del Modelo

Se implementó validación cruzada **K-Fold** para medir:

📌 Accuracy
📌 Precision
📌 Recall
📌 F1 Score
📌 Macro F1

---

# ⭐ Ventajas del Sistema

✅ Automatiza tickets
✅ Reduce tiempo de respuesta
✅ Fácil de usar
✅ Código propio
✅ Escalable

---

# 🔮 Mejoras Futuras

* Más categorías
* Dataset real grande
* Dashboard administrativo
* API REST
* Base de datos
* Estadísticas en tiempo real

---

# 🏁 Conclusión

Este proyecto demuestra cómo aplicar Inteligencia Artificial real mediante clasificación automática de texto usando fundamentos matemáticos sólidos y una interfaz moderna.

Representa una solución útil para empresas que manejan grandes volúmenes de solicitudes.

---

# 👨‍💻 Autoría

Proyecto académico desarrollado para el curso de Inteligencia Artificial - Universidad Rafael Landívar.

```
```
