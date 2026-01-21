# PROCURANDO E DELETANDO METADATAS DO PDF

---

Metadados têm um papel importante no mundo digital: eles armazenam informações ocultas, como o nome do autor do documento, a data de criação, o software utilizado e, às vezes, até o histórico do arquivo.

---

**Um simples script em Python que lê e exibe os metadados de um PDF (autor, título, assunto etc.) e salva a saída em um arquivo `.txt`.**

# Como funciona?

* [`metadata.py`](metadata.py) Lê o conteúdo dos metadados, como autor, título e outros campos.
* [`nometadata.py`](nometadata.py) Verifica se o PDF possui metadados e, caso possua, remove-os.

---

# Requisitos

Certifique-se que o **Python 3** e **PyPDF2** estão instalados.

```bash
pip install PyPDF2
```

---

# Como usar

1. Coloque o seu arquivo PDF em qualquer lugar do seu sistema.
2. Atualize o caminho do arquivo no código:

```python
show_metadata("/path/to/your/file.pdf")
```

---

# Espero que goste!

Embora os metadados possam ser úteis para o gerenciamento e a autenticação de documentos, eles também podem expor, sem querer, informações pessoais ou sensíveis.

Por isso, é uma boa prática revisar e, ocasionalmente, remover os metadados especialmente antes de compartilhar PDFs publicamente ou enviá-los para destinatários desconhecidos.

<p align="left">
  <img src="../images/pingu2.jpeg" alt="PDF PINGU" width="500">
</p>


