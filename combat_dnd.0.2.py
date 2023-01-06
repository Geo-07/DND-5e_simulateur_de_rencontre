#!/usr/bin/env python3
"""
Ce programme sert à :
=====================
    Ce programme sert à simuler une renconrte dans Donjons & Dragons 5e.

Usage:
======
    Mettre ici la commande à rentrer avec ses éventuels arguments

        argument1: un entier signifiant un truc
        argument2: une chaîne de caractères signifiant un autre truc
        
        
Created on : Sun Jan  1 10:04:20 2023
============
"""
# -*- coding: utf-8 -*-

__authors__ = ("Geo_07")
__contact__ = ("geo.zerosept@gmail.com")
__copyright__ = "CC-BY-SA"
__date__ = "2023-01-01"
__version__= "0.2"


import dice
import json

ko = []
stabilises = []
morts = []
ennemis_combatants = []
aventuriers_combatants = []



class Combatant:
    """Cette classe crée un combattant avec tous ses attributs.
    Elle gère l'attaque et la défense de chaque combattant et enregistre son 
    état actuel (pv ko, jds contre la mort, stabilisé et mort).
    """
    
    def __init__(self,
                  # nom,         A VIRER SI PAS UTILE
                  # equipe,      ====================
                  # pv,
                  # deja_touche,
                  # actif,
                  # ko,
                  # stabilise,
                  # jdsvie,
                  # jdsmort,
                  # mort,
                  # bonus_initiative,
                  # initiative,
                  # rang_initiative,
                  # classe_armure,
                  # nombre_attaques,
                  # pour_toucher,
                  # des_pour_toucher,
                  # critique_a,
                  # bonus_degats,
                  # nombre_des_degats,
                  # valeur_des_degats
                 ):
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
        self.critique_a = 20
        self.bonus_degats = 0
        self.nombre_des_degats = 1
        self.valeur_des_degats = 1
        

# Fonction création de combatant    
def import_combatants(fichier, verbose):
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
    if verbose:
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
    if verbose:
        for obj in combatants_tries:
            print(f"{obj.nom} : initiative {obj.initiative} rang\
 {obj.rang_initiative} équipe : {obj.equipe}")
    for combatant in combatants_tries:
        if combatant.equipe == "Aventuriers": #A reprendre !!!!!
            aventuriers_combatants.append(combatant)
        elif combatant.equipe == "Ennemis":
            ennemis_combatants.append(combatant)
        else:
            print("Les équipes sont mal définies ou les options choisies ne \
                  sont pas prises en charge") 
    print("Liste des ennemis :")
    for comb in ennemis_combatants:
        print(comb.nom)
    print("Liste des aventuriers :")
    for comb in aventuriers_combatants:
        print(comb.nom)
    return combatants_tries


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
    print(f"pour toucher : {pour_toucher}, degats : {degats}, ca : \
{defenseur.classe_armure}")
    if defenseur.classe_armure <= pour_toucher:
        defenseur.pv = defenseur.pv - degats
        defenseur.touche = True
        if verbose:
            print(f"{attaquant.nom} inflige {degats} points de dégats \
à {defenseur.nom} à qui il reste {defenseur.pv} PV")
    else:
        if verbose:
            print(f"{attaquant.nom} rate son attaque contre {defenseur.nom}")
    if defenseur.pv <= 0:
        defenseur.ko = True
        initiative.remove(defenseur)
        if defenseur.equipe == "Ennemis":
            ennemis_combatants.remove(defenseur)
        elif defenseur.equipe == "Aventuriers":
            aventuriers_combatants.remove(defenseur)
        ko.append(defenseur)
        if verbose:
            print(f"{attaquant.nom} met KO {defenseur.nom} !!!")
    
       
def combat(initiative, verbose):
    for attaquant in initiative: #Objet attaquant selon rang d'initiative
        #On détermine l'équipe du défenseur
        if attaquant.equipe == "Aventuriers": #A reprendre !!!!!
            equipe_defenseur = ennemis_combatants
        if attaquant.equipe == "Ennemis":
            equipe_defenseur = aventuriers_combatants
        else:
            print("Les équipes sont mal définies ou les options choisies ne \
                  sont pas prises en charge")
        if len(equipe_defenseur) > 0:
            for i in range(attaquant.nombre_attaques):
                # attaque(attaquant, equipe_defenseur[1], verbose) 
                print(equipe_defenseur[1].nom)
                i = i+1 
            
                

combatants = import_combatants("combatants_low_pv.json",0)
initiative = calcul_initiative(combatants, True)
combat(initiative, True)
# attaque (initiative[1], initiative[2], True)
for joueurs_vivants in ko:
    print(joueurs_vivants.nom)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
