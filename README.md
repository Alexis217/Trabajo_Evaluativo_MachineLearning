# 🍷 Clasificador de calidad del vino

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)](https://fastapi.tiangolo.com/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-📝-orange)](https://jupyter.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-💎-yellow)](https://scikit-learn.org/stable/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)

Un sistema completo para **predecir la calidad de vino tinto** (buena o mala) usando Machine Learning, API REST con **FastAPI**, y una web liviana en HTML/JS.

---

## 🧠 Model Training jupyter notebook

- Preproceso de datos con `pandas`, `sklearn` y `matplolib`.
- Convertir la columna `quality` en binaria (`quality_binary`).
- Entrenamiento de un **árbol de decisión** y evaluarlo.
- Exportacion de el modelo con `joblib.dump()`.

---

## 🛠️ Backend – FastAPI

- Ruta `POST /predict` que recibe un JSON con 11 parámetros químicos y devuelve:
  - `predicción`: 0 o 1
  - `mensaje`: “Mala calidad” o “Buena calidad”

---

## 💻 Frontend – index.html

- Formulario grid responsive para ingresar los valores químicos.
- Botón de predicción que llama a `/predict` vía `fetch`.
- Muestra resultado con emojis ✅ o ❌, y mensajes claros.
- Diseño moderno con CSS (tarjeta, sombras, fuentes limpias).

---

## ⚙️ Uso

1. **Entrenar modelo** (si necesitás actualizarlo):

   ```
   pip install pandas scikit-learn matplolib
   ```

   Abrí `main.ipynb` y ejecutá todo.

2. **Levantar API**:

   ```
   pip install fastapi uvicorn
   ```

   uvicorn main:app --reload

3. **Abrir frontend**:

   En `index.html`, abrir con Live Server.

4. **Usar la interfaz**:

   Ingresás valores → clic en “Predecir Calidad” → obtenés resultado al instante.

---

## 🧩 Requisitos

- Python 3.x
- Navegador moderno para el frontend.

---

## 🧑‍💻 Autores

Gaston Espinola · [Github](https://github.com/GastonEspinola2)

Alexis Albarenga · [Github](https://github.com/Alexis217)

---
