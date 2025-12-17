# Examen de Recuperación – Inteligencia Artificial

## Datos del estudiante

**Nombre:** Cristian Yahir Garcia Hernandez
**Materia:** Inteligencia Artificial
**Tipo de evaluación:** Examen de recuperación
**Lenguaje:** Python 3.8+

---

## 1. Objetivo del proyecto

El objetivo de este proyecto es **construir un modelo de Inteligencia Artificial capaz de clasificar un comportamiento académico**, específicamente **predecir si un estudiante aprueba o no una evaluación general**, utilizando información demográfica, educativa y resultados académicos.

El problema se aborda como un **problema de clasificación binaria**, donde:

* `1` representa que el estudiante **aprueba**
* `0` representa que el estudiante **no aprueba**

---

## 2. Dataset utilizado

Se utilizó un **dataset académico de estudiantes**, el cual contiene información demográfica, nivel educativo de los padres, preparación previa y calificaciones obtenidas.

### Variables del dataset:

* `Genero`: Género del estudiante
* `Etnia`: Grupo étnico
* `Nivel educativo de los padres`: Nivel académico máximo alcanzado por los padres
* `Examen de preparacion`: Indica si el estudiante completó un curso de preparación
* `Matematicas`: Calificación obtenida en matemáticas
* `Lectura`: Calificación obtenida en lectura
* `Escritura`: Calificación obtenida en escritura

El dataset fue cargado utilizando la librería **pandas**.

Pagina de origen del dataset: https://www.kaggle.com/datasets/ernestohinojosa/estudiantes?resource=download&select=Estudiantes.csv


---

## 3. Comportamiento a predecir

A partir de las calificaciones de matemáticas, lectura y escritura, se calculó un **promedio general**.

Se creó una variable objetivo llamada `aprobado`, definida de la siguiente manera:

* Promedio ≥ 60 → **Aprobado (1)**
* Promedio < 60 → **No aprobado (0)**

De esta forma, el modelo aprende a **clasificar el comportamiento académico del estudiante**.

---

## 4. Preprocesamiento de datos

Se aplicaron las siguientes técnicas de preprocesamiento:

* Verificación y eliminación de valores nulos
* Codificación de variables categóricas mediante `LabelEncoder`
* Normalización de variables numéricas usando `StandardScaler`

---

## 5. División de los datos

El dataset fue dividido en:

* 70% para entrenamiento
* 30% para prueba

Se utilizó una división estratificada para asegurar que ambas clases estuvieran representadas.

---

## 6. Modelo de Machine Learning

Se utilizó el modelo de **Regresión Logística**, adecuado para problemas de clasificación binaria y visto en clase.

### Justificación del modelo:

* Sencillo y eficiente
* Fácil de interpretar
* Buen desempeño con datasets pequeños
* Ideal para clasificación binaria

---

## 7. Evaluación del modelo

El desempeño del modelo se evaluó utilizando las siguientes métricas:

* Accuracy
* Precisión
* Recall
* Matriz de confusión

Además, se generaron gráficas para analizar visualmente los resultados.

---

## 8. Resultados 

Después de realizar el preprocesamiento de los datos y entrenar el modelo de **Regresión Logística**, se obtuvieron los siguientes resultados.

---

### 🔹 Distribución de aprobados y no aprobados

Se generó una gráfica de barras que muestra la distribución de estudiantes **aprobados (1)** y **no aprobados (0)** dentro del dataset.

📌 **Evidencia:**  
Gráfica de distribución de aprobados y no aprobados.

Esta gráfica permite observar la cantidad de estudiantes en cada clase, lo cual es importante para entender el comportamiento del dataset antes del entrenamiento del modelo.

---

### 🔹 Evaluación del modelo

El modelo fue evaluado utilizando el conjunto de prueba, obteniendo las siguientes métricas:

- **Accuracy:** 98.33%  
- **Precisión:** 98.60%  
- **Recall:** 99.06%

Estos valores indican que el modelo tiene un **alto desempeño**, logrando clasificar correctamente la gran mayoría de los casos.

---

### 🔹 Matriz de confusión

Se generó la siguiente matriz de confusión para analizar con mayor detalle las predicciones realizadas por el modelo:

| Valor real \ Predicción | No aprobado | Aprobado |
|------------------------|-------------|----------|
| **No aprobado** | 83 | 3 |
| **Aprobado** | 2 | 212 |

📌 **Evidencia:**  
Matriz de confusión del modelo de Regresión Logística.

**Interpretación:**
- El modelo clasificó correctamente **83 estudiantes no aprobados**.
- Clasificó correctamente **212 estudiantes aprobados**.
- Solo se presentaron **5 errores en total**, lo que demuestra una muy buena capacidad de clasificación.

---

### 🔹 Análisis final de resultados

Con base en los resultados obtenidos, se concluye que **sí fue posible clasificar el comportamiento de los estudiantes (aprobado / no aprobado)** utilizando información académica y demográfica.

El modelo de **Regresión Logística** mostró ser adecuado para este problema debido a su simplicidad, buen rendimiento y facilidad de interpretación.

---

### ✅ Conclusión de los resultados

El modelo entrenado cumple con el objetivo del proyecto, logrando **predecir correctamente el estado de aprobación de los estudiantes**, cumpliendo con todos los requisitos establecidos en el examen de recuperación.

# 9 Explicación final

Los resultados obtenidos muestran que **sí fue posible predecir y clasificar el comportamiento académico de los estudiantes**.

El modelo logró identificar patrones entre las variables demográficas, educativas y las calificaciones, permitiendo predecir si un estudiante aprobará o no. Aunque el dataset es de tamaño reducido, el modelo cumple correctamente el objetivo académico del proyecto.

---

## 10. Problemas presentados

El principal problema fue el tamaño limitado del dataset, lo que inicialmente provocó métricas indefinidas. Este inconveniente se solucionó aplicando una división estratificada de los datos.

---

## 11. Posibles mejoras

* Uso de un dataset más grande
* Comparación con otros modelos (Árboles de Decisión, KNN)
* Ajuste de hiperparámetros
* Inclusión de más variables relevantes

---

## 12. Instrucciones de ejecución

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar el programa:

```bash
python modelo.py
```

---

## 13. Conclusión

Este proyecto demuestra la aplicación completa de un flujo de Machine Learning para la clasificación de un comportamiento académico, cumpliendo todos los requisitos del examen de recuperación.
