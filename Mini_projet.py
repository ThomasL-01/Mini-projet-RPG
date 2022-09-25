#Mini-Projet
#Matteo Le Goff; William Smith; Thomas Loureiro; Kyle Lobstein

from random import randint, choice
import time

print('\nBienvenue dans le jeu de rôle,\nVous pourrez choisir une classe de combattant et affronter un adversaire aléatoire.\nBon jeu !')
time.sleep(2)

#class définissant les infos du personnage
class Perso:
    def __init__(self,nom, type,dégats, ptsvie, classe, vitesse = 0, esquive = 0, critiques = 0):
        self.nom = nom
        self.type = type #bot ou joueur
        self.degats = dégats #pts de dégats
        self.pv = ptsvie #Pts de vie lors de la partie (modulables)
        self.speed = vitesse #Vitesse d'attaque (constante)
        self.current_speed = 0 #Vitesse dans la partie (modulable)
        self.classe = classe #Classe du perso
        self.critiques = critiques #Proba de dégats critiques
        self.esquive = esquive #proba d'esquive de l'attaque
        self.compte_attaque = 0 #Pour l'attaque de l'assassin 
        if self.classe == 'mort-vivant': #Pour les réanimations du mort vivant
            self.reanimations = 5
        
    def afficherStats(self): #Affiche les stats du perso
        print("nom :",self.nom)
        print("classe :", self.classe)
        print("force :",self.degats)
        print("pv :", self.pv)
        print("vitesse :", self.speed)
        print("chances de coups critiques :", self.critiques)
        print("chances d'esquive :" ,self.esquive)
        
    def estVivant(self): #verifie si le perso est en vie
        if self.pv <= 0:
            if self.classe == 'mort-vivant': #Dans le cas d'un mort-viant:
                if self.reanimations > 0:
                    self.reanimations -=1
                    self.degats -= 0.10*classes['mort-vivant']['dégats'] #diminution des stats
                    self.speed -= 0.10*classes['mort-vivant']['vitesse']
                    self.pv = classes['mort-vivant']['Vie']
                    if self.type == 'bot':
                        print('Ton adversaire a été réanimé, ses stats ont été diminuées,\nil lui reste',self.reanimations,'réanimation(s)')
                    else:
                        print('Tu as été réanimé, tes stats ont été diminuées,\nil te reste',self.reanimations,'réanimation(s)')
                    time.sleep(2)
                    return True
                else:
                    return False
            else:   
                return False
        else:
            return True
    
    def attaquer(self,persob, crit, esquive_ennemi): #Attaque et esquive des persos
        if self.classe == 'assassin' and self.compte_attaque == 0: #pour la 1ère attaque de l'assassin
            self.compte_attaque += 1
            persob.pv -= 100
            print(self.nom,'a attaqué par surprise, et inflige',100,'dégats à',persob.nom,'!')
            
        elif crit <= self.critiques: #Vérifie si le perso inflige un critique
            self.compte_attaque += 1
            if esquive_ennemi > persob.esquive: #vérifie si le perso esquive (si < a valeure d'esquive il esquive )
                persob.pv -= self.degats *2
                print('Coup Critique !',self.nom, 'a attaqué: -', self.degats*2, "PV à ",persob.nom,'!\n')
            elif esquive_ennemi <= persob.esquive:
                print(persob.nom, "a esquivé l'attaque de",self.nom,'!\n')
        else:
            self.compte_attaque += 1
            if esquive_ennemi > persob.esquive:
                persob.pv -= self.degats
                print(self.nom, 'a attaqué: -', self.degats, "PV à ",persob.nom,'!\n')
            elif esquive_ennemi <= persob.esquive:
                print(persob.nom, "a esquivé l'attaque de",self.nom,'!\n')

#Toutes les classes du jeu avec chacunes leurs spécialitées
classes = {'assassin': {'dégats':20, 'Vie':700, 'vitesse': 25, 'esquive':30, 'critiques':50},
        'guerrier': {'dégats':20, 'Vie':1200, 'vitesse': 20, 'esquive':20, 'critiques':20},
        'mort-vivant': {'dégats':35, 'Vie':180, 'vitesse': 15, 'esquive':15, 'critiques':75},
        }

#Liste de noms choisis aléatoirement pour le bot
liste_noms = ('Gareli', 'Ann-jen','Lauesc','Docceol','Retchel','Habar','Thoga','Comerid','Dangrim','Layguth','Tonwaldbard','Chaelron','Ceored','Limen','Nansyl','Javell','Riera','Ealsara','Vengrim')

#Idem pour les classes du bot choisi aléatoirement
liste_classes = ('assassin', 'guerrier', 'mort-vivant')

a_choisi = False
while not a_choisi:  #permet le choix de la classe au joueur
    joueur_classe = input('\nQuelle classe choisis tu ?\n!help pour afficher les différentes classes et leurs stats ')  
    if joueur_classe == '!help':
        print(' \n classe assassin (inflige des dégats élevés lors de la 1ère attaque et un tour bonus):\n dégats: 20, Vie: 700, vitesse: 25, esquive: 30%, chance de critiques: 50%\n',
            '\n classe guerrier: dégats: 20, Vie: 1200, vitesse: 20, esquive: 20%, chance de critiques: 20% \n',
            '\n classe mort-vivant (a plusieurs vies avec des stats qui diminuent a chaque mort):\n dégats: 35, Vie: 180, vitesse: 15, esquive: 15%, chance de critiques: 75%, réanimations: 5 \n',
            '\nPour attaquer il suffit de taper 1\n\n')
            
    elif joueur_classe == 'classe assassin' or joueur_classe =='Assassin' or joueur_classe =='assassin' or joueur_classe ==' Assassin' or joueur_classe ==' assassin':                
        joueur_classe = 'assassin'
        print('Vous avez choisi la classe ' + joueur_classe)
        a_choisi = True
                
    elif joueur_classe == 'classe guerrier'  or joueur_classe == 'Guerrier' or joueur_classe == 'guerrier' or joueur_classe == ' Guerrier' or joueur_classe == ' guerrier':
        joueur_classe = 'guerrier'
        print('Vous avez choisi la classe ' + joueur_classe)
        a_choisi = True
            
    elif joueur_classe == 'classe mort-vivant' or joueur_classe =='Mort-vivant' or joueur_classe =='mort-vivant' or joueur_classe ==' Mort-vivant' or joueur_classe ==' mort-vivant':
        joueur_classe = 'mort-vivant'
        print('Vous avez choisi la classe ' + joueur_classe)
        a_choisi = True
    
    else:
        print('Commande non comprise')
   
def tour_joueur(): #permet de controler le tour du joueur
    a_joué = False
    time.sleep(1)
    print('Tu as ',joueur.pv,' PV et ton adversaire en a:', bot.pv ,'\n')
    while not a_joué:
        time.sleep(0.5)
        action = input("C'est a toi de jouer. Tu peux: \n1. Attaquer ")
        if action == '1':
            crit = randint(0,100) # si < la valeur de crit alors inflige un crit
            esquive_ennemis = randint(0,100) # si < la valeur d'esquive alors l'adversaire esquive cette attaque (crit ou non)
            #print('joueur:',crit,esquive_ennemis) #pour vérifier les valeurs d'esquive et crit
            joueur.attaquer(bot, crit, esquive_ennemis)
            a_joué = True
        else:
            print('Action non comprise taper 1')
        if joueur.classe == 'assassin':
            if joueur.compte_attaque == 1:
                print('\nTu as une attaque bonus!')
                tour_joueur()
                   
def tour_bot(): #idem pour le bot
    time.sleep(1)
    print("Tour de l'adversaire")
    time.sleep(1)
    crit = randint(0,100)
    esquive_ennemis = randint(0,100)
    #print('bot:',crit,esquive_ennemis)
    bot.attaquer(joueur, crit, esquive_ennemis)
    if bot.classe == 'assassin':
            if bot.compte_attaque == 1:
                print("\nL'adversaire a une attaque bonus!")
                tour_bot()

def combat(perso1,perso2):#permet le combat entre les 2 persos
    en_vie = True
    while en_vie:
        if not perso1.estVivant(): #vérifie si le perso 2 est en vie (ici le joueur)
            en_vie = False
            if perso2.classe == 'mort-vivant':
                print('Tu as ',perso2.pv,'PV avec',perso2.reanimations,'réanimations restantes et ton adversaire a',0 ,'PV\n')
            else:
                print('Tu as',perso2.pv,'PV restants et ton adversaire en a',0,'\n')
            print('Vous avez gagné !\n')
        if not perso2.estVivant(): #vérifie si le perso 1 est en vie (ici le bot)
            en_vie = False
            if perso1.classe == 'mort-vivant':
                print('Tu as ',0,' PV et ton adversaire en a', perso1.pv ,'avec',perso1.reanimations,'réanimations restantes\n')
            else:
                print('Tu as',0,'PV restants et ton adversaire en a',perso1.pv,'\n')
            print(perso1.nom,'a gagné !\n')
        else: #permet la succesion des tours joueurs et bots
            perso1.current_speed += perso1.speed
            perso2.current_speed += perso2.speed
            if perso1.current_speed >= 100: #vérifie si tour du bot
                tour_bot()
                perso1.current_speed -= 100
            elif perso2.current_speed >= 100: # idem  tour joueur
                tour_joueur()
                perso2.current_speed -= 100   
         
nom_j = input('Comment vous appelez vous ? ')
#cretaion du joueur et du personnage
joueur = Perso(nom_j, 'joueur', classes[joueur_classe]['dégats'], classes[joueur_classe]['Vie'], joueur_classe,classes[joueur_classe]['vitesse'],classes[joueur_classe]['esquive'], classes[joueur_classe]['critiques'])

classe_bot = choice(liste_classes)
bot = Perso(choice(liste_noms),'bot',classes[classe_bot]['dégats'],classes[classe_bot]['Vie'],classe_bot ,classes[classe_bot]['vitesse'],classes[classe_bot]['esquive'], classes[classe_bot]['critiques'])

print('Votre adversaire est:', bot.nom, classe_bot)

combat(bot,joueur)