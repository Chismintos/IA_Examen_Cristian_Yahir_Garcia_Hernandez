# Examen de Recuperación – Inteligencia Artificial

## Datos del estudiante

**Nombre:** Cristian Yahir Garcia Hernandez
**Materia:** Inteligencia Artificial
**Tipo de evaluación:** Examen de recuperación
**Lenguaje:** Python 3.8+

---

## 1. Objetivo del proyecto

El objetivo de este proyecto es **construir un modelo de Inteligencia Artificial capaz de clasificar un comportamiento**, específicamente **predecir si un estudiante aprueba o no una materia** a partir de información académica previa.

Este problema corresponde a un **problema de clasificación binaria**, donde:

* `1` representa que el estudiante **aprueba**
* `0` representa que el estudiante **no aprueba**

---

## 2. Descripción del comportamiento predicho

Sí, **el comportamiento fue correctamente clasificado**.

El modelo analiza variables como:

* Horas de estudio
* Porcentaje de asistencia
* Sexo
* Promedio previo

A partir de estos datos, el modelo aprende patrones que le permiten **clasificar el comportamiento del estudiante** y predecir si aprobará o no la materia. Esto cumple directamente con el objetivo del examen de **predecir un comportamiento usando IA**.

---

## 3. Dataset utilizado

El dataset contiene 10 registros y 5 columnas:

* `horas_estudio`: Número de horas dedicadas al estudio
* `asistencia`: Porcentaje de asistencia a clases
* `sexo`: Variable categórica (M / F)
* `promedio`: Promedio académico previo
* `aprobado`: Variable objetivo (0 = No aprobado, 1 = Aprobado)

El dataset fue cargado utilizando la librería **pandas**.

---

## 4. Análisis inicial del dataset

Se realizaron las siguientes acciones iniciales:

* Visualización de las dimensiones del dataset
* Revisión de los tipos de datos
* Verificación de valores nulos

El análisis mostró que el dataset no contenía valores nulos, por lo que no fue necesario imputarlos.

---

## 5. Preprocesamiento de datos

Se aplicaron varias técnicas de preprocesamiento:

### 5.1 Limpieza de datos

* Eliminación de valores nulos en caso de existir

### 5.2 Codificación de variables categóricas

* La variable `sexo` fue transformada a valores numéricos utilizando `LabelEncoder`

### 5.3 Normalización

* Se aplicó `StandardScaler` para normalizar las variables numéricas
* Esto permitió que todas las características estuvieran en la misma escala

---

## 6. División de los datos

Los datos fueron divididos en:

* **70% entrenamiento**
* **30% prueba**

Se utilizó una división **estratificada**, garantizando que ambas clases (aprobado y no aprobado) estuvieran presentes en ambos conjuntos.

---

## 7. Modelo de Machine Learning utilizado

Se utilizó el modelo de **Regresión Logística**, el cual fue visto en clase y es adecuado para problemas de clasificación binaria.

### Justificación del modelo:

* Es simple y eficiente
* Funciona bien con datasets pequeños
* Permite interpretar fácilmente los resultados
* Es ideal para clasificación de dos clases

---

## 8. Entrenamiento del modelo

El modelo fue entrenado utilizando el conjunto de entrenamiento y la librería **scikit-learn**.

Durante el entrenamiento, el modelo aprendió la relación entre las variables de entrada y el comportamiento objetivo (aprobado / no aprobado).

---

## 9. Evaluación del modelo

El modelo fue evaluado utilizando las siguientes métricas:

* **Accuracy**: Proporción de predicciones correctas
* **Precisión**: Qué tan confiables son las predicciones positivas
* **Recall**: Capacidad del modelo para identificar correctamente a los aprobados
* **Matriz de confusión**: Visualización de aciertos y errores del modelo

También se generaron gráficas:

* Distribución de la variable objetivo
* Matriz de confusión visual

---

## 10. Explicación final de los resultados

Los resultados obtenidos indican que **sí fue posible clasificar y predecir el comportamiento de los estudiantes**.

El modelo logró identificar patrones entre las variables académicas y el resultado final, permitiendo predecir correctamente si un estudiante aprobaría o no. Aunque el dataset es pequeño, el modelo funciona correctamente y cumple el objetivo del proyecto.

La matriz de confusión muestra cómo el modelo distingue entre estudiantes aprobados y no aprobados, y las métricas indican un desempeño aceptable para un ejercicio académico.

---

## 11. Problemas presentados durante el desarrollo

Uno de los principales problemas fue el tamaño reducido del dataset, lo cual inicialmente provocó métricas indefinidas. Este problema se solucionó utilizando una división estratificada de los datos, asegurando la representación de ambas clases.

---

## 12. Posibles mejoras

Si se contara con más tiempo o información, se podrían implementar las siguientes mejoras:

* Usar un dataset más grande
* Probar otros modelos como Árboles de Decisión o KNN
* Ajustar hiperparámetros
* Agregar más variables relevantes

---

## 13. Instrucciones para ejecutar el proyecto

1. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar el programa:

```bash
python modelo.py
```

---

## 14. Conclusión

Este proyecto cumple con todos los requisitos del examen de recuperación y demuestra la aplicación completa de un flujo de Machine Learning: carga de datos, preprocesamiento, entrenamiento, evaluación y visualización. El comportamiento fue correctamente clasificado utilizando técnicas de Inteligencia Artificial.
