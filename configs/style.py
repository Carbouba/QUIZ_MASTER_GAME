"""
Constantes de style centralisées pour l'interface graphique du Quiz Master Game.

Ce module regroupe les couleurs, polices et dimensions utilisées dans toute
l'application, permettant une personnalisation visuelle cohérente et facile.
"""

# ── Palette de couleurs ────────────────────────────────────────────────────────
COLORS = {
    "bg":            "#212172",   # Arrière-plan principal
    "surface":       "#10103d",   # Surface des cartes / panneaux
    "surface2":      "#0f0f1a",   # Surface secondaire (identique au bg)
    "surface3":      "#20253b",   # Surface tertiaire (zone de question)
    "border":        "#2a2a4a",   # Couleur de bordure standard
    "primary":       "#7c3aed",   # Couleur principale (violet)
    "primary_hover": "#6d28d9",   # Survol de la couleur principale
    "primary_dim":   "#2e1065",   # Version atténuée de la couleur principale
    "danger":        "#ef4444",   # Rouge danger / erreur
    "danger_hover":  "#dc2626",   # Survol rouge danger
    "danger_light":  "#450a0a",   # Rouge léger (fond de message d'échec)
    "success_hover": "#064e3b",   # Vert succès (fond de message de bonne réponse)
    "warning":       "#f59e0b",   # Orange avertissement
    "warning_hover": "#e69206",   # Survol orange avertissement
    "text":          "#e2e8f0",   # Texte principal
    "text_muted":    "#94a3b8",   # Texte secondaire / atténué
    "text_dim":      "#475569",   # Texte très atténué
    "white":         "#e2e8f0",   # Blanc (identique au texte principal)
    "black":         "#1a1a2e",   # Noir (identique à surface)
}

# ── Polices de caractères ──────────────────────────────────────────────────────
FONTS = {
    "title":       ("Orbitron", 18, "bold"),   # Titre principal
    "h1":          ("Orbitron", 36, "bold"),   # Titre h1 (grande icône)
    "subtitle":    ("Roboto", 13),           # Sous-titre / bouton secondaire
    "button":      ("Roboto", 15, "bold"),   # Texte des boutons
    "body":        ("Roboto", 14),           # Corps de texte
    "label":       ("Roboto", 12, "bold"),   # Étiquette
    "question":    ("Roboto", 18, "bold"),   # Texte de question
    "placeholder": ("Roboto", 18),           # Texte de placeholder / secondaire
    "badge":       ("Roboto", 11, "bold"),   # Badge (petite étiquette)
    "emoji":       ("Noto Color Emoji", 40),  # Pour les emojis
}

# ── Dimensions de l'interface ─────────────────────────────────────────────────
DIMENSIONS = {
    "window_width":  500,   # Largeur de la fenêtre principale
    "window_height": 700,   # Hauteur de la fenêtre principale
    "header_height": 60,    # Hauteur de l'en-tête
    "card_height":   150,   # Hauteur d'une carte de contenu
    "border":        15,    # Rayon de bordure (arrondi des coins)
}