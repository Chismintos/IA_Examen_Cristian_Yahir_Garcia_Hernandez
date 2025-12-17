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

## 8. Resultados y explicación final

Los resultados obtenidos muestran que **sí fue posible predecir y clasificar el comportamiento académico de los estudiantes**.

El modelo logró identificar patrones entre las variables demográficas, educativas y las calificaciones, permitiendo predecir si un estudiante aprobará o no. Aunque el dataset es de tamaño reducido, el modelo cumple correctamente el objetivo académico del proyecto.

---

## 9. Problemas presentados

El principal problema fue el tamaño limitado del dataset, lo que inicialmente provocó métricas indefinidas. Este inconveniente se solucionó aplicando una división estratificada de los datos.

---

## 10. Posibles mejoras

* Uso de un dataset más grande
* Comparación con otros modelos (Árboles de Decisión, KNN)
* Ajuste de hiperparámetros
* Inclusión de más variables relevantes

---

## 11. Instrucciones de ejecución

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar el programa:

```bash
python modelo.py
```

---

## 12. Conclusión

Este proyecto demuestra la aplicación completa de un flujo de Machine Learning para la clasificación de un comportamiento académico, cumpliendo todos los requisitos del examen de recuperación.
