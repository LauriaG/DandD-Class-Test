# -*- coding: utf-8 -*-
"""
Created on Tue May  29 02:34:47 2018

@author: Gabriel Lauria
"""

from sklearn import tree

#We want to predict which D&D class has more in common
#with the players based on their characteristics

classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

#classType    
#           ->  0 = battlers
#               1 = spellcasters
#attack     ->  0 = melee
#               1 = ranged
#               2 = both
#primarySkill
#           ->  0 = strength
#               1 = dexterity
#               2 = intelligence
#               3 = wisdom
#               4 = charisma
#               5 = constitution
#secondarySkill
#           -> same as above

characteristicsDictionary = [
                                ["class type", "0 for battlers\n1 for spellcasters"],
                                ["attack", "0 for melee\n1 for ranged\n2 for both"],
                                ["primary skill",
                                    "0 for strength\n1 for dexterity\n2 for intelligence\n3 for wisdom\n4 for charisma\n5 for constitution"],
                                ["secondary skill",
                                    "0 for strength\n1 for dexterity\n2 for intelligence\n3 for wisdom\n4 for charisma\n5 for constitution"]
                            ]

classesCharacteristics = [
                            [0, 0, 0, 5], #barbarian
                            [1, 2, 1, 4], #bard
                            [1, 1, 3, 4], #cleric
                            [1, 0, 2, 3], #druid
                            [0, 0, 0, 5], #fighter
                            [0, 0, 0, 1], #monk
                            [0, 0, 3, 4], #paladin
                            [0, 2, 0, 1], #ranger
                            [0, 2, 1, 2], #rogue
                            [1, 1, 5, 4], #sorcerer
                            [1, 1, 3, 4], #warlock
                            [1, 1, 2, 3] #wizard
                        ]

class Player:
    characteristics = [None] * len (characteristicsDictionary)
    classPrediction = None

    def fillPlayerCharacteristics (self, characteristicsDictionary):
        for i in range(len(characteristicsDictionary)):
            print ("\n" + characteristicsDictionary [i][0] + ":")
            print (characteristicsDictionary [i][1])
            self.characteristics [i] = int (input ("Enter with your " + characteristicsDictionary [i][0] + " number: "))

            #check if the input is valid
            #while (self.characteristics [i] > 5) or (self.characteristics < 0):
                #print ("\n\tWarning!")
                #print ("Invalid value: " + str (self.characteristics [i]))
                #print ("Enter with a valid value!")

                #print ("\n" + characteristicsDictionary [i][0] + ":")
                #print (characteristicsDictionary [i][1])
                #self.characteristics [i] = int (input ("Enter with your " + characteristicsDictionary [i][0] + " number: "))

        #check if secundary skill == primary skill
        while self.characteristics [-1] == self.characteristics [-2]:
            print ("\n\tWarning!")
            print ("Secondary skill must be different from primary!")
            print ("Your primary skill number is ", self.characteristics [-2])
            print ("\n" + characteristicsDictionary [-1][0] + ":")
            print (characteristicsDictionary [-1][1])
            self.characteristics [-1] = int (input ("Enter with your " + characteristicsDictionary [-1][0] + " number: "))

class Quiz:
    clfTree = tree.DecisionTreeClassifier ()
    
    def ask (self, player, characteristicsDictionary):
        player.fillPlayerCharacteristics (characteristicsDictionary)

    def predict (self, player, classes, classesCharacteristics):
        self.clfTree = self.clfTree.fit (classesCharacteristics, classes)
        player.classPrediction = self.clfTree.predict ([player.characteristics])

    def showResult (self, player, classes):
        print ("You should be a " + player.classPrediction [0] + "!")

def printTittle ():
    print ("#" * 22)
    print ("#D&D Class predictor!#")
    print ("#" * 22)

def startQuiz (classes, classesCharacteristics):
    player = Player ()
    quiz = Quiz ()
    quiz.ask (player, characteristicsDictionary)
    quiz.predict (player, classes, classesCharacteristics)
    quiz.showResult (player, classes)

#########################################################################################################################

#########################################################################################################################

printTittle ()
startQuiz (classes, classesCharacteristics)
