from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QCheckBox
)

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from core import Core

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books | Login')
        self.setFixedSize(700, 700)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #F8FAE5;
        """)

        self.v_box = QVBoxLayout()
        self.v_box2 = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()
        self.h_box7 = QHBoxLayout()
        self.h_box8 = QHBoxLayout()
        self.h_box9 = QHBoxLayout()

        self.core = Core()

        self.text_login = QLabel("Login", self)
        self.text_login.setAlignment(Qt.AlignCenter)
        self.text_login.setStyleSheet("""
        font-size: 30px;
        color: #76453B;
        """)

        self.text_email = QLabel("Email:", self)
        self.text_email.setStyleSheet("""
        color: #76453B;
        font-size: 18px;
        """)
        self.input_email = QLineEdit(self)
        self.input_email.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.input_email.setFixedSize(350, 40)
        self.input_email.setPlaceholderText("Email")

        self.text_password = QLabel("Password:", self)
        self.text_password.setStyleSheet("""
        color: #76453B;
        font-size: 18px;
        """)
        self.input_password = QLineEdit(self)
        self.input_password.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)
        self.input_password.setPlaceholderText("Password")

        self.h_shower = QHBoxLayout()
        self.checkbox_password = QCheckBox("Show", self)
        self.checkbox_password.setStyleSheet("""
        color: #76453B;
        """)
        self.h_shower.addStretch()
        self.h_shower.addWidget(self.checkbox_password)

        self.btn_login = QPushButton(self)
        self.btn_login.setFixedHeight(40)
        self.btn_login.setStyleSheet("""
        QPushButton {
            background-color: #43766C;
            color: #FFF;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #33665C;
        }
        """)
        self.btn_login.setText("Log In")

        self.text_signup = QLabel("Don't have an account?", self)
        self.text_signup.setStyleSheet("""
        color: #76453B;
        """)

        self.btn_signup = QPushButton(self)
        self.btn_signup.setFixedHeight(40)
        self.btn_signup.setStyleSheet("""
        QPushButton {
            background-color: #43766C;
            color: #FFF;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #33665C;
        }
        """)
        self.btn_signup.setText("Sign up")

        #status
        self.h_status = QHBoxLayout()
        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignCenter)
        self.h_status.addWidget(self.status)

        self.h_box1.addWidget(self.text_login)
        self.h_box2.addWidget(self.text_email)
        self.h_box3.addWidget(self.input_email)
        self.h_box4.addWidget(self.text_password)
        self.h_box5.addWidget(self.input_password)
        self.h_box6.addWidget(self.btn_login)
        self.h_box7.addWidget(self.text_signup)
        self.h_box8.addWidget(self.btn_signup)

        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_shower)
        self.v_box.addLayout(self.h_status)
        self.v_box.addLayout(self.h_box6)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box7)
        self.v_box.addLayout(self.h_box8)
        self.v_box.addStretch()

        self.h_box9.addStretch()
        self.h_box9.addLayout(self.v_box)
        self.h_box9.addStretch()

        self.v_box2.addLayout(self.h_box9)

        self.setLayout(self.v_box2)

        self.btn_signup.clicked.connect(self.open_signup)
        self.checkbox_password.stateChanged.connect(self.clickBox)
        self.btn_login.clicked.connect(self.check)


        self.show()

    def check(self):
        email = self.input_email.text()
        password = self.input_password.text()
        res = self.core.check_email(email)

        if not email and not password:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Fill empty spaces")
            QTimer.singleShot(3000, self.remove_label)
        else:
            try:
                if len(res[0][0]) > 0:
                    if res[0][1] != password:
                        self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                            """)
                        self.status.setText("Password is wrong")
                    else:
                        self.status.setStyleSheet("""
                            background-color: #198754;
                            color: #FFF;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                            """)
                        self.status.setText("Logged in")
                        QTimer.singleShot(2000, self.open_main)

                QTimer.singleShot(1000, self.remove_label)
            except Exception:
                self.status.setStyleSheet("""
                    background-color: #FFC107;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("Email is wrong")

            QTimer.singleShot(3000, self.remove_label)

    def open_main(self):
        self.win = MainWindow()
        self.close()

    def clickBox(self, state):
        if state == Qt.Checked:
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    def open_signup(self):
        self.close()
        self.win = SignupWindow()

    def remove_label(self):
        self.status.setStyleSheet("")
        self.status.setText("")

class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books | Sign up')
        self.setFixedSize(700, 700)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #F8FAE5;
        """)

        self.core = Core()

        self.v_box = QVBoxLayout()
        self.v_box2 = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()
        self.h_box7 = QHBoxLayout()
        self.h_box8 = QHBoxLayout()
        self.h_box9 = QHBoxLayout()
        self.h_box10 = QHBoxLayout()
        self.h_box11 = QHBoxLayout()
        self.h_box12 = QHBoxLayout()
        self.h_box13 = QHBoxLayout()

        #status
        self.h_status = QHBoxLayout()
        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignCenter)
        self.h_status.addWidget(self.status)

        self.text_signup = QLabel("Sign up", self)
        self.text_signup.setAlignment(Qt.AlignCenter)
        self.text_signup.setStyleSheet("""
        font-size: 30px;
        color: #76453B;
        """)

        self.text_name = QLabel("Name:", self)
        self.text_name.setStyleSheet("color: #76453B;")
        self.input_name = QLineEdit(self)
        self.input_name.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.input_name.setFixedSize(350, 40)
        self.input_name.setPlaceholderText("Name")

        self.text_email = QLabel("Email:", self)
        self.text_email.setStyleSheet("color: #76453B;")
        self.input_email = QLineEdit(self)
        self.input_email.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.input_email.setFixedSize(350, 40)
        self.input_email.setPlaceholderText("Email")

        self.text_password = QLabel("Password:", self)
        self.text_password.setStyleSheet("color: #76453B;")
        self.input_password = QLineEdit(self)
        self.input_password.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)
        self.input_password.setPlaceholderText("Password")

        self.h_shower = QHBoxLayout()
        self.checkbox_password = QCheckBox("Show", self)
        self.checkbox_password.setStyleSheet("color: #76453B;")
        self.h_shower.addStretch()
        self.h_shower.addWidget(self.checkbox_password)

        self.re_text_password = QLabel("Repeat Password:", self)
        self.re_text_password.setStyleSheet("color: #76453B;")
        self.re_input_password = QLineEdit(self)
        self.re_input_password.setStyleSheet("""
        QLineEdit {
            border: 2px solid #B19470;
            border-radius: 10px;
        }
        QLineEdit:hover {
            border-color: #917450;
        }
        """)
        self.re_input_password.setEchoMode(QLineEdit.Password)
        self.re_input_password.setFixedHeight(40)
        self.re_input_password.setPlaceholderText("Repeat Password")

        self.btn_signup = QPushButton(self)
        self.btn_signup.setFixedHeight(40)
        self.btn_signup.setStyleSheet("""
        QPushButton {
            background-color: #43766C;
            color: #FFF;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #33665C;
        }
        """)
        self.btn_signup.setText("Sign up")

        self.text_login = QLabel("Have an account?", self)
        self.text_login.setStyleSheet("color: #76453B;")

        self.btn_login = QPushButton(self)
        self.btn_login.setFixedHeight(40)
        self.btn_login.setStyleSheet("""
        QPushButton {
            background-color: #43766C;
            color: #FFF;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: #33665C;
        }
        """)
        self.btn_login.setText("Log in")

        self.h_box1.addWidget(self.text_signup)
        self.h_box2.addWidget(self.text_name)
        self.h_box3.addWidget(self.input_name)
        self.h_box4.addWidget(self.text_email)
        self.h_box5.addWidget(self.input_email)
        self.h_box6.addWidget(self.text_password)
        self.h_box7.addWidget(self.input_password)
        self.h_box8.addWidget(self.re_text_password)
        self.h_box9.addWidget(self.re_input_password)
        self.h_box10.addWidget(self.btn_signup)
        self.h_box11.addWidget(self.text_login)
        self.h_box12.addWidget(self.btn_login)

        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)
        self.v_box.addLayout(self.h_box7)
        self.v_box.addLayout(self.h_box8)
        self.v_box.addLayout(self.h_box9)
        self.v_box.addLayout(self.h_shower)
        self.v_box.addLayout(self.h_status)
        self.v_box.addLayout(self.h_box10)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box11)
        self.v_box.addLayout(self.h_box12)
        self.v_box.addStretch()

        self.h_box13.addStretch()
        self.h_box13.addLayout(self.v_box)
        self.h_box13.addStretch()

        self.v_box2.addLayout(self.h_box13)

        self.setLayout(self.v_box2)

        self.btn_signup.clicked.connect(self.create_user)
        self.btn_login.clicked.connect(self.open_login)
        self.checkbox_password.stateChanged.connect(self.clickBox)

        self.show()

    def clickBox(self, state):
        if state == Qt.Checked:
            self.input_password.setEchoMode(QLineEdit.Normal)
            self.re_input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)
            self.re_input_password.setEchoMode(QLineEdit.Password)

    def open_login(self):
        self.close()
        self.win = LoginWindow()

    def create_user(self):
        name = self.input_name.text()
        email = self.input_email.text()
        password = self.input_password.text()
        re_password = self.re_input_password.text()

        if name and email and password and name[0].isalpha() and len(name) > 1 and self.email_checker(email) and len(password) >= 8 and re_password == password and self.space_checker(name) and self.space_checker(email) and self.space_checker(password):
            result = self.core.insert_data(name, email, password)
            if result == False:
                self.status.setStyleSheet("""
                    background-color: #DC3545;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("User already exists")
            else:
                self.status.setStyleSheet("""
                    background-color: #198754;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("Signed up")
                QTimer.singleShot(3000, self.open_main)
        elif ' ' in name or ' ' in email or ' ' in password:
            if ' ' in name:
                self.status.setStyleSheet("""
                    background-color: #FFC107;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("Write name without space")
            elif ' ' in email:
                self.status.setStyleSheet("""
                    background-color: #FFC107;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("Write email without space")
            elif ' ' in password or ' ' in re_password:
                self.status.setStyleSheet("""
                    background-color: #FFC107;
                    color: #FFF;
                    font-weight: bold;
                    padding-top: 10px;
                    padding-bottom: 10px;
                    border-radius: 10px;
                    """)
                self.status.setText("Write password without space")
        elif name and not name[0].isalpha():
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Name is wrong")
        elif email and not self.email_checker(email):
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Email is wrong")
        elif 0 < len(password) < 8:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFC107;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Password min length 8")
        elif re_password != password:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Passwords doesn't match")
        else:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
                """)
            self.status.setText("Fill empty spaces")

        QTimer.singleShot(3000, self.remove_label)

    def open_main(self):
        self.window = MainWindow()
        self.close()
    def email_checker(self, email) -> bool:
        if email[0].isalpha() and '@' in email and '.' in email and email[-1].isalpha():
            index = email.index('@')
            if email[index+1] != '.' and email.count('@') == 1 and email.count('.') == 1 and index < email.index('.'):
                symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '~', '`', '/', ':', ';', ',', '|', '?', '<', '>', '{', '}', '[', ']', "'"]
                for i in symbols:
                    if i in email:
                        return False
                return True
            else:
                return False
        else:
            return False

    def space_checker(self, text):
        if ' ' in text:
            return False
        else:
            return True

    def remove_label(self):
        self.status.setStyleSheet("")
        self.status.setText("")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 700)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        """)

        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()

        self.loading_label = QLabel(self)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.h_box1.addWidget(self.loading_label)

        movie = QMovie("Spinner-1s-203px.gif")
        self.loading_label.setMovie(movie)
        movie.start()

        self.v_box.addLayout(self.h_box1)
        self.setLayout(self.v_box)

        self.show()


app = QApplication([])
win = LoginWindow()
app.exec_()
