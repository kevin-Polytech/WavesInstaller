import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window(a,b,c):
    app = QApplication(sys.argv)
    fenetre= QWidget()
    
    fenetre.setGeometry(400,a,b,c)
    fenetre.setWindowTitle("Waves")
    fenetre.show()
    sys.exit(app.exec_())
    

    
if __name__ == '__main__':
    window(150,600,400)
    