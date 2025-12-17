import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# =========================
# 1. Cargar dataset
# =========================
df = pd.read_csv("dataset.csv")

print("Dimensiones del dataset:")
print(df.shape)

print("\nTipos de datos:")
print(df.dtypes)

# =========================
# 2. Limpieza de datos
# =========================
print("\nValores nulos:")
print(df.isnull().sum())

# Eliminar valores nulos si existieran
df = df.dropna()

# =========================
# 3. Gráfica: distribución de la variable objetivo
# =========================
plt.figure()
sns.countplot(x="aprobado", data=df)
plt.title("Distribución de la variable objetivo")
plt.xlabel("Aprobado (0 = No, 1 = Sí)")
plt.ylabel("Cantidad")
plt.show()

# =========================
# 4. Codificación de variables categóricas
# =========================
encoder = LabelEncoder()
df["sexo"] = encoder.fit_transform(df["sexo"])

# =========================
# 5. Separar variables
# =========================
X = df.drop("aprobado", axis=1)
y = df["aprobado"]

# =========================
# 6. Normalización
# =========================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# 7. Train / Test (con stratify)
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# =========================
# 8. Modelo
# =========================
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# =========================
# 9. Predicciones
# =========================
y_pred = modelo.predict(X_test)

# =========================
# 10. Evaluación
# =========================
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
matriz = confusion_matrix(y_test, y_pred)

print("\nResultados del modelo:")
print("Accuracy:", accuracy)
print("Precisión:", precision)
print("Recall:", recall)
print("Matriz de confusión:")
print(matriz)

# =========================
# 11. Gráfica Matriz de Confusión
# =========================
plt.figure()
sns.heatmap(
    matriz,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No aprobado", "Aprobado"],
    yticklabels=["No aprobado", "Aprobado"]
)

plt.xlabel("Predicción")
plt.ylabel("Valor real")
plt.title("Matriz de Confusión - Regresión Logística")
plt.show()
