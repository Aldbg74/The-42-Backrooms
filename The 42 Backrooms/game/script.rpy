#Section prise de notes
#Il faudrait trouver un moyen pour que le joueur de puisse pas s'appeler "narator"
#Il faudrait créer une ending speciale pour les joueurs qui ont le nom de Alexis
#Il faudrait vraiment organiser ce merdier de code
#Il faudrait vraiment trouver une banque d'image pour les scenes
#Il faudrait vraiment augmenter le sénario et les choix du perso
#Idealement il faudrait rajouter quelques "Monstres" pour rendre le jeu plus interessant
#Rajouter des timed choices pour les "appaitions" des monstres

#Attention vous lisez le scypt du jeu, vous avez donc acces au jeux et a de possibles spoilers
#Vous pouvez aussi voir des truc qui devrait etre fait mais qui ne le sont pas encore


# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image code = "code.png"
image cafe = "cafe.png"
image b = "backrooms1.png"
image matrice = "matrice.png"
image bdoor = "backroomdoor.png"
image b2 = "backroom3.png"
image b3 = "creepyroom.png"
image 2cb = "cabine.png"
image 2cour = "Foretcourse.png"

# Déclarez les personnages utilisés dans le jeu.
define pp = Character("[nom_du_perso]", color="ffc8c8")
define na = Character('Narator', color="#ffc8c8")
define H = Character('???', color="#FF0000")
define I = Character( "[nom_du_persosecondaire]", color="#00FF00")


# Le jeu commence ici
label start:
    "Comment vous appelez-vous ?"
    $ nom_du_perso = renpy.input("Entrez un nom.")

    # tentative d'integration du fait que le joueur ne doit pas pouvoir entrer narator
    #if [nom_du_perso] == "Narator":
    #    "Vous ne pouvez pas vous appeler Narator."
    #    jump start


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

    menu :
        "Que faire ?"
        "On va continuer a marcher":
            jump marcher
        "Et si on essayait de faire demi tour ?":
            jump demitour

    label demitour:
    na "Vous vous retournez"
    na "Vous marchez dans la direction opposée"
    na "Etrangement, le decort change"
    I "Le decort change on dirait"
    pp "Oui, on dirait que l'on est dans un autre couloir"
    scene b3
    na "Vous arrivez dans une piece"
    na "On dirait une salle de torture"
    na "[nom_du_persosecondaire] vous prend la main"

    menu :
        "Que faire ?"
        "Garder vos distances":
            $ distance = "oui"
            jump GDISTANCE
        "Laisser [nom_du_persosecondaire] vous prendre la main":
            $ distance = "non"
            jump GMAIN

    label GDISTANCE :
    na "vous faite en sorte de garder vos distances"
    na "Vous ne preferez pas avoir la main de [nom_du_persosecondaire] dans la votre"
    jump suite1


    label GMAIN :
    na "Vous laissez [nom_du_persosecondaire] vous prendre la main"
    na "Cette sensation est agréable"
    jump suite1

    label suite1 :
    na "Vous marchez dans la piece en evitant les objets"
    I "Dans notre malheur on a de la chance"
    pp "Pourquoi ?"
    I "Dans les jeux vidéo les backrooms sont habités par des monstres"
    I "On a de la chance, il n'y a personne ici"
    pp "Oui, on a de la chance effectivement on aurait pu tomber sur un monstre"
    scene black
    na "Une nouvelle piece sombre"
    I "J'ai peur"
    menu: 
        "Que faire ?"
        "Je vais le rassurer":
            $ rassurer = "oui"
            jump rassurer
        "Je vais le laisser dans son coin":
            $ rassurer = "non"
            jump laisser

    label rassurer :
    na "Vous vous rapprochez de [nom_du_persosecondaire]"
    na "Vous le rassurez en la prenant dans vos bras"
    na "Vous le rassurez en lui disant que tout va bien"
    I "Merci beaucoup [nom_du_perso]"
    pp "De rien [nom_du_persosecondaire]"
   
    # Je ne sais pas comment faire marcher la fonction suivante
    # if distance == "Non" :
    #    na "[nom_du_persosecondaire] se tourne vers vous"
    #    na "[nom_du_persosecondaire] vous embrasse"
    
    pp "On va continuer a marcher"
    na "Vous continuez votre marche dans ces couloirs"
    scene b
    pp "On est de retour au départ"
    I "Il y a quelque chose de bizarre"
    I "On dirait un goblet de café, la par terre"
    na "Effectivement, on semble appercevoir un goblet de café"
    pp "Si on bois ce café, on pourra peut etre sortir de ces backrooms"
    I "C'est une possibilité"
    I "Ou alors on va mourir"
    pp "On va mourir quoi qu'il arrive"
    I "Oui, c'est vrai"
    pp "On va donc boire ce café"
    I "On va boire ce café"
    na "Vous prenez le café"
    na "Vous le buvez"
    jump goodendingInes

    label laisser :
    na "Vous laissez [nom_du_persosecondaire] dans son coin"
    na "Vous finissez par tomber sur une grande piece"
    na "Vous n'avez pas remarqué que [nom_du_persosecondaire] vous avait quitté"
    na "Vous vous retrouvez seul"
    na "Vous vous retrouvez seul dans cette piece"
    na "et les murs de la piece se referment sur vous"
    na "Vous etes mort"
    return

    label marcher :
    na "Vous continuez a marcher"
    na "Vous marchez pendant des heures"
    na "Vous marchez pendant des jours"
    na "Vous marchez pendant des semaines"
    na "Vous marchez pendant des mois"
    na "Vous marchez pendant des années"
    na "Vous marchez pendant des décénies"
    na "Vous marchez pendant des siècles"
    na "Vous marchez pendant des millénaires"
    na "Vous marchez pendant des milliards d'années"
    na "Vous marchez pendant des milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards de milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards de milliards de milliards de milliards de milliards d'années"
    na "Vous marchez pendant des milliards de milliards de milliards de milliards de milliards de milliards de milliards de milliards de milliards d'années"
    na "Vous passerez donc le restant de votre existence a marcher dans ce couloir"
    return


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
   
        if distance == "non" :
            if rassurer == "oui" :
                scene black
                na "Vous vous reveillez"
                na "Ines vous regarde"
                na "Elle vous sourit"
                na "Vous vous sentez bien"
                na "Vous vous approchez d'elle"
                na "vos levres se touchent"
                na "Vous vous embrassez"
                I "Je t'aime [nom_du_perso]"
                pp "Je t'aime aussi [nom_du_persosecondaire]"
                na "Meilleure fin"
                na ""
                na ""
                na ""
                na ""
                na ""
                na ""
                na ""
                na ""
                na ""
                na "This is not the end"
                na "This is just the begining"
                H "Hurlement strident"
                na "Sauvegarde Chacal"
                na "Personne n'echappe a l'omega"
                jump p2revel

        if distance == "oui" :
            if rassurer == "non" :
                scene black
                na "Vous vous reveillez"
                na "[nom_du_persosecondaire] vous regarde"
                na "Elle vous sourit"
                I "On a gagné"
                I "On a gagné"
                na "Fin Moyenne"
                return

    label p2revel :
    scene black
    na "Vous vous reveillez"
    na "Cela fait 3 mois que vous avez quitté les backrooms"
    na "[nom_du_persosecondaire] dort de l'autre coté du lit"
    na "Cela fait aussi 3 mois que vous etes ensemble"
    scene 2cb
    na "vous sortez de votre maison"
    na "vous avez loué un airbnb pour passer un peu de temps ensemble"
    na "vous entendez des pas derrirer vous"
    na "vous vous retournez"
    I "Hello [nom_du_perso]"
    pp "Hello [nom_du_persosecondaire]"
    na "vous vous embrassez"
    I "Je ne t'ai pas entendu sortir"
    pp "Je ne voulais pas te déranger"
    I "C'est gentil, je vais faire du café tu en veux ?"
    pp "Oui, si on ne revit pas ce qu'il c'est passé"
    na "Ines repart en direction de la cuisine"
    na "Vous restez un moment a l'exterieur"
    na "Vous n'osez pas lui parler"
    na "De vos cauchemards"
    na "De vos peurs"
    na "Depuis que vous etes sorti des backrooms"
    na "Vous avez peur"
    na "Vous avez l'impression d'etre suivi"
    na "Vous avez l'impression d'etre observé"
    na "Vous avez d'ailleurs pris cet airbnb pour vous isoler"
    na "Et pour savoir si quelqu'un vous suivait bel et bien"
    scene black
    na "vous rentrez a l'interieur"
    na "vous prenez par terre une pochette que vous portez toujours avec vous"
    pp "Je vais courrir a l'exterieur"
    I "Ok, je fait des pancakes en attendant"
    na "vous sortez de l'airbnb"
    scene 2cb
    na "Vous ouvrez la pochette"
    na "Vous y trouvez un couteau, et un glock 17 flambant neuf"
    na "Un cadeau d'un ami proche de vous"
    na "vous commencez a courrir"
    image 2cour
    na "Vous courrez"
    na "Vous courrez"
    na "Vous vous retrouvez vite avec une belle vue sur le paysage"
    na "Vous le remarquez soudain"
    na "le 4x4 qui vous a suivi depuis le début"
    na "il est la"
    na "vous sortez le glock"
    na "vous pouvez vous approcher du vehicule ou vous pouvez vous enfuir"
    menu :
        "Approcher":
            jump c2approche
        "Enfuir":
            jump c2fuite
    
    label c2approche :
    scene black
    na "Vous vous approchez du vehicule"
    na "il y a un homme a l'interieur"
    na "vous vous approchez de plus en plus"

    menu:
        "Tirer":
            jump c2tire
        "Ne pas tirer":
            jump c2pasTire
    
    label c2fuite :
    na "Vous vous enfuyez"
    na "Vous repartez dans la direction de l'airbnb"
    na "Un coup de feu se fait entendre"
    na "vous tombez a terre"
    na "mort"
    return
    
    label c2tire :
    scene black
    na "Vous tirez 3 cartouches dans le vehicule"
    na "l'homme a l'interieur est mort"
    na "vous vous approchez"
    na "Vous voyez du sang et des morceaux de chair"
    na "vous vous approchez encore, et commencez a fouiller l'honme"
    na "Il porte une carte de visite"
    na "Omega Team, Contractor"
    na "Vous vous retournez"
    na "Vous voyez un homme qui vous regarde"
    na "Il vous sourit"
    H "Bonjour [nom_du_perso]"
    H "Je suis le chef de l'Omega Team"
    H "Vous n'auriez pas dû vous echapper des backrooms"
    H "Vous n'auriez pas dû vous echapper de la mort"
    na "l'homme sort sort son arme"
    na "il tire"
    scene black
    na "vous tombez"
    na ""
    na "1 mois plus tard"
    scene white
    na "Un jeu sur les backrooms qui part autant en couille"
    na "il avait fumé quoi le dev ?"
    na ""
    na "Vous ouvrez les yeux, vous ne voyez qu'un halo blanc"
    I "[nom_du_perso] ? Reste avec moi s'il te plait"
    I "Je t'aime, je pourrais pas vivre sans toi"
    scene black
    na "2 mois plus tard"
    na "[nom_du_persosecondaire], vous regarde sur votre lit d'hospital"
    na "Cela fait 3 mois que vous êtes dans le coma"
    I "Reveille toi s'il te plait"
    I "Je ne peux pas m'imaginer vivre sans toi"
    I "Tu est la personne la plus importante dans ma vie"
    na "[nom_du_persosecondaire] s'approche de vos levres et vous embrasse"
    scene white
    na "Vous ouvrez les yeux"
    I "[nom_du_perso] !!"
    scene black
    na "Vous montez difficilement vos bras pour la prendre dans les bras"
    pp "Tu m'as manqué"
    I "Ne me fait plus jamais cela"
    I "La police doit d'interoger"
    I "Tu t'est pris une balle"
    I "Qu'est ce qu'il c'est passé ?"
    na "Vous passez 1h a essayer de lui expliquer ce qu'il en est"
    I "Pourquoi tu ne m'en as pas parlé ?"
    pp "Je ne voulais pas t'inquéter"
    I "Je suis enervé contre toi la"
    na "[nom_du_persosecondaire], a effectivement l'air extrémement decu"
    pp "Tu est la seule fille qui ma jamais aimé, avec ce que l'on as vécu, je ne voulais pqs t'inquéter"
    I "ok, je vais voir les docteur leur dire que t'est debout"
    na "[nom_du_persosecondaire] sort de la chambre"
    na "Votre sac a dos est a coté de vous, vous essqyer de l'atteindre"
    na "Vous arriver a l'attraper, et en fouillaint, vous retrouver l'écrain"
    na "Vous l'ouvrez la boule au ventre"
    na "la bague est toujours la"
    na "Vous auriez du faire votre demande pendant vos vacances"
    na "Au meme moment [nom_du_persosecondaire] rentre dans la chambre"
    I "C'est quoi cette bague ? elle est pour qui ?"
    menu:
        "Que dois-je faire ?"
        "Lui faire ma demande"
            jump 2demande
        "Ne rien dire"
            jump 2riendire

    label 2riendire:
        na "Vous decidew de ne rien dire"
        na "Mais cela fait tellement de temps que vous attendez"
        jump 2demande
    
    label 2demande:
        I "Alors c'est quoi cette bague ?"
        pp "[nom_du_persosecondaire] ?"
        I "Oui ?"
        pp "Est ce que tu veux partager ta vie avec moi ?"
        na "Un leger blanc se fait sentir"
        I "Tu me demande en mariage ?"
        pp "Oui"
        na "[nom_du_persosecondaire] vous saute au coup"
        I "Oui, oui OUI !!"
        I "Je t'aime bordel je veux passer ma vie avec toi"
        na "Vous passez plusieurs minutes a vous embrasser"
        jump 2suite
    
    label 2suite:
        na "lieu inconnu"
        H "Monsieur, il c'est reveillé, l'autre est toujours en vie"
        H "Nous devons les éliminer vous etes au courant"
        H "Le projets backroom est historiquement un projet de la NSA pour torturer des prisoniers"
        H "Le projet est devenu hors de controle, et des personnes sont comme tombé a l'interieur"
        H "Beaucoup sont mort, il ne doivent pas pouvoir témoigner"
        H "Elimination classique ou les backroom v2 ?"
        H "On y reflechit, rester joignable"

        na "Lyon"
        na "Vous avez depuis longtemps fait des recherches"
        na "Depuis votre sortie d'hospital sur Omega"
        na "Une société paramilitaire employé par les gouvernements les plus puissants"
        na "et accesoirement chargé du mauvais job pour les services secrets de plusieurs pays"
        na "Vous avez tout rassemblé sur se groupe"
        na "Vous avez désormais une grande responsabilité"
        na "Vous pouvez laisser la vie continuer, et prendre le risque de mourir"
        na "Ou aller chercher ces fils de pute chez eux et les mettre hors d'état de nuite"
        menu :
            "Les attaquer"
                jump 2attack
            "On laisse tomber"
                jump 2giveup
    label 2attack:
        na "Votre décision est prise"
        na "Ces personnes sont trop dangereuses"
        na "Et vous menaceront vous et [nom_du_persosecondaire] jusqu'a la fin de votre vie"
        na "Vous ne pouvez pas les laisser faire"
        na "Vous etes dans votre sous sol"
        # Faudrait trouver la photo d'une cave
        na "Vous avez appelé de vielles relations"
        jump flashback
    



    label 2giveup:
        na "vous avez decidé de laisser tomber"
        na "vous vivez votre meilleure vie avec [nom_du_persosecondaire]"
        na "Un jour vous prenez tout les deux la voiture pour aller au repas de présentation a sa famille"
        na "Vous avez le trac"
        pp "Tu est bien installé on peut y aller ?"
        I "On peut y aller, mes parents sont cool tu vera, il devrait bien t'aimer"
        na "Vous mettez la clef dans le contact"
        na "Vous mettez le contact"
        return

    label flashback:
        na "Pays inconnu, 22h"
        na "Il y a de nombreuse années"
        