#!/usr/bin/env python3
"""
Ce programme sert à :
=====================
    Ce programme sert à simuler une renconrte dans Donjons & Dragons 5e.


@todo : Liste des choses à faire !!!
====================================
    # BUG : Sous l'IDE Spyder, j'ai une bonne gestion des caractères (encodage 
        UTF-8 ?) mais pas ailleurs ...
        
    # @todo_Usage :
        Remplir correctement la section 'Usage' ci-dessous dans la 
        documentation de ce programme.

    # @todo_Verbose_type :
        Passer verbose en type 'int' avec : 
            0 : pas de détail,
            1 : détails minimalistes,
            2 : un peu plus de détaile, 
            etc. ...
            
    # @todo_Niveau_de_detail :
        Si pas de détails sélectionné, passer le résultat en retour de la 
        fonction combat() plutôt que d'en forcer l'impression dans la console.
        
    # @todo_Critique_a :
        Gestion des coups critiques


Usage: # @todo_Usage
======
    Commande à rentrer :
        rencontre(fichier, verbose)

        fichier : str
            Nom du fichier 'combatants.json' contenant la liste des combatants
        verbose : str ou boolean
            Niveau de détail du retour console :
                False : Aucun retour # @todo_Niveau_de_detail
        
        
Created on : Sun Jan  1 10:04:20 2023
============


Versions :
==========
    v-0.1 : Appropriation d'un code généré par chat GPT qui m'a permis 
            d'apprendre à programmer en python
            
    v-0.2 : Réalisation d'un premier programme fonctionnel permettant de 
            simuler une rencontre.
            
    v-0.3 : EN COURS DE DÉVELOPPEMENT
            Amélioration des commentaires
            Inventaire des améliorations à apporter
            
"""
# -*- coding: utf-8 -*- # BUG ???

__authors__ = ("Geo-07")
__contact__ = ("geo.zerosept@gmail.com")
__githhub__ = ("https://github.com/Geo-07/DND-5e_simulateur_de_rencontre")
__copyright__ = "CC-BY-SA"
__date__ = "2023-01-08"
__version__= "0.3"


import dice
import json




        

# Fonction création de combatant    
def import_combatants(fichier, verbose): # @todo_Verbose_type
    """
Cette fonction a pour rôle de lire un fichier JSON recensant les combatants et
de créer un objet Combatant pour chacun d'entre-eux. Elle est capable de
retourner la liste des combatants dans la console grâce au mode verbose.

    Parameters
    ----------
    fichier : Texte
        Nom du fichier au format JSON contenant le liste des combatant
        si réglé à "default", prend "combatants.json" comme nom de fichier
    verbose : Boolean (True or False)
        Imprime dans la console la liste des combattants créés et leurs 
        équipes respectives.

    Returns
    -------
    Sortie : List
        Retourne la liste des objets Combatants créés en sortie.

    """
    combatants = []
    if fichier == "default":
        fichier = "combatants.json"
        print(f"Le fichier par défaut est réglé sur {fichier}")
    elif not fichier:
        fichier = "combatants.json"
        print("Le fichier n'a pas été renseigné !")
        print(f"{fichier} a été utilisé par défaut")
    with open(fichier, "r") as f:
        donnees = json.load(f)
    for d in donnees:
        c = Combatant()
        c.nom = d["nom"]
        c.equipe = d["equipe"]
        c.pv = d["pv"]
        c.bonus_initiative = d["bonus_initiative"]
        c.classe_armure = d["ca"]
        c.nombre_attaques = d["nombre_attaques"]
        c.pour_toucher = d["pour_toucher"]
        c.des_pour_toucher = d["des_pour_toucher"]
        c.critique_a = d["critique_a"]
        c.bonus_degats = d["bonus_degats"]
        c.nombre_des_degats = d["nombre_des_degats"]
        c.valeur_des_degats = d["valeur_des_degats"]
        combatants.append(c)
    if verbose == True:
        for c in combatants:
            print(f"{c.nom} de l'équipe {c.equipe} est prêt(e) au combat")
    return combatants

def calcul_initiative(liste,verbose):
    """
Cette fonction calcule l'initiative pour chaque combatant de la liste en
paramètre, puis les classe par ordre décroissant d'initiative pour leur
affecter leur rang de combatant.

    Parameters
    ----------
    liste : List
        Liste d'objets Combatants.
    verbose : Boolean
        Imprime dans la console le dictionnaire de l'initiative.

    Returns
    -------
    Sortie : List
        Liste d'objets combatants_tries triés par rang d'initiative croissant

    """
    for obj in liste:
        obj.initiative = dice.roll('1d20t') + obj.bonus_initiative
    #La commande suivante permet de trier les combatants par rang d'initiative
    combatants_tries = sorted(combatants,
                              key=lambda obj: obj.initiative,
                              reverse = True)
    i = 1
    for obj in combatants_tries:
        obj.rang_initiative = i
        i = i+1
    if verbose  == True:
        for obj in combatants_tries:
            print(f"{obj.nom} : initiative {obj.initiative} rang\
 {obj.rang_initiative} équipe : {obj.equipe}")
    for combatant in combatants_tries:
        if combatant.equipe == "Aventuriers": #A reprendre !!!!!
            aventuriers_combatants.append(combatant)
        elif combatant.equipe == "Ennemis":
            ennemis_combatants.append(combatant)
        else:
            print("1 -Les équipes sont mal définies ou les options choisies ne\
 sont pas prises en charge") 
    return (combatants_tries, ennemis_combatants, aventuriers_combatants)


def attaque(attaquant, defenseur, verbose):
    """
    Cette fonction permet de gérer les attaques en combat et de mettre à jour
    les objets relatifs au défenseur si ce dernier encaisse des dégâts.
    Si un combatant est tué, on met également à jour les listes :
        ko (en l'intégrant dedans)
        ennemis_combatants ou aventuriers_combatants (en l'enlevant de là)

    Parameters
    ----------
    attaquant : Objet
        Objet attaquant.
    defenseur : Objet
        Objet défenseur.
    verbose : Boolean
        Veut-on un retour écrit dans la console des évènements ?

    Returns
    -------
    none

    """
    pour_toucher = dice.roll('1d20t') + attaquant.pour_toucher
    degats = dice.roll("{0}d{1}t".format(attaquant.nombre_des_degats,
                                         attaquant.valeur_des_degats))\
                                        + attaquant.bonus_degats
    if verbose == True:
        print(f"pour toucher : {pour_toucher}, degats : {degats}, ca : \
{defenseur.classe_armure}")
    if defenseur.classe_armure <= pour_toucher:
        defenseur.pv = defenseur.pv - degats
        defenseur.touche = True
        if verbose == True:
            print(f"{attaquant.nom} inflige {degats} points de dégats \
à {defenseur.nom} à qui il reste {defenseur.pv} PV")
    else:
        if verbose == True:
            print(f"{attaquant.nom} rate son attaque contre {defenseur.nom}")
    if defenseur.pv <= 0:
        defenseur.ko = True
        initiative.remove(defenseur)
        if defenseur.equipe == "Ennemis":
            ennemis_combatants.remove(defenseur)
        elif defenseur.equipe == "Aventuriers":
            aventuriers_combatants.remove(defenseur)
        ko.append(defenseur)
        if verbose == True:
            print(f"{attaquant.nom} met KO {defenseur.nom} !!!")
            

def sauvegarde_contre_la_mort(ko, verbose):
    """
    Un combattant KO doit faire à chaque tour des jets de sauvegarde contre la
    mort pour déterminer les conséquences de ses blessures. Il lance 1d20 et
    s'il fait 10 ou +, il réussit son jet de sauvegarde, s'il fait moins de 10,
    il le rate. À la première des deux conditions remplies (3 succès ou 3 
    échecs), il est soit stabilisé (il reste à 0 PV et ne combat pas, mais ses
    blessures ne menacent plus sa vie) soit il meurt de ses blessures.
                                    
        Pour chaque objet 'victime' dans la liste 'ko', on lance 1d20
            Sur un résultat inférieur à 10, on incrémente l'attribut 'jdsmort'
            de l'objet 'victime'.
                Dans ce cas, on teste si l'attribut 'jdsmort' de l'objet
                'vicime' vaut 3 (ou plus, même si c'est inutile ...). Si cette
                condition est remplie, on retire l'objet 'victime' de la liste
                'ko' et on le met dans la liste 'morts'.
            Sur un 10 ou plus, on incrémente l'attribut 'jdsvie' de l'objet
            'victime'.
                Dans ce cas, on teste si l'attribut 'jdsvie' de l'objet
                'vicime' vaut 3 (ou plus, même si c'est inutile ...). Si cette
                condition est remplie, on retire l'objet 'victime' de la liste
                'ko' et on le met dans la liste 'stabilises'.
            

    Parameters
    ----------
    ko : list
        Liste des objets 'victimes' contenant les combattants dont les 'pv' ont
        étés réduits à 0.
    verbose : boolean ou str
        Décrit le niveau de détail des retours imprimés dans la console :
            - False (boolean) = Aucun retour
            - "minimal" (str) = Retour limité à l'essentiel
            - True (boolean) = Retour ultra détaillé

    Returns
    -------
    None.

    """
    for victime in ko:
        if dice.roll('1d20t') < 10:
            victime.jdsmort = victime.jdsmort + 1
            if victime.jdsmort >= 3:
                morts.append(victime)
                ko.remove(victime)
        else:
            victime.jdsvie = victime.jdsvie + 1
            if victime.jdsvie >= 3:
                stabilises.append(victime)
                ko.remove(victime)


# DÉFINITION DE LA FONCTION 'combat'
def combat(initiative, verbose):
    """
    Cette fonction qui effectue le combat en lui-même va permettre de gérer les
    atttaques faites avec la fonction 'attaque' durant une rencontre.
    
    Voici les étapes effectuées dans l'ordre :
        1- Initialisation des variables 'equipe_gagnante' et 'tours' à 0
        2- Tant qu'il n'y a pas d'équipe gagnante :
            a) On imprime dans la console le numéro du tour actuel si 'verbose'
            le permet.
            b) Pour chaque attaquant dans l'ordre d'initiative :
                1- On crée la variable 'equipe_defenseur' qui prend la valeur
                opposée à celle de l'équipe de l'attaquant.
                2- Pour un nombre d'attaques corespondant à celui de 
                l'attaquant, s'il reste au moins un défenseur, on utilise la 
                fonction 'attaque' pour calculer le résultat de l'attaque de 
                l'attaquant sur la première occurence de la liste 
                'equipe_defenseur'.
            c) On détermine l'équipe gagnante et on l'indique dans la variable 
            'equipe_gagnante'.
            d) On effectue les jets de sauvegarde contre la mort des combatants
            KO grâce à la fonction 'sauvegarde_contre_la_mort'
        3- On imprime le résultat du combat dans la console

    Parameters
    ----------
    initiative : list
        Liste des combatants classés par ordre d'initiative.
    verbose : boolean ou str
        Niveau de détail du retour imprimé dans la console.

    Returns
    -------
    equipe_gagnante : str
        Renvoie l'équipe gagnante sous forme de chaine de caractères

    """
    equipe_gagnante = 0
    tours = 0
    while equipe_gagnante == 0 :
        tours = tours + 1
        if verbose == True:
            print(f"Tour {tours}")
        for attaquant in initiative: #Objet attaquant selon rang d'initiative
            #On détermine l'équipe du défenseur
            if attaquant.equipe == "Aventuriers": #A reprendre !!!!!
                equipe_defenseur = ennemis_combatants
            elif attaquant.equipe == "Ennemis":
                equipe_defenseur = aventuriers_combatants
            else:
                print("2 -Les équipes sont mal définies ou les options\
choisies ne sont pas prises en charge")
            for i in range(attaquant.nombre_attaques):
                if len(equipe_defenseur) > 0:
                    attaque(attaquant, equipe_defenseur[0], verbose)
                    i = i+1
        if len(aventuriers_combatants) == 0:
            equipe_gagnante = "Ennemis"
        elif len(ennemis_combatants) == 0:
            equipe_gagnante = "Aventuriers"
        sauvegarde_contre_la_mort(ko, verbose)
    # @todo_Niveau_de_detail
    if verbose == "minimal":
        print(f"Les {equipe_gagnante} ont gagné le combat en {tours} tours")
    return(equipe_gagnante)


# DÉFINITION DE LA FONCTION 'rencontre'            
def rencontre(fichier, verbose):
    """
    C'est la fonction centrale du programme qui va articuler les appels aux 
    différentes fonctions qui le constituent !
    
    Voici les étapes effectuées dans l'ordre :
        1- Déclaration des variables globales du programme :
            combatants (list) : liste des combatants
            initiative (list) : liste des combatants classés par initiative
        2- Création de la liste des combatants :
            Les combatants sont importés depuis le 'fichier' dans la liste 
            'combatants' grâce à la fonction 'import_combatants'.
        3- Calcul de l'ordre d'initiative :
            L'initiative des combatants de la liste 'combatants' est calculée 
            et ils sont rangés dans la liste 'initiative' par ordre 
            d'initiative décroissant grâce à la fonction 'calcul_initiative'. 
            On crée également deux listes 'ennemis_combatants' et 
            'aventuriers_combatants' contenant les combatants des groupes
            respectifs aventuriers ou ennemis classés par initiative 
            décroissante.
        4- Combat :
            On utilise la fonction 'combat' pour déterminer l'issue de la 
            rencontre.
        5- Retour console du résultat :
            On met à jour les variables 'nombre_ko', 'nombre_morts' et 
            'nombre_stabilises' et selon la valeur de 'verbose', on imprime
            dans la console les détails du combat.
        
    Parameters
    ----------
    fichier : str
        Nom du fichier JSON décrivant les combatants.
    verbose : boolean ou str
        niveau de détail du retour dans la console.

    Returns
    -------
    None.

    """
    global combatants
    global initiative
    combatants = import_combatants(fichier, verbose)
    (initiative, ennemis_combatants, aventuriers_combatants) = \
        calcul_initiative(combatants, verbose)
    equipe_gagnante = combat(initiative, verbose)
    # attaque (initiative[1], initiative[2], True)
    nombre_ko = len(ko)
    nombre_morts = len(morts)
    nombre_stabilises = len(stabilises)
    if verbose == "minimal" or verbose == True:
        if nombre_ko > 0:
            print(f"Il y a {nombre_ko} combatant(s) KO ! La liste est :")
            for combatants_ko in ko:
                print(combatants_ko.nom)
        if nombre_morts > 0:
            print(f"Il y a {nombre_morts} combatant(s) morts ! La liste est :")
            for combatants_morts in morts:
                print(combatants_morts.nom)
        if nombre_stabilises > 0:
            print(f"Il y a {nombre_stabilises} combatant(s) stabilisés ! \
La liste est :")
            for combatants_stabilises in stabilises:
                print(combatants_stabilises.nom)
    return(equipe_gagnante)


# DÉFINITION DE L'OBJET : 'Combatant'
class Combatant:
    """Cette classe crée un combattant avec tous ses attributs.
    Elle gère l'attaque et la défense de chaque combattant et enregistre son 
    état actuel (pv ko, jds contre la mort, stabilisé et mort).
    
    A class to represent a person.

    ...

    Attributes
    ----------
    nom : str
        Le nom de cet objet 'combattant'.
        
    equipe : str
        L'équipe de cet objet 'combattant'.
        
    pv : int
        Les points de vie restants de cet objet 'combattant'.
        
    deja_touche : boolean
        Cet objet 'combattant' a-t-il déjà ete touché par une attaque ?
        
    actif : boolean
        Cet objet 'combattant' est-il toujours actif
        
    ko : boolean
        Cet objet 'combattant' est-il ko ?
        
    stabilise : boolean
        Cet objet 'combattant' est-il stabilisé ?
        
    jdsvie : int
        Le nombre de jets de sauvegarde contre la mort réussis de cet objet
        'combattant'.
        
    jdsmort : int
        Le nombre de jets de sauvegarde contre la mort échoués de cet objet
        'combattant'.
        
    mort : boolean
        Cet objet 'combattant' est-il mort ?
        
    bonus_initiative : int
        Le bonus pour le calcul d'initiative de cet objet 'combattant'.
        
    initiative : int
        Le score d'initiative de cet objet 'combattant'.
        
    rang_initiative : int
        La rang d'initiative de cet objet 'combattant'.
        
    classe_armure : int
        La valeur de la classe d'armure de cet objet 'combattant'.
        
    nombre_attaques : int
        Le nombre d'attaques permises en un tour de cet objet 'combattant'.
        
    pour_toucher : int
        Le bonus pour toucher de cet objet 'combattant'.
        
    des_pour_toucher : str
        Le(s) dé(s) à lancer pour touchar par cet objet 'combattant' (mais
        c'est toujours '1d20' en fait ...')
        
    critique_a : int
        Score que doit faire cet objet 'combattant' pour faire un coup 
        critique.
        
    bonus_degats : int
        Bonus de dégâts de cet objet 'combattant'.
        
    nombre_des_degats : int
        Nombre de dés de dégat de cet objet 'combattant'.
        
    valeur_des_degats :
        Type de dés de dégats de cet objet 'combattant'.

    Methods
    -------
    None
    
    """
    
    def __init__(self):
        """
        On initialise les attributs par défaut des objets
                             
        """
        self.nom = "Joli petit nom"
        self.equipe = "Equipe"
        self.pv = 1
        self.deja_touche = False
        self.actif = True
        self.ko = False
        self.stabilise = False
        self.jdsvie = 0
        self.jdsmort = 0
        self.mort = False
        self.bonus_initiative = 0
        self.initiative = 0
        self.rang_initiative = 0
        self.classe_armure = 0
        self.nombre_attaques = 1
        self.pour_toucher = 0
        self.des_pour_toucher = "1d20t"
        self.critique_a = 20    # @todo_Critique_a
        self.bonus_degats = 0
        self.nombre_des_degats = 1
        self.valeur_des_degats = 1


ko = []
stabilises = []
morts = []
ennemis_combatants = []
aventuriers_combatants = []


equipe_gagnante = rencontre("combatants.json", 0)
print (f"{equipe_gagnante} gagne")

# BUG
# itterations = 10
# victoires_aventuriers = 0

# for i in range(itterations):
#     equipe_gagnante = rencontre("combatants.json", 0)
#     if equipe_gagnante == "Aventuriers":
#         victoires_aventuriers += 1
# taux_reussite = victoires_aventuriers * 100 / itterations
# print(f"Le taux de réussite des aventuriers est de {taux_reussite} %.")
    
