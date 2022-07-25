import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt, QLine

import prediction_file

class Hearth(QWidget):
    
    def __init__(self) -> None :
        
        super(Hearth, self).__init__()
        self.sub_head = QLabel("Hearth Attack Predector")
        self.sub_head.setFont(QFont("Times",24, weight=QFont.Bold))
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.l6 = QLineEdit()
        self.l7 = QLineEdit()
        self.l8 = QLineEdit()
        self.l9 = QLineEdit()
        self.l10 = QLineEdit()
        self.l11 = QLineEdit()
        self.l12 = QLineEdit()
        self.t0 = QLabel("1.age:")
        self.t1 = QLabel("2.sex(1=male, 0=female):")
        self.t2 = QLabel("3.cp(0, 1, 2, 3):")
        self.t3 = QLabel("4.trestbps:")
        self.t4 = QLabel("5.chol:")
        self.t5 = QLabel("6.fbs(1=true, 0=false):")
        self.t6 = QLabel("7.restecg(0, 1, 2):")
        self.t7 = QLabel("8.thalach:")
        self.t8 = QLabel("9.exang(1=yes, 0=no):")
        self.t9 = QLabel("10.oldpeak:")
        self.t10 = QLabel("11.slope:")
        self.t11 = QLabel("12.thal:")
        self.t12 = QLabel("13.ca:")
        self.h0 = QHBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        self.h8 = QHBoxLayout()
        self.h9 = QHBoxLayout()
        self.h10 = QHBoxLayout()
        self.h11 = QHBoxLayout()
        self.h12 = QHBoxLayout()
        self.clbtn = QPushButton("CLEAR")
        self.clbtn.setFixedWidth(100)
        self.submit = QPushButton("SUBMIT")
        self.submit.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()
        
    def initui(self) -> None:
        
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l0.setValidator(QDoubleValidator())
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l6.setValidator(QDoubleValidator())
        self.l7.setValidator(QDoubleValidator())
        self.l8.setValidator(QDoubleValidator())
        self.l9.setValidator(QDoubleValidator())
        self.l10.setValidator(QDoubleValidator())
        self.l11.setValidator(QDoubleValidator())
        self.l12.setValidator(QDoubleValidator())
        self.l0.setFixedSize(40,30)
        self.l1.setFixedSize(40,30)
        self.l2.setFixedSize(40,30)
        self.l3.setFixedSize(40,30)
        self.l4.setFixedSize(40,30)
        self.l5.setFixedSize(40,30)
        self.l6.setFixedSize(40,30)
        self.l7.setFixedSize(40,30)
        self.l8.setFixedSize(40,30)
        self.l9.setFixedSize(40,30)
        self.l10.setFixedSize(40,30)
        self.l11.setFixedSize(40,30)
        self.l12.setFixedSize(40,30)
        
        self.h0.addWidget(self.t0)
        self.h0.addWidget(self.l0)
        self.v1_box.addLayout(self.h0)
        
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.v1_box.addLayout(self.h1)
        
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.v1_box.addLayout(self.h2)
        
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.v1_box.addLayout(self.h3)
        
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
        self.v1_box.addLayout(self.h4)
        
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.v1_box.addLayout(self.h5)
        
        self.h6.addWidget(self.t6)
        self.h6.addWidget(self.l6)
        self.v1_box.addLayout(self.h6)
        
        self.h7.addWidget(self.t7)
        self.h7.addWidget(self.l7)
        self.v1_box.addLayout(self.h7)
        
        self.h8.addWidget(self.t8)
        self.h8.addWidget(self.l8)
        self.v1_box.addLayout(self.h8)
        
        self.h9.addWidget(self.t9)
        self.h9.addWidget(self.l9)
        self.v1_box.addLayout(self.h9)
        
        self.h10.addWidget(self.t10)
        self.h10.addWidget(self.l10)
        self.v1_box.addLayout(self.h10)
        
        self.h11.addWidget(self.t11)
        self.h11.addWidget(self.l11)
        self.v1_box.addLayout(self.h11)
        
        self.h12.addWidget(self.t12)
        self.h12.addWidget(self.l12)
        self.v1_box.addLayout(self.h12)
        
        self.hr = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.hr.addWidget(self.submit)
        self.hr.addWidget(self.clbtn)
        self.v1_box.addLayout(self.hr)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(10)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)
        
    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("About")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times",24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel("This model uses Logistic Regression.\nAccuracy of model: %85 ")
        self.details.setFont(QFont("Arial",14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        
    def clfn(self):
        
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.l6.clear()
        self.l7.clear()
        self.l8.clear()
        self.l9.clear()
        self.l10.clear()
        self.l11.clear()
        self.l12.clear()
        self.report_subhead.setText("About")
        self.results.setText(" ")
        self.details.setText("This model uses Logistic Regression.\nAccuracy of model: %85")
        
    def test_input(self) -> None:
        
        my_dict = {"age":float(self.l0.text()), 
                   "sex":float(self.l1.text()),
                   "cp":float(self.l2.text()), 
                   "trestbps":float(self.l3.text()),
                   "chol":float(self.l4.text()),
                   "fbs":float(self.l5.text()),
                   "restecg":float(self.l6.text()),
                   "thalach":float(self.l7.text()),
                   "exang":float(self.l8.text()),
                   "oldpeak":float(self.l9.text()),
                   "slope":float(self.l10.text()),
                   "ca":float(self.l11.text()),
                  "thal":float(self.l12.text()),}
        output = prediction_file.check_input(my_dict)
        
        if output==0:
            self.results.setText("No Hearth Attack.")
        else:
            self.results.setText("Heart Attack.\nPlease get checked soon.")
            
        
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))           

    def mwindow(self) -> None:
        
        self.setFixedSize(800, 800)
        self.setWindowTitle("Hearth Attack Predector")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Hearth()
    a_window.mwindow()
    sys.exit(app.exec_())