# Análisis de Datos en Biotecnología Aplicada con Python

Material del módulo de **Escuela Global**. Docente: **Carlos Cárdenas Fernández**.

Aplicamos herramientas computacionales en Python para representar, analizar e interpretar
información biológica en contextos de biotecnología y salud.

---

## 📦 Contenido de este repositorio

| Carpeta | Qué contiene |
|---|---|
| [`slides/`](slides/) | Diapositivas de la clase (`.pptx`) y scripts que las generan |
| [`notebooks/`](notebooks/) | Práctica guiada en Jupyter / Google Colab |
| [`data/`](data/) | Datos de ejemplo en formato FASTA |

---

## 🧬 Unidad 2 — ADN, ARN y Proteínas en Python

Clase del día: **representación de información biológica**.

- 📊 **Diapositivas:** [`slides/U2_ADN_ARN_Proteinas_EscuelaGlobal.pptx`](slides/U2_ADN_ARN_Proteinas_EscuelaGlobal.pptx)
- 💻 **Notebook (práctica):** [`notebooks/U2_practica_adn_arn_proteinas.ipynb`](notebooks/U2_practica_adn_arn_proteinas.ipynb)

### Abrir la práctica en Google Colab (sin instalar nada)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unimauro/analisis-datos-biotecnologia-python/blob/main/notebooks/U2_practica_adn_arn_proteinas.ipynb)

### Lo que aprenderás
1. El **dogma central**: ADN → ARN → Proteína
2. El ADN como **datos** (texto) y cómo medirlo (longitud, composición, **%GC**)
3. **Complemento** y cadena **reversa-complementaria**
4. **Transcripción** (ADN → ARN) y **traducción** (ARN → Proteína)
5. El **código genético** y los codones
6. **Biopython**: `Seq`, `SeqIO` y el formato FASTA
7. Caso en salud: **detectar una mutación**

---

## 🚀 Cómo usar este repositorio

### Opción A — Google Colab (recomendado para clase)
Haz clic en el badge **Open in Colab** de arriba y ejecuta las celdas con `Shift + Enter`.

### Opción B — En tu computadora
```bash
git clone https://github.com/unimauro/analisis-datos-biotecnologia-python.git
cd analisis-datos-biotecnologia-python
pip install -r requirements.txt
jupyter notebook notebooks/U2_practica_adn_arn_proteinas.ipynb
```

### Regenerar las diapositivas
```bash
cd slides/assets && python make_assets.py && python make_figures.py
cd .. && python build_deck.py
```

---

## 🗺️ Programa del módulo (7 unidades)

1. Entorno de trabajo y uso de Python en biotecnología
2. **Representación de información biológica en Python** ← *clase actual*
3. Análisis de procesos biológicos
4. Análisis de microorganismos y datos biológicos
5. Automatización de procesos biotecnológicos
6. Representación computacional en biotecnología
7. Aplicación integral en biotecnología

---

## 📚 Recursos
- [Biopython](https://biopython.org/) — Tutorial & Cookbook
- [NCBI](https://www.ncbi.nlm.nih.gov/) — genes y secuencias reales
- [Rosalind](https://rosalind.info/) — retos de bioinformática

---

*Escuela Global · Análisis de Datos en Biotecnología Aplicada con Python.*
