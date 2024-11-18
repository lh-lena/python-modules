from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
import sys

#Main Window  
class App(QWidget):  
   def __init__(self):  
      super().__init__()  
      # Setting the title  
      self.title = 'Scorpion'  
      # Setting the Position  
      self.left = 0  
      self.top = 0  
      self.width = 400  
      self.height = 250  

      self.setWindowTitle(self.title)  
      self.setGeometry(self.left, self.top, self.width, self.height) 
      # introducing a table  
      self.creatingTable()  
   
      # Adding Widgets  
      self.layout = QVBoxLayout()  
      self.layout.addWidget(self.tableNew)  
      self.setLayout(self.layout)  
   
      # Displaying the window  
      self.show()  
  
#Creating the table  
def creatingTable(self):  
   self.tableNew = QTableWidget()  

   # Giving the count for the Row   
   self.tableNew.setRowCount(4)  

   # Giving the count for the Column  
   self.tableNew.setColumnCount(2)  

   self.tableNew.setItem(0, 0, QTableWidgetItem("Cell(1,1)"))  
   self.tableNew.setItem(0, 1, QTableWidgetItem("Cell(1,2)"))  
   self.tableNew.setItem(1, 0, QTableWidgetItem("Cell(2,1)"))  
   self.tableNew.setItem(1, 1, QTableWidgetItem("Cell(2,2)"))  
   self.tableNew.setItem(2, 0, QTableWidgetItem("Cell(3,1)"))  
   self.tableNew.setItem(2, 1, QTableWidgetItem("Cell(3,2)"))  
   self.tableNew.setItem(3, 0, QTableWidgetItem("Cell(4,1)"))  
   self.tableNew.setItem(3, 1, QTableWidgetItem("Cell(4,2)"))  
  
# Adjusting the horizontal fir of the table  
   self.tableNew.horizontalHeader().setStretchLastSection(True)  
   self.tableNew.horizontalHeader().setSectionResizeMode(  
      QHeaderView.Stretch)  

def keyPressEvent(self, e):
   print(e.key())
   if e.key() == Qt.Key_Escape:
      self.close()

App.keyPressEvent = keyPressEvent
App.creatingTable = creatingTable

if __name__ == '__main__':  
  
   # creating the pyqt5 application      
   base = QApplication(sys.argv)  

   # creating an instance of the created Window  
   window = App()  

   # starting the application   
   sys.exit(base.exec_())  