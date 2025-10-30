# RECHERCHE ET SUPPRESSION DES MÉTADONNÉES PDF

<p align="left">
  <img src="../images/pingu.jpeg" alt="PDF PINGU" width="500">
</p>

Les métadonnées jouent un rôle important dans le monde numérique : elles stockent des informations cachées, comme le nom de l’auteur du document, la date de création, le logiciel utilisé et parfois même l’historique du fichier.

---

**Un simple script Python qui lit et affiche les métadonnées d’un fichier PDF (auteur, titre, sujet, etc.) et enregistre la sortie dans un fichier `.txt`.**

# Comment ça marche?

* [`metadata.py`](metadata.py) Lit le contenu des métadonnées, comme l’auteur, le titre et d’autres champs.
* [`nometadata.py`](nometadata.py) Vérifie si le PDF contient des métadonnées et, le cas échéant, les supprime.

---

# Exigences

Assurez-vous d’avoir **Python 3** et **PyPDF2** installés.

```bash
pip install PyPDF2
```

---

# Comment utiliser

1. Placez votre fichier PDF n’importe où sur votre système.
1. Mettez à jour le chemin du fichier dans le code.

```python
show_metadata("/path/to/your/file.pdf")
```

---

# J'espère que cela vous plaira!

Bien que les métadonnées puissent être utiles pour la gestion et l’authentification des documents, elles peuvent aussi révéler involontairement des informations personnelles ou sensibles.

C’est pourquoi il est conseillé de vérifier et de supprimer de temps en temps les métadonnées, surtout avant de partager des fichiers PDF publiquement ou de les envoyer à des destinataires inconnus.

![PDF PINGU](../images/pingu2.jpeg)

