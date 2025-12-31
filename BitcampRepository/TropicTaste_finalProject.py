# ==========================================
# PROGETTO FINALE - CLASSIFICAZIONE FRUTTI
# TropicTaste Inc.
# ==========================================

# 1. IMPORT
import os
# 1.1 IMPORT LIBRERIE e CSV
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "fruits.csv")

df: DataFrame = pd.read_csv(DATA_PATH)

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 2. CARICAMENTO DATASET
df = pd.read_csv("fruits.csv")

print("\n--- PRIME RIGHE DEL DATASET ---")
print(df.head())

print("\n--- INFO DATASET ---")
print(df.info())

print("\n--- STATISTICHE DESCRITTIVE ---")
print(df.describe())


# 3. ANALISI ESPLORATIVA DEI DATI (EDA)

# Distribuzione del target
print("\n--- DISTRIBUZIONE DEI FRUTTI ---")
print(df["Frutto"].value_counts())

df["Frutto"].value_counts().plot(kind="bar")
plt.title("Distribuzione dei tipi di frutto")
plt.xlabel("Frutto")
plt.ylabel("Conteggio")
plt.tight_layout()
plt.show()


# Istogrammi delle feature numeriche
features = [
    "Peso (g)",
    "Diametro medio (mm)",
    "Lunghezza media (mm)",
    "Durezza buccia (1-10)",
    "Dolcezza (1-10)"
]

for feature in features:
    plt.hist(df[feature], bins=20)
    plt.title(f"Distribuzione di {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequenza")
    plt.tight_layout()
    plt.show()


# Scatter plot Peso vs Diametro
for fruit in df["Frutto"].unique():
    subset = df[df["Frutto"] == fruit]
    plt.scatter(
        subset["Peso (g)"],
        subset["Diametro medio (mm)"],
        label=fruit,
        alpha=0.7
    )

plt.title("Peso vs Diametro medio")
plt.xlabel("Peso (g)")
plt.ylabel("Diametro medio (mm)")
plt.legend()
plt.tight_layout()
plt.show()


# 4. PREPROCESSING

# Separazione feature e target
X = df.drop("Frutto", axis=1)
y = df["Frutto"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nDimensioni Training set:", X_train.shape)
print("Dimensioni Test set:", X_test.shape)


# 5. PIPELINE + MODELLO

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(random_state=42))
])


# 6. OTTIMIZZAZIONE IPERPARAMETRI (GRID SEARCH)

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 5, 10]
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\n--- MIGLIORI PARAMETRI ---")
print(grid_search.best_params_)

best_model = grid_search.best_estimator_


# 7. CROSS-VALIDATION SUL MODELLO OTTIMIZZATO

cv_scores = cross_val_score(
    best_model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)

print("\nAccuracy media Cross-Validation:", cv_scores.mean())
print("Deviazione standard:", cv_scores.std())


# 8. VALUTAZIONE SUL TEST SET

y_pred = best_model.predict(X_test)

print("\n--- ACCURACY TEST SET ---")
print(accuracy_score(y_test, y_pred))

print("\n--- CLASSIFICATION REPORT ---")
print(classification_report(y_test, y_pred))

print("\n--- CONFUSION MATRIX ---")
cm = confusion_matrix(y_test, y_pred)
print(cm)


# Visualizzazione Confusion Matrix
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.tight_layout()
plt.show()


# 9. IMPORTANZA DELLE FEATURE

feature_importances = best_model.named_steps["model"].feature_importances_

plt.barh(X.columns, feature_importances)
plt.title("Importanza delle Feature")
plt.xlabel("Importanza")
plt.tight_layout()
plt.show()


# 10. CONCLUSIONI FINALI

print("\n--- CONCLUSIONI ---")
print(
    "Il modello Random Forest ha mostrato un'elevata accuratezza "
    "nella classificazione dei frutti esotici.\n"
    "La standardizzazione delle feature e l'ottimizzazione degli "
    "iperparametri hanno migliorato la capacità di generalizzazione.\n"
    "Il sistema è adatto per l'automazione del processo di classificazione "
    "di TropicTaste Inc."
)
