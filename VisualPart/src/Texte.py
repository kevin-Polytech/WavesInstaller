import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


app = QApplication(sys.argv)

champ = QLineEdit("Voici mon premier champ de texte")
champ.show()

app.exec_()