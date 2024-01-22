from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout
)

from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books | Login')
        self.setFixedSize(700, 700)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
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

        self.text_login = QLabel("Login", self)
        self.text_login.setAlignment(Qt.AlignCenter)
        self.text_login.setStyleSheet("""
        font-size: 30px;
        """)

        self.text_email = QLabel("Email:", self)
        self.text_email.setStyleSheet("""
        font-size: 18px;
        """)
        self.input_email = QLineEdit(self)
        self.input_email.setFixedSize(350, 40)
        self.input_email.setPlaceholderText("Email")

        self.text_password = QLabel("Password:", self)
        self.text_password.setStyleSheet("""
        font-size: 18px;
        """)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)
        self.input_password.setPlaceholderText("Password")

        self.btn_login = QPushButton(self)
        self.btn_login.setFixedHeight(40)
        self.btn_login.setText("Log In")

        self.text_signup = QLabel("Don't have an account?", self)

        self.btn_signup = QPushButton(self)
        self.btn_signup.setFixedHeight(40)
        self.btn_signup.setText("Sign up")

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


        self.show()

    def open_signup(self):
        self.close()
        self.win = SignupWindow()

class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Books | Sign up')
        self.setFixedSize(700, 700)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
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
        self.h_box10 = QHBoxLayout()
        self.h_box11 = QHBoxLayout()
        self.h_box12 = QHBoxLayout()
        self.h_box13 = QHBoxLayout()

        self.text_signup = QLabel("Sign up", self)
        self.text_signup.setAlignment(Qt.AlignCenter)
        self.text_signup.setStyleSheet("""
        font-size: 30px;
        """)

        self.text_name = QLabel("Name:", self)
        self.text_name.setStyleSheet("""
        font-size: 18px;
        """)
        self.input_name = QLineEdit(self)
        self.input_name.setFixedSize(350, 40)
        self.input_name.setPlaceholderText("Name")

        self.text_email = QLabel("Email:", self)
        self.text_email.setStyleSheet("""
        font-size: 18px;
        """)
        self.input_email = QLineEdit(self)
        self.input_email.setFixedSize(350, 40)
        self.input_email.setPlaceholderText("Email")

        self.text_password = QLabel("Password:", self)
        self.text_password.setStyleSheet("""
        font-size: 18px;
        """)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)
        self.input_password.setPlaceholderText("Password")

        self.re_text_password = QLabel("Repeat Password:", self)
        self.re_text_password.setStyleSheet("""
        font-size: 18px;
        """)
        self.re_input_password = QLineEdit(self)
        self.re_input_password.setEchoMode(QLineEdit.Password)
        self.re_input_password.setFixedHeight(40)
        self.re_input_password.setPlaceholderText("Repeat Password")

        self.btn_signup = QPushButton(self)
        self.btn_signup.setFixedHeight(40)
        self.btn_signup.setText("Sign up")

        self.text_login = QLabel("Have an account?", self)

        self.btn_login = QPushButton(self)
        self.btn_login.setFixedHeight(40)
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
        self.v_box.addStretch()
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

        self.btn_login.clicked.connect(self.open_login)

        self.show()

    def open_login(self):
        self.close()
        self.win = LoginWindow()

app = QApplication([])
win = LoginWindow()
app.exec_()
