import os, sys

from time import sleep

from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication( sys.argv )

def copyFile() :
    cpBtn.setDisabled( True )
    for i in range( 0, 100 ) :
        # File Copy Code
        # sleep( 0.1 ) is instead of the file copy code
        sleep( 0.1 )
        pb.setValue( i + 1 )
        qApp.processEvents()

    cpBtn.setEnabled( True )
    pb.reset()

fcpDlg = QDialog()

cpBtn = QPushButton( fcpDlg )
cpBtn.setText( "Download" )
cpBtn.clicked.connect( copyFile )
cpBtn.setFixedWidth( 72 )

pb = QProgressBar()
pb.setMinimumWidth( 300 )
pb.setRange( 0, 100 )

lyt = QVBoxLayout( fcpDlg )
lyt.addWidget( pb )
lyt.addWidget( cpBtn )

fcpDlg.setLayout( lyt )

fcpDlg.show()

sys.exit( app.exec_() )