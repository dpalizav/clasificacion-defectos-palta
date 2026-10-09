# Clasificación de defectos en palta Hass mediante visión por computadora

## Descripción
Proyecto de clasificación supervisada de imágenes para diferenciar RUSSET y lesiones etiquetadas PICADURA en palta Hass. Según la documentación inicial, cada archivo representa una palta completa y contiene tres franjas horizontales de cámaras, con distintas vistas por rotación. Las vistas de una fruta no deben tratarse como muestras independientes.

## Objetivo
Auditar los datos y desarrollar posteriormente un clasificador con **ResNet50 mediante Transfer Learning**, evaluado con particiones independientes por fruto/grupo. Pipeline: datos → particiones → preprocesamiento → modelo → predicción → métricas. En esta etapa se ejecuta exclusivamente el EDA.

## Autor
Luis Daniel Paliza Vilca

GitHub: [dpalizav](https://github.com/dpalizav)

## Dataset
En la inspección local, `DATASET_PALTA` se encuentra **junto al repositorio**, no dentro. El notebook detecta una carpeta con ese nombre dentro o junto al repositorio y exige seleccionar una ruta relativa explícita si hay dos copias. Las imágenes no están incluidas en Git; clonar el repositorio no descarga el dataset.

```text
carpeta_de_trabajo/
├── DATASET_PALTA/
│   ├── train/{PICADURA,RUSSET}/
│   ├── validation/{PICADURA,RUSSET}/
│   └── test/{PICADURA,RUSSET}/
└── clasificacion-defectos-palta/  # localmente: Proyecto tesis
    └── 4. entrenamiento/01_EDA.ipynb
```

Resultados de la ejecución del 9 de octubre de 2026:

| Partición | PICADURA | RUSSET | Total | Porcentaje |
|---|---:|---:|---:|---:|
| train | 497 | 77 | 574 | 69,24 % |
| validation | 107 | 21 | 128 | 15,44 % |
| test | 106 | 21 | 127 | 15,32 % |
| Total | 710 | 119 | 829 | 100 % |

- 829 imágenes TIFF RGB legibles; 0 corruptas y 0 archivos no reconocidos como imágenes en esta carpeta.
- PICADURA: 85,65 %; RUSSET: 14,35 %. Razón mayoritaria/minoritaria: **5,97:1**.
- 822 tamaños diferentes: ancho 1434–2429 px y alto 577–1068 px. Se señalaron 37 archivos por resolución/aspecto atípico según la regla IQR; esto no significa que sean inválidos.
- **Dos pares exactos entre particiones**, confirmados por SHA-256 de archivos y píxeles: uno train–validation y otro train–test. El segundo tiene etiquetas contradictorias.
- 0 candidatos adicionales con dHash de 64 bits y distancia ≤4. Este resultado no descarta semejanzas no detectadas ni vistas del mismo fruto.
- Diferencia máxima de proporción de clase entre particiones: 3,12 puntos porcentuales; de brillo medio: 1,89/255. Son diferencias exploratorias entre particiones, no drift temporal demostrado.

La fuente/procedencia, licencia de uso y validación experta de etiquetas no están documentadas en los archivos inspeccionados. Se deben completar antes de publicar o distribuir datos.

### Coincidencias que requieren revisión antes de entrenar

| Archivo | Coincidencia | Problema |
|---|---|---|
| `train/PICADURA/704F3E54-250505-153013-0.RGB.tiff` | `validation/PICADURA/defecto.RGB.tiff` | Misma imagen con distinto nombre en train y validation |
| `train/PICADURA/704F3E54-250612-145719-5.RGB.tiff` | `test/RUSSET/704F3E54-250612-145719-5.RGB.tiff` | Misma imagen en train y test con clases distintas |

Las rutas de esta tabla son relativas a `DATASET_PALTA`. No se modificó ninguna imagen. El CSV presenta cada criterio de coincidencia: cuatro filas de criterios corresponden a **dos pares únicos**, no cuatro pares distintos.

## Estructura del repositorio
- `1. fuentes/`, `2. informe/`, `3. presentacion/`: carpetas locales vacías en la inspección; Git no versiona carpetas vacías.
- `4. entrenamiento/01_EDA.ipynb`: EDA completo, con resultados y gráficos guardados.
- `4. entrenamiento/02_Baseline.ipynb`: antecedente histórico conservado con una nota aclaratoria. No forma parte del EDA ni define el modelo principal vigente.
- `4. entrenamiento/ejecutar_eda.py`: ejecución automática del EDA con el Python activo.
- `4. entrenamiento/eda_inventario.csv`: características, rutas relativas y hashes de todos los archivos.
- `4. entrenamiento/eda_calidad.csv`: incidencias para revisión; no borra archivos.
- `4. entrenamiento/eda_duplicados.csv`: pares coincidentes, clases y particiones.
- `4. entrenamiento/eda_distribucion.csv`: conteos y porcentajes por partición.
- `4. entrenamiento/eda_resumen.json`: resultados, versiones, semilla y firma del dataset.
- `prueba/`: 154 archivos `.gsi` en subcarpetas locales; excluida de Git y distinta del dataset analizado.
- `requirements.txt`: dependencias del EDA, con versiones validadas.
- `.gitignore`: exclusiones existentes para datos, modelos y temporales.

## Instalación
Se validó con Python 3.12.14. Desde la raíz del repositorio en PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

No es necesario activar el entorno para usar estos comandos. En VS Code, seleccionar `.venv` como kernel del notebook y disponer de la extensión Jupyter. Las dependencias se limitan a análisis, imágenes, gráficos y ejecución de notebooks; este EDA no necesita TensorFlow, OpenCV ni scikit-learn.

## EDA
El notebook incluye inventario; distribución de clases y particiones; desbalance; estadísticas de dimensiones, resolución, aspecto y canales; muestras reales; RGB, intensidad y brillo; apertura y verificación de imágenes; archivos inesperados; hashes exactos de bytes y píxeles; dHash perceptual; comparación entre particiones; conclusiones calculadas e implicancias para ResNet50.

El brillo incluye el fondo y no es una medición fotométrica. dHash es un filtro exploratorio, no una prueba de identidad. Las coincidencias exactas sí evidencian contaminación entre particiones. La duplicación física no equivale a augmentation dinámica y no aumenta el número de observaciones independientes.

## Modelo propuesto
**ResNet50 mediante Transfer Learning.** Pendiente de implementación y entrenamiento después de resolver los problemas de datos. Resize y preprocesamiento se aplicarán en el pipeline, conservando originales; se deberá preservar la geometría multivista y comprobar que el tamaño de entrada conserva los defectos.

La exploración multivista descrita anteriormente se mantiene como posible línea posterior. El notebook histórico de baseline no se ha ejecutado en esta sesión.

## Ejecución
1. Colocar el dataset en la estructura indicada, conservando las particiones existentes.
2. Abrir `4. entrenamiento/01_EDA.ipynb` en VS Code, seleccionar el entorno y usar **Run All / Ejecutar todo**.
3. Alternativamente, desde la raíz:

```powershell
.\.venv\Scripts\python.exe "4. entrenamiento\ejecutar_eda.py"
```

La ejecución guarda las salidas en el notebook y regenera los cinco reportes `eda_*`. Se usa semilla 42 para muestras. El manifiesto y la firma SHA-256 permiten identificar la versión analizada. Los hashes de entrada se conservan para auditoría. La ejecución no entrena ni altera las imágenes.

## Estado actual
- **EDA realizado** sobre las 829 imágenes reales, con celdas ejecutadas, gráficos y reportes.
- **ResNet50 pendiente de entrenamiento.**
- Próximos pasos: revisar las dos coincidencias y la etiqueta contradictoria; definir identidad de fruto/lote; acordar particiones independientes; revisar ejemplos atípicos; definir balance, preprocesamiento y métricas antes de entrenar.
- Métricas futuras: F1 por clase y macro-F1, balanced accuracy, precision/recall y matriz de confusión. No ajustar hiperparámetros con test.
