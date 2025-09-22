# BinaryML

Un projet de machine learning simple qui manipule des séquences de mots avec des scores de confiance et des utilitaires de tokenisation.

## 📁 Structure du projet

```
BinaryML/
├── src/
│   ├── main.py              # Point d'entrée principal
│   ├── utils/
│   │   └── token.py         # Utilitaires de tokenisation et encodage
│   └── datasets/
│       └── datasets.json    # Dataset de 50 suites de mots avec scores de confiance
└── README.md
```

## 🎯 Fonctionnalités

### Tokenisation (`utils/token.py`)
- **Tokenisation par caractère** : `tokenize(text)` convertit le texte en liste de caractères
- **Détokenisation** : `detokenize(tokens)` reconstitue le texte
- **Conversion token → entier** : `tokenToInteger(token)` utilise les valeurs ASCII
- **Conversion entier → token** : `integerToToken(integer)` utilise chr()
- **Encodage/décodage texte** : 
  - `encode_text(text)` → chaîne de codes ASCII séparés par espaces
  - `decode_text(encoded)` → texte original

### Dataset (`datasets/datasets.json`)
Structure des données :
```json
{
  "word_sequences": [
    {
      "id": 1,
      "text": "bonjour salut",
      "confidence": 0.95
    }
  ]
}
```

**50 suites de mots** couvrant :
- Salutations et politesse
- Technologie et programmation
- Intelligence artificielle
- Développement web/mobile
- Concepts techniques

**Scores de confiance** : 0.23 à 0.96

### Application principale (`main.py`)
- Interface colorée avec `colorama`
- Chargement et affichage du dataset
- Filtrage par score de confiance (seuil : 0.9)
- Logique de comparaison binaire des derniers mots
- Interface utilisateur interactive

## 🚀 Utilisation

```bash
# Installer les dépendances
pip install colorama

# Lancer l'application
python3 src/main.py
```

## 🔧 Fonctionnement technique

1. **Chargement du dataset** : Parse le JSON et extrait les séquences de mots
2. **Filtrage intelligent** : Affiche uniquement les entrées avec :
   - Confiance ≥ 0.9
   - Derniers mots différents (comparaison binaire)
3. **Interface colorée** : Vert pour le bot, jaune pour l'utilisateur
4. **Encodage binaire** : Conversion des mots en bytes pour comparaison

## 📊 Caractéristiques du dataset

- **Volume** : 50 entrées
- **Format** : Suites de 2-3 mots
- **Langues** : Français et termes techniques anglais
- **Domaines** : IA, programmation, web, salutations
- **Confiance moyenne** : ~0.75

## 🎨 Technologies utilisées

- **Python 3** : Langage principal
- **JSON** : Format de données
- **Colorama** : Interface colorée en terminal
- **Encodage ASCII/UTF-8** : Manipulation de texte

## 🤖 Pour Copilot

Ce projet implémente :
- Tokenisation de base pour NLP
- Dataset structuré avec scores de confiance
- Comparaisons binaires de mots
- Interface utilisateur simple
- Utilitaires de conversion texte ↔ numérique

Idéal pour comprendre les bases du traitement de langage naturel et de la manipulation de données textuelles.