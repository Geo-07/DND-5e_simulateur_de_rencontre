#!/usr/bin/env python3
"""
Ce programme sert � :
=====================
    Ce programme sert � simuler une renconrte dans Donjons & Dragons 5e.

Usage:
======
    Mettre ici la commande � rentrer avec ses �ventuels arguments

        argument1: un entier signifiant un truc
        argument2: une cha�ne de caract�res signifiant un autre truc
        
        
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
    """Cette classe cr�e un combattant avec tous ses attributs.
    Elle g�re l'attaque et la d�fense de chaque combattant et enregistre son 
    �tat actuel (pv ko, jds contre la mort, stabilis� et mort).
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
        

# Fonction cr�ation de combatant    
def import_combatants(fichier, verbose):
    """
Cette fonction a pour r�le de lire un fichier JSON recensant les combatants et
de cr�er un objet Combatant pour chacun d'entre-eux. Elle est capable de
retourner la liste des combatants dans la console gr�ce au mode verbose.

    Parameters
    ----------
    fichier : Texte
        Nom du fichier au format JSON contenant le liste des combatant
        si r�gl� � "default", prend "combatants.json" comme nom de fichier
    verbose : Boolean (True or False)
        Imprime dans la console la liste des combattants cr��s et leurs 
        �quipes respectives.

    Returns
    -------
    Sortie : List
        Retourne la liste des objets Combatants cr��s en sortie.

    """
    combatants = []
    if fichier == "default":
        fichier = "combatants.json"
        print(f"Le fichier par d�faut est r�gl� sur {fichier}")
    elif not fichier:
        fichier = "combatants.json"
        print("Le fichier n'a pas �t� renseign� !")
        print(f"{fichier} a �t� utilis� par d�faut")
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
            print(f"{c.nom} de l'�quipe {c.equipe} est pr�t(e) au combat")
    return combatants

def calcul_initiative(liste,verbose):
    """
Cette fonction calcule l'initiative pour chaque combatant de la liste en
param�tre, puis les classe par ordre d�croissant d'initiative pour leur
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
        Liste d'objets combatants_tries tri�s par rang d'initiative croissant

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
 {obj.rang_initiative} �quipe : {obj.equipe}")
    for combatant in combatants_tries:
        if combatant.equipe == "Aventuriers": #A reprendre !!!!!
            aventuriers_combatants.append(combatant)
        elif combatant.equipe == "Ennemis":
            ennemis_combatants.append(combatant)
        else:
            print("Les �quipes sont mal d�finies ou les options choisies ne \
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
    Cette fonction permet de g�rer les attaques en combat et de mettre � jour
    les objets relatifs au d�fenseur si ce dernier encaisse des d�g�ts.
    Si un combatant est tu�, on met �galement � jour les listes :
        ko (en l'int�grant dedans)
        ennemis_combatants ou aventuriers_combatants (en l'enlevant de l�)

    Parameters
    ----------
    attaquant : Objet
        Objet attaquant.
    defenseur : Objet
        Objet d�fenseur.
    verbose : Boolean
        Veut-on un retour �crit dans la console des �v�nements ?

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
            print(f"{attaquant.nom} inflige {degats} points de d�gats \
� {defenseur.nom} � qui il reste {defenseur.pv} PV")
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
        #On d�termine l'�quipe du d�fenseur
        if attaquant.equipe == "Aventuriers": #A reprendre !!!!!
            equipe_defenseur = ennemis_combatants
        if attaquant.equipe == "Ennemis":
            equipe_defenseur = aventuriers_combatants
        else:
            print("Les �quipes sont mal d�finies ou les options choisies ne \
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



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
