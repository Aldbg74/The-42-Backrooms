# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image cluster = "cluster2.png"

# Déclarez les personnages utilisés dans le jeu.
define pp = Character('Me', color="#c8ffc8")
define na = Character('Narator', color="#ffc8c8")

# Le jeu commence ici
label start:
    scene cluster
    na "Bonjour, je suis le narrateur de ce jeu."
    na "Je vais vous raconter une histoire."
    na "Lyon, Augergne Rhone Alpes, France, 2019."
    
    return
