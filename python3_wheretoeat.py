# =========================================================== #
# Name: Mandl
# Description:
# Simple Python3 script to decide where to go for lunch
# Updated: 28 Nov 2018
# =========================================================== #

import sys
import random as rand

# ui imports
import wheretoeatdesign
from PyQt4 import QtCore,QtGui

# argparse import for adding arguments : https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
import argparse

# data ======================================================= #

lFoodLocations = ["DailyCut",
                  "Subway",
                  "Pho",
                  "iSteaks",
                  "Carls Jr",
                  "FoodBarn",
                  "TwoChefs",
                  "Red"]

lCheapFoodLocations = ["Downstairs",
                       "Guest La Mian",
                       "Grass",
                       "Bread",
                       "Koufu",
                       "FoodMaster"]

# =========================================================== #

class WhereToEatApp(QtGui.QMainWindow, wheretoeatdesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WhereToEatApp, self).__init__(parent)

        # initialise the parser -------------------------------------------------------------------------*
        parser = argparse.ArgumentParser(description="Helps you decide on a place to eat if you cant!")

        parser.add_argument('budget', type=int, nargs='?', help='budget input')                         # this is where you add the additional / required arguments.

        args = vars(parser.parse_args())                                                                # Parse the args
        print(args)
        inputArg = args['budget']
        if inputArg is not None:
            print(self.WhereToEat(inputArg))
        else:
            self.showUI()

        # -----------------------------------------------------------------------------------------------*

    def printHello(self):
        print('code is working')

    def showUI(self):
        self.setupUi(self)
        self.btn_Tellme.clicked.connect(self.showDialog)
        self.btn_Surpriseme.clicked.connect(self.SurpriseMe)

    def updateUI(self, pOutput):
        self.Le_showresult.setText(pOutput)

    def showDialog(self):
        pBudgetValue, UserInput = QtGui.QInputDialog.getInt(self,"Input Budget","Enter it here")
        if UserInput:
            self.updateUI(self.WhereToEat(pBudgetValue))

    def WhereToEat(self, pBudgetValue):
        if pBudgetValue <= 10:
            # places that cost 10 or less
            lCheapListCount = lCheapFoodLocations[:-1]
            cheapnum = len(lCheapListCount)
            cheapPlaceRandomIdx = rand.randint(0, cheapnum)
            cheapLocation = lCheapFoodLocations[cheapPlaceRandomIdx]
            return cheapLocation

        if pBudgetValue >= 11:
            # places that cost 11 or more
            lExListCount = lFoodLocations[:-1]
            exnum = len(lExListCount)
            exPlaceRandomIdx = rand.randint(0, exnum)
            exLocation = lFoodLocations[exPlaceRandomIdx]
            return exLocation

    def SurpriseMe(self):
        lMergedList = lCheapFoodLocations + lFoodLocations
        for eachitem in lMergedList:
            print(eachitem)

def main():
    app = QtGui.QApplication(sys.argv)
    form = WhereToEatApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()