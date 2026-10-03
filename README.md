# Clasificación de defectos en palta Hass mediante visión por computadora

## Proyecto

**Diferenciación visual entre russet y lesiones compatibles con picadura de insecto en palta Hass mediante aprendizaje profundo multivista.**

## Objetivo

Desarrollar y evaluar modelos de aprendizaje profundo para diferenciar visualmente:

- RUSSET
- PICADURA

## Características de las imágenes

Cada archivo representa una sola palta.

Cada imagen está compuesta por tres franjas horizontales correspondientes a tres cámaras ubicadas en diferentes ángulos.

Dentro de cada franja se observan varias vistas de la misma fruta debido a su rotación durante el proceso de inspección.

Por lo tanto, la unidad experimental es la palta completa y no cada vista individual.

## Metodología

1. Análisis exploratorio de datos (EDA).
2. Control de calidad y distribución del dataset.
3. División Train / Validation / Test.
4. Modelo baseline utilizando la imagen completa.
5. Evaluación individual de cámaras.
6. Modelo multivista.
7. Comparación experimental.

## Baseline

Imagen completa → MobileNetV3Small → Clasificación

El baseline permitirá establecer una referencia antes de utilizar explícitamente las tres cámaras.

## Modelo propuesto

Cámara 1 ─┐
Cámara 2 ─┼─ CNN compartida → Fusión → Clasificación
Cámara 3 ─┘

## Evaluación

Se utilizarán:

- Accuracy
- Balanced Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión

Se dará especial atención al desempeño de la clase PICADURA.

## Estado actual

- Dataset organizado.
- Train / Validation / Test definidos.
- EDA en desarrollo.
- Baseline en desarrollo.
- Modelo multivista pendiente.
