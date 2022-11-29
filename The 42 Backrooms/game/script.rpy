# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image code = "code.png"
image cafe = "cafe.png"
image b = "backrooms1.png"
image matrice = "matrice.png"
image bdoor = "backroomdoor.png"
image b2 = "backroom3.png"

# Déclarez les personnages utilisés dans le jeu.
define pp = Character("[nom_du_perso]", color="ffc8c8")
define na = Character('Narator', color="#ffc8c8")
define H = Character('???', color="#FF0000")
define I = Character( "[nom_du_persosecondaire]", color="#00FF00")


# Le jeu commence ici
label start:
    play music "NLIFE.MP3"
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
    na "Soudin le tournis vous prend"
    na "Vous vous sentez mal"
    
    scene black
    stop sound  

    jump black

    label black :
    na "Vous vous reveillez"
    H "HURLEMENT"
    na "Vous entendez un hurlement"
    jump backrooms

    label backrooms :
    scene b
    na "Vous vous retournez"
    pp "Qu'est ce que c'est que ce bordel ?"
    pp "Je suis dans les backrooms ?"
    pp "C'est pas une connerie de creepypasta a la con se truc ?"

    H "HURLEMENT"
    H "AIDEZ MOI"

    menu:
        "Que faire ?"
        "Je vais l'aider":
            jump aide
        "Je vais l'ignorer":
            jump ignore

    label aide :
    scene b
    na "Vous vous dirigez vers le hurlement"
    na "Vous voyez une porte"
    scene bdoor
    na "Vous vous approchez de la porte"
    na "Vous remarquez la presence de sang sur la porte"

    menu :
        "J'ouvre la porte":
            jump ouvre
        "Je fuis":
            jump ignore

    label ouvre :
    na "Vous ouvrez la porte"
    scene black
    na "La piece est plongée dans le noir"
    na "Vous entendez un bruit"
    H "HURLEMENT"
    H "Je suis la"
    H "[nom_du_perso] aide moi"

    menu :
        "Que faire ?"
        "Je vais l'aider":
            jump help
        "Je vais l'ignorer":
            jump ignore1

    label ignore1:
    na "Vous vous retournez"
    na "vous fuyez dans la direction opposée"
    na "Vous vous sentez mal"
    na "n'auriez vous pas fait une erreur ?"

    menu:
        "Que faire ?"
        "Je retourne l'aider":
            jump help
        "Je ne peux pas l'aider":
            jump ignore


    label help :
    scene black
    na "vous approchez"
    pp "Qu'est ce que tu veux ?"
    H "Je veux sortir"
    H "Je veux sortir de ces backrooms"
    pp "tu veux sortir ?"
    H "Oui"

    menu :
        "Que faire ?"
        "Je vais l'aider":
            jump freindship
        "Je vais l'aider contre un petit service ;)":
            jump pervers

    label pervers :
    scene black
    na "Attends"
    na "Je vais te rendre un petit service"
    return

    label freindship :
    scene black
    pp "Je vais t'aider"
    H "Merci"
    H "Merci beaucoup"
    pp "De rien"
    na "Vous lui demandez son nom"
    $ nom_du_persosecondaire = renpy.input("Entrez un nom.")
    pp "Je m'appelle [nom_du_perso]"
    H "Je m'appelle [nom_du_persosecondaire]"
    na "Vous vous êtes présenté"
    na "Vous avez fait connaissance"
    na "Vous avez décidé de vous aider"

    I "tu sait comment on sort de ces backrooms ?"
    pp "Non"
    I "Moi non plus"
    I "Mais je vais essayer de trouver une solution"
    I "Je vais essayer de trouver un moyen de sortir"
    pp "Tu as une idée ?"
    I "peut etre"
    I "Il faut en premier lieu trouver comment on est arrivé ici"
    pp "Je suis arrivé ici en prenant un café"
    I "Moi aussi"
    pp "Le café est peut etre la solution"
    I "Un café magique ?"
    pp "rire"

    H "hurrlement"
    na "Vous entendez un hurlement"
    na "Vous vous retournez"
    na "Vous voyez une porte"

    I "C'est moi ou cette porte m'etait pas la avant ?"
    pp "Non ce n'est pas toi"
    pp "la porte vient d'apparaitre"
    I "damm shit"
    I "on va ouvrir ?"
    pp "Oui, j'imagine que c'est la seule solution"
    na "Vous ouvrez la porte"
    scene b2
    na "Vous entrez dans la piece"
    na "La porte derriere vous disparait"
    pp "On ne peut plus faire marche arriere maintenant"
    I "On va ou ?"
    pp"on dirait qu'il n'y a pas 500 chemins" 
    pp "on va donc devoir le suivre"
    I "Je peux te prendre la main ?"
    pp "Oui, bien sur"
    scene black
    na "Vous vous prenez la main"
    na "Vous marchez dans un long couloir"
    na "Vous marchez pendant des heures"
    na "Vous marchez pendant des jours"

    I "On est ou ?"
    pp "Je ne sais pas, on dirait que l'on est toujours dans le meme couloir"
    I "On est perdu"
    pp "il doit y avoir une logique dans tout ça"
    I "On va trouver une solution"
    pp "Oui, on va trouver une solution"









    label ignore :
    na "Vous preverez fuire dans la direction opposé"
    scene black
    na "soudin la lumiere s'eteint"
    na "vous entendez le bruit d'une respirations"
    na "une respiration lente"
    na "qui s'approche"

    #Menu pour le fin de jeu "Sacrifice"
    
    menu :
        "Que faire ?"
        "Rester immobile":
            jump imo
        "Courir le plus vite et loin possible":
            jump Courir

    label Courir :
    na "Vous courrez le plus vite possible"
    scene backrooms1
    na "vous etes de retour au point de départ"
    na "Vous devenez fou"
    na "vous n'etes plus capable de vous controler"
    na "vous vous mettez a courir dans les couloirs"
    na "vous frappez les murs"
    na "Vous etes devenu fou"
    pp "HOUEUUUEUUU"
    pp "I STILL ALIIIIVEEEEEEEEEE"
    pp "Yhoueuseh"
    return

    # Troll de fin de jeu "Sacrifice matrice"
    label imo :
    na "Vous restez immobile"
    na "la respiration se fait de plus en plus proche"
    na "Vous sentez le souffle de l'entité sur votre visage"
    na "Vous sentez une main sur votre épaule"
    na "Felicitations vous avez perdu"
    na "Vous avez perdu contre les backrooms"
    na "L'entité vous a attrapé"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"
    na "Vous avez perdu"

    # Fin du jeu : on revient au menu principal.
    menu :
        "Resister":
            jump resistance
        "Accepter":
            jump accepte

    label resistance :
    na "Vous vous reveillez"
    scene b
    na "vous etes toujours dans les backrooms"
    H "Bonjour [nom_du_perso] !"
    H "Je suis l'entité des backrooms"
    H "Vous avez battu mon jeu"
    scene matrice
    H "Vous avez battu la matrice"
    H "Vous faites parti des rares humains a avoir reussi"
    H "Vous avez gagné"
    H "Je vous renvoie chez vous [nom_du_perso]"
    H "Peut etre nous reverrons nous un jour"
    jump goodending

    label accepte :
    return
        
    label goodending :
    scene black
    na "Vous vous reveillez"
    na "Vous vous sentez bien"
    na "Vous vous sentez en forme"
    na "Vous vous sentez en bonne santé"
    na "Vous levez vos yeux"
    scene code
    pp "Merde..."
    pp "Je suis toujours dans mon code"
    pp "Survivre au backrooms pour se faire blackhole"
    pp "C'est pas un peu con ?"
    return

    label goodendingInes :
    scene black
    pp "Vous vous reveillez"
    pp "Ines vous regarde"
    pp "Elle vous sourit"
    pp "Vous vous sentez bien"
    pp "Vous vous approchez d'elle"
    pp "vos levres se touchent"
    pp "Vous vous embrassez"
    I "Je t'aime"
    pp "Je t'aime aussi"

    na "Bonne fin"
    return




    return
