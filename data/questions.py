"""
Module contenant le dictionnaire des questions/réponses du Quiz Master Game.

Thème : Culture locale — Niger, Afrique de l'Ouest, Sahel.
La fonction get_question() retourne le dictionnaire complet, ce qui facilite
son import et son utilisation depuis d'autres modules.

Catégories :
  - Niger : Géographie & Villes
  - Niger : Histoire & Politique
  - Niger : Traditions & Culture
  - Niger : Gastronomie
  - Niger : Langues & Ethnies
  - Afrique de l'Ouest : Capitales & Pays
  - Afrique de l'Ouest : Histoire & Culture
  - Sahel & Nature locale
"""


def get_question():
    """Retourne le dictionnaire de toutes les questions et leurs réponses.

    Returns:
        dict: Un dictionnaire où chaque clé est une question (str)
              et chaque valeur est la réponse attendue (str).
    """
    questions = {

        # ── Niger : Géographie & Villes ────────────────────────────────────
        "Quelle est la capitale du Niger ?": "Niamey",
        "Quelle est la deuxième\nplus grande ville du Niger ?": "Zinder",
        "Quel grand fleuve traverse\nle sud-ouest du Niger ?": "Niger",
        "Quel désert couvre plus de\n80 % du territoire nigérien ?": "Sahara",
        "Quel lac transfrontalier\nse trouve à l'extrême sud-est ?": "Tchad",
        "Quelle ville est la capitale\nhistorique des Touaregs au Niger ?": "Agadez",
        "Combien de régions\nadministratives compte le Niger ?": "8",
        "Quelle région est célèbre\npour ses mines d'uranium ?": "Agadez",
        "Quel fleuve prend sa source\nen Guinée et passe par Niamey ?": "Niger",
        "Quelle ville du Niger\nest surnommée 'La Sultanate' ?": "Zinder",
        "Dans quelle région\nse trouve la ville de Tahoua ?": "Tahoua",
        "Quel massif montagneux\nse trouve au nord du Niger ?": "Aïr",
        "Le Niger partage sa frontière\navec combien de pays ?": "7",
        "Quel pays est directement\nau sud du Niger ?": "Nigeria",
        "Quelle ville abrite\nle Grand Marché de Niamey ?": "Niamey",
        "Quelle rivière saisonnière\ntraverse Niamey en parallèle du Niger ?": "Goulbi",
        "Dans quel département\nse trouve la ville de Dosso ?": "Dosso",
        "Quel parc national du Niger\nest classé au patrimoine de l'UNESCO ?": "W",

        # ── Niger : Histoire & Politique ──────────────────────────────────
        "En quelle année le Niger\na-t-il obtenu son indépendance ?": "1960",
        "De quel pays le Niger\na-t-il obtenu son indépendance ?": "France",
        "Qui fut le premier président\ndu Niger indépendant ?": "Diori",
        "En quelle année la première\nconstitution du Niger a-t-elle été adoptée ?": "1960",
        "Quel évènement historique\na eu lieu le 26 juillet 2023 au Niger ?": "Coup d'État",
        "Comment s'appelait le Niger\nà l'époque coloniale ?": "Territoire du Niger",
        "Quelle organisation régionale\nregroupant des pays africains a suspendu\nle Niger en 2023 ?": "CEDEAO",
        "Quel sultan règne\nsur la ville d'Agadez ?": "Sultan d'Agadez",
        "Quelle est la fête nationale\ndu Niger ?": "18 décembre",
        "Quel empire historique\na dominé l'ouest du Niger\nau XVe siècle ?": "Songhaï",
        "Quel nom portait l'empire\nqui contrôlait Zinder avant la colonisation ?": "Damagaram",
        "En quelle année\nle premier coup d'État au Niger\na-t-il eu lieu ?": "1974",

        # ── Niger : Traditions & Culture ──────────────────────────────────
        "Quel animal est\nle symbole national du Niger ?": "Gazelle",
        "Comment s'appelle\nle thé vert très sucré bu\ntout au long de la journée ?": "Ataye",
        "Comment s'appelle la danse\ntraditionelle des Zarma-Songhaï ?": "Hauka",
        "Comment appelle-t-on\nle bâton de lutte traditionnel\npratiqué au Niger ?": "Lutte traditionnelle",
        "Quel tissu coloré\nporté par les femmes nigériennes\ns'appelle ?": "Pagne",
        "Quel instrument à cordes\ntraditional est très populaire\nchez les Haoussa ?": "Molo",
        "Comment appelle-t-on\nle griot au Niger\nen langue haoussa ?": "Maroki",
        "Quelle fête marquant\nla fin du Ramadan est\ntrès célébrée au Niger ?": "Aïd el-Fitr",
        "Quel festival annuel\ncélèbre la culture\ndes Touaregs à Agadez ?": "Festival d'Agadez",
        "Comment s'appelle\nla case traditionnelle\nronde des zones rurales ?": "Paillote",
        "Quel vêtement long\net ample est porté\npar les hommes nigériens ?": "Boubou",
        "La mosquée d'Agadez\nest construite en quel matériau ?": "Terre",
        "Comment appelle-t-on\nle mariage traditionnel\nhaoussa ?": "Kununchi",
        "Quel mot signifie\n'bienvenue' en haoussa ?": "Sannu",

        # ── Niger : Gastronomie ────────────────────────────────────────────
        "Comment s'appelle\nla viande séchée et épicée\ntypique du Niger ?": "Kilishi",
        "Quel plat à base de mil\nest le plus consommé\nau Niger ?": "Dégué",
        "Comment appelle-t-on\nla bouillie de mil\nbue le matin ?": "Koko",
        "Quel fruit du désert\ntrès sucré pousse\nsur le palmier dattier ?": "Datte",
        "Comment s'appelle\nla galette de haricots\nfrite à l'huile ?": "Kosai",
        "Quel plat à base de riz\nservi lors des fêtes\nau Niger ?": "Riz gras",
        "Comment appelle-t-on\nla sauce arachide\ntrès prisée au Niger ?": "Miyan gyada",
        "Quel légume-feuille\ntrès utilisé dans\nles sauces nigériennes ?": "Moringa",
        "Comment s'appelle\nla bière traditionnelle\nà base de mil ?": "Dolo",
        "Quel fruit sauvage\ndu Sahel est utilisé\npour faire du jus ?": "Jujube",

        # ── Niger : Langues & Ethnies ──────────────────────────────────────
        "Quelle est la langue officielle\ndu Niger ?": "Français",
        "Quelle ethnie est la plus\nnombreuse au Niger ?": "Haoussa",
        "Quelle langue parle\nl'ethnie Zarma-Songhaï ?": "Zarma",
        "Comment dit-on\n'merci' en haoussa ?": "Nagode",
        "Quelle ethnie nomade\nhabite principalement\nle désert du Sahara au Niger ?": "Touareg",
        "Quel peuple éleveur\nnomade est présent\nau Niger et au Mali ?": "Peul",
        "Comment s'appelle\nl'écriture traditionnelle\nutilisée par les Touaregs ?": "Tifinagh",
        "Combien de langues nationales\nsont officiellement reconnues\nau Niger ?": "10",
        "Quel groupe ethnique\nest connu pour sa pratique\ndu commerce transsaharien ?": "Touareg",
        "Comment dit-on\n'bonjour' en zarma ?": "Fofo",

        # ── Afrique de l'Ouest : Capitales & Pays ─────────────────────────
        "Quelle est la capitale\ndu Sénégal ?": "Dakar",
        "Quelle est la capitale\ndu Mali ?": "Bamako",
        "Quelle est la capitale\ndu Burkina Faso ?": "Ouagadougou",
        "Quelle est la capitale\nde la Côte d'Ivoire ?": "Yamoussoukro",
        "Quelle est la capitale\ndu Nigeria ?": "Abuja",
        "Quel pays d'Afrique de l'Ouest\nest le plus peuplé ?": "Nigeria",
        "Quelle est la capitale\nde la Guinée ?": "Conakry",
        "Quel pays d'Afrique de l'Ouest\nest entièrement enclavé\ncomme le Niger ?": "Burkina Faso",
        "Quelle est la capitale\ndu Bénin ?": "Porto-Novo",
        "Quel pays est situé\nà l'ouest du Niger ?": "Mali",
        "Quel pays est situé\nà l'est du Niger ?": "Tchad",
        "Quelle est la capitale\ndu Togo ?": "Lomé",

        # ── Afrique de l'Ouest : Histoire & Culture ────────────────────────
        "Quel empire médiéval\nétait connu pour\nson or au Mali ?": "Mali",
        "Quel célèbre roi du Mali\na fait un pèlerinage\nà La Mecque au XIVe siècle ?": "Mansa Moussa",
        "Quelle ville malienne\nétait un grand centre\ndu savoir islamique ?": "Tombouctou",
        "Quel empire a précédé\ncelui du Mali\nen Afrique occidentale ?": "Ghana",
        "Comment s'appelle\nle tissu coloré traditionnel\norigine du Ghana ?": "Kente",
        "Quel instrument de musique\nest symbole de\nl'Afrique de l'Ouest ?": "Djembé",
        "Comment appelle-t-on\nle conteur traditionnel\nen Afrique de l'Ouest ?": "Griot",
        "Quel festival sénégalais\ncélèbre la musique\net les arts africains ?": "FESMAN",
        "Quelle religion est\nla plus pratiquée\nen Afrique de l'Ouest ?": "Islam",
        "Quelle organisation\nregroupe les pays\nd'Afrique de l'Ouest ?": "CEDEAO",
        "Quel pays africain\nn'a jamais été colonisé ?": "Éthiopie",
        "Quelle monnaie commune\nutilisent plusieurs pays\nd'Afrique de l'Ouest ?": "CFA",

        # ── Sahel & Nature locale ──────────────────────────────────────────
        "Comment appelle-t-on\nla zone de transition\nentre le Sahara et\nla savane africaine ?": "Sahel",
        "Quel arbre emblématique\ndu Sahel stocke\nde l'eau dans son tronc ?": "Baobab",
        "Quelle plante du Sahel\nest très nutritive\net utilisée comme légume ?": "Moringa",
        "Comment s'appelle\nle vent chaud et sablonneux\nqui souffle au Niger ?": "Harmattan",
        "Quel animal sauvage\nse trouve dans\nle parc du W au Niger ?": "Éléphant",
        "Quelle saison des pluies\ns'appelle localement\n'hivernage' au Sahel ?": "Hivernage",
        "Quel arbre produit\nle karité, très utilisé\ndans les cosmétiques ?": "Karité",
        "Comment appelle-t-on\nla migration annuelle\ndes animaux vers\nles zones de pâturage ?": "Transhumance",
        "Quel phénomène naturel\nmenace le plus\nles terres du Niger ?": "Désertification",
        "Quelle initiative portée\npar plusieurs pays africains\nvise à stopper l'avancée\ndu désert ?": "Grande Muraille Verte",
    }

    return questions
