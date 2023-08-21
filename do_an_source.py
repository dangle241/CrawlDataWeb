
import string
from PyQt5 import QtCore, QtGui, QtWidgets
import requests 
from bs4 import BeautifulSoup

#lấy link từ web
one=''
link_base= "https://careerbuilder.vn/viec-lam/cntt-phan-mem-c1-trang-{}-vi.html"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "\
    "AppleWebKit/537.36  (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}   

list_link=[]
for one in range(1,3):
  item=link_base.format(one)
  list_link.append(item)


class Ui_MainWindow(object):
    def __init__(self):
        self.i=0        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 691, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.jobname_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.jobname_lineEdit.setGeometry(QtCore.QRect(140, 40, 331, 31))
        self.jobname_lineEdit.setObjectName("jobname_lineEdit")
        self.company_name_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.company_name_lineEdit.setGeometry(QtCore.QRect(140, 90, 331, 31))
        self.company_name_lineEdit.setObjectName("company_name_lineEdit")
        self.locatation_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.locatation_lineEdit.setGeometry(QtCore.QRect(140, 140, 331, 31))
        self.locatation_lineEdit.setObjectName("locatation_lineEdit")
        self.search_button = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.search_it())
        self.search_button.setGeometry(QtCore.QRect(510, 40, 93, 31))
        self.search_button.setObjectName("search_button")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 71, 31))
        self.label_3.setObjectName("label_3")
        self.delete_button = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.delete_it())
        self.delete_button.setGeometry(QtCore.QRect(510, 90, 91, 31))
        self.delete_button.setObjectName("delete_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 190, 691, 431))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Print_textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.Print_textEdit.setGeometry(QtCore.QRect(20, 30, 651, 261))
        self.Print_textEdit.setObjectName("Print_textEdit")
        self.print_button = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.print_it())
        self.print_button.setGeometry(QtCore.QRect(510, 140, 93, 31))
        self.print_button.setObjectName("print_button")
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName("menubar")
        self.app = QtWidgets.QMenu(self.menubar)
        self.app.setObjectName("app")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.app.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    

    # hàm xóa
    def delete_it(self):
        self.Print_textEdit.clear()
    #hàm search
    def search_it(self):
        self.print_screen=" "
        self.print_csv=" "
        J_n=self.jobname_lineEdit.text().title()
        C_n=self.company_name_lineEdit.text().title()
        D_c=self.locatation_lineEdit.text().title()
        
        # craw từng page
        for i in range(len(list_link)):
            link=list_link[i]
            r=requests.get(link,headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            jobs =soup.find_all('div',class_="figcaption")
            
        #lấy dữ liệu của từng việc
            for job in jobs :
                company_name=job.find('a',class_="company-name").text.title()
                job_name_1=job.find('a',class_='job_link').text.title().split()
                job_name=' '
                job_name= job_name.join(job_name_1).replace(',','-')
                salary=job.find('div',class_="salary").text.title().replace("  ","")
                location=job.find('div',class_='location').li.text.title()
                more_infor=job.div.h2.a['href']

                if J_n  in job_name and C_n in company_name and D_c in location:
                    str1=f"{company_name},{job_name},{salary},{location},{more_infor},\n "
                    str2=f"Comapany name:{company_name}\n Job name: {job_name}\n Salary: {salary}\n" 
                    "Location: {location}\n More infor: {more_infor}\n\n "      
                    self.print_csv+=str1
                    self.print_screen+=str2
        
        if self.print_screen==" ":
            self.print_screen="not found"        
        self.Print_textEdit.setText(self.print_screen)
    #hàm in  
    def print_it(self):
        self.i+=1
        f = open(f"output{self.i}.csv", "w",encoding="utf-8")
        f.write(self.print_csv)
        f.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Search box"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Job name:"))
        self.label_2.setText(_translate("MainWindow", "Company name:"))
        self.label_3.setText(_translate("MainWindow", "Location:"))
        self.delete_button.setText(_translate("MainWindow", "Delete data"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Print box"))
        self.print_button.setText(_translate("MainWindow", "Print data"))
        self.app.setTitle(_translate("MainWindow", "app"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
