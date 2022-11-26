# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image code = "code.png"
image cafe = "cafe.png"

# Déclarez les personnages utilisés dans le jeu.
define pp = Character("[nom_du_perso]", color="ffc8c8")
define na = Character('Narator', color="#ffc8c8")
define H = Character('???', color="#FF0000")


# Le jeu commence ici
label start:

    "Comment vous appelez-vous ?"
    $ nom_du_perso = renpy.input("Entrez un nom.")
    "Vous vous appelez [nom_du_perso] !"
    na "Bonjour, je suis le narrateur de ce jeu."
    na "Je vais vous raconter une histoire."
    na "Lyon, Augergne Rhone Alpes, France, 2019."
    na "2h du matin"
    scene code
    pp "Je ne comprend rien"
    pp "Pourquoi mon code ne marche pas ?"
    pp "Je suis en train de perdre mon temps"
    pp "Je ne sais pas quoi faire"

    menu :
        "Que Faire"
        "Je rentre chez moi bordel":
            jump endgame
        "On va boire un café":
            jump cafe
    
    label endgame :
    na "Vous prenez vos affaires, et rentrer doucements mais surement chez vous."
    na "Vous ne decouvrirez jamais les backrooms de 42"
    return
    
    label cafe :
    na "Vous prenez vos affaires, et vous dirigez vers la machine a café."
    scene cafe
    na "Vous ne semblez pas intrigué par le fait qu'il fait jour 
    dehors et qu'une fleche semble floter dans les escalier du campus"
    na "ni d'ailleurs par cette affichage degeulasse autour de l'ecran"

    pp "Arthur n'est pas la"
    pp "On va prendre un café degeux a la machine"
    na "vous approchez de la machine a café"
    na "vous prenez votre café"
    na "vous buvez votre café"
    na "vous vous sentez mieux"
    na "vous vous sentez plus en forme"
    na "Soudin le tournis vous prend""
    na "Vous vous sentez mal"

    scene black
    na "Vous vous reveillez"
    H "HURLEMENT"
    na "Vous entendez un hurlement"
    na "Vous vous retournez"
    na "Vous voyez une femme, avec un visage déformé, et des yeux rouges"
    na "Elle vous regarde, et vous sourit"
    na "Elle vous dit"
    na "Je suis la reine des backrooms"




        


    
    return
