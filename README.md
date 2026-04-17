# 🎮 Quiz Master Game

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Une application de quiz interactive avec une interface moderne et élégante, développée en Python avec CustomTkinter. Testez vos connaissances sur la culture et la géographie du Niger et de l'Afrique de l'Ouest !

![Quiz Master Game](images/screenshot.png)

## ✨ Fonctionnalités

- 🎯 **10 questions aléatoires** à chaque partie pour une expérience renouvelée
- 🏆 **Système de record** avec persistance des meilleurs scores
- 🎨 **Interface moderne** avec thème sombre et accents néon
- ⌨️ **Navigation intuitive** avec support de la touche Entrée
- 🔄 **Réinitialisation du record** pour recommencer à zéro
- 💾 **Base de données SQLite** pour stocker les scores

## 🚀 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/username/quiz-master-game.git
   cd quiz-master-game
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate  # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'application**
   ```bash
   cd views
   python main_gui.py
   ```
   
   Ou lancez depuis la racine :
   ```bash
   python Quiz_Master_Game.py
   ```

## 📋 Structure du Projet

```
Quiz_Master_Game_GUI/
├── 📁 configs/
│   └── style.py          # Configuration des couleurs, polices et dimensions
├── 📁 data/
│   ├── questions.py      # Base de données des questions/réponses
│   └── quiz_data.db      # Base de données SQLite des records
├── 📁 images/
│   ├── back.png          # Icônes de l'interface
│   ├── play.png
│   ├── quit.png
│   └── sync.png
├── 📁 views/
│   └── main_gui.py       # Interface graphique principale
├── .gitignore
├── Quiz_Master_Game.py   # Point d'entrée alternatif
├── README.md             # Ce fichier
├── requirements.txt      # Dépendances Python
└── record.txt            # Fichier de record (legacy)
```

## 🎮 Comment jouer

1. **Lancez l'application** - L'écran d'accueil affiche le record à battre
2. **Cliquez sur "Commencer le quiz"** - 10 questions aléatoires vous seront posées
3. **Répondez aux questions** - Tapez votre réponse et appuyez sur Entrée ou cliquez sur "Envoyer"
4. **Gagnez des points** - +1 point pour une bonne réponse, -1 point pour une mauvaise
5. **Battez le record** - Votre score est sauvegardé si vous faites mieux que le record actuel

### Règles du jeu

- Le score minimum affiché est **0** (même en cas de réponses incorrectes)
- Les questions sont tirées aléatoirement d'une base de **40+ questions**
- Chaque partie propose **10 questions uniques**
- Le record est **persisté** entre les sessions

## 🛠️ Technologies utilisées

| Technologie | Usage |
|-------------|-------|
| **Python 3.12** | Langage principal |
| **CustomTkinter** | Interface graphique moderne |
| **Pillow (PIL)** | Manipulation d'images |
| **CTkMessagebox** | Boîtes de dialogue |
| **SQLite3** | Base de données des records |

## 📝 Exemple de questions

Le quiz couvre divers sujets sur le Niger et l'Afrique de l'Ouest :

| Catégorie | Exemple de question |
|-----------|---------------------|
| 🌍 Géographie | "Quelle est la capitale du Niger ?" |
| 🎭 Culture | "Quelle est la danse traditionnelle du Niger ?" |
| 📜 Histoire | "En quelle année le Niger a-t-il obtenu son indépendance ?" |
| 🌾 Agriculture | "Quel est l'aliment de base des Nigeriens ?" |

## 🎨 Personnalisation

### Modifier les couleurs

Éditez `configs/style.py` :

```python
COLORS = {
    "bg": "#212172",        # Fond principal
    "surface": "#10103d",   # Surfaces des cartes
    "primary": "#7c3aed",   # Couleur principale (violet)
    # ...
}
```

### Ajouter des questions

Éditez `data/questions.py` :

```python
questions = {
    "Ta nouvelle question ?": "La réponse",
    # ...
}
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Boubacar** - *Développeur principal*

Name: Boubacar
Project: Quiz Master Game
Stack: Python, CustomTkinter, Pillow, CTkMessagebox, SQLite3
Email: saniboubacar1992@gmail.com

- GitHub: [@Carbouba](https://github.com/Carbouba)
- Email: saniboubacar1992@gmail.com

---

⭐ N'oubliez pas de mettre une étoile si ce projet vous a plu !

## 🐛 Rapport de bugs

Si vous trouvez un bug ou avez une suggestion, veuillez [ouvrir une issue](https://github.com/Carbouba/QUIZ_MASTER_GAME/issues).

## 🔮 Roadmap

- [ ] Ajouter des catégories de questions
- [ ] Mode multijoueur en local
- [ ] Sons et effets audio
- [ ] Animation de célébration pour les nouveaux records
- [ ] Export des statistiques de jeu
- [ ] Mode sombre/clair toggle

---

<p align="center">
  Fait avec ❤️ et 🐍 en Python
</p>
