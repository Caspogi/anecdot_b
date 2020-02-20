import urllib.request
from bs4 import BeautifulSoup
import re
import sys
from pyqt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                            QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    resp = urllib.request.urlopen('http://baneks.ru/random')  # download html file
    html = resp.read()
    soup = BeautifulSoup(html, 'html.parser')  # cooking soup
    anek = soup.find_all('p')
    anek = re.sub(r'<b>', '', re.sub(r'<br/>', '', re.sub(r'</p>', '', re.sub(r'<p>', '', str(anek[0])))))
    print(anek)
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())