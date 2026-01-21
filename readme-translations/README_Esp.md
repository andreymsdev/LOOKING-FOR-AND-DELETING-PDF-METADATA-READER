# BUSCANDO Y ELIMINANDO METADATOS DE PDF

---

Los metadatos tienen un papel importante en el mundo digital: almacenan información oculta, como el nombre del autor del documento, la fecha de creación, el software utilizado e incluso, a veces, el historial del archivo.

---

**Un sencillo script en Python que lee y muestra los metadatos de un PDF (autor, título, asunto, etc.) y guarda la salida en un archivo `.txt`.**

# ¿Cómo funciona?

* [`metadata.py`](metadata.py) — Lee el contenido de los metadatos, como el autor, el título y otros campos.
* [`nometadata.py`](nometadata.py) — Verifica si el PDF contiene metadatos y, en caso afirmativo, los elimina.

---

# Requisitos

Asegúrate de tener **Python 3** y **PyPDF2** instalados.

```bash
pip install PyPDF2
```

---


# Cómo usar

1. Coloca tu archivo PDF en cualquier lugar de tu sistema.
2. Actualiza la ruta del archivo en el código:

```python
show_metadata("/path/to/your/file.pdf")
```

---

# ¡Espero que te guste!

Aunque los metadatos pueden ser útiles para la gestión y autenticación de documentos, también pueden exponer inadvertidamente información personal o sensible.

Por eso, es una buena práctica revisar y, de vez en cuando, eliminar los metadatos especialmente antes de compartir archivos PDF públicamente o enviarlos a destinatarios desconocidos.

<p align="left">
  <img src="../images/pingu2.jpeg" alt="PDF PINGU" width="500">
</p>

