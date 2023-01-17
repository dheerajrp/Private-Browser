import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget


class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Create and set the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and add the URL bar
        self.url_bar = QLineEdit()
        layout.addWidget(self.url_bar)

        # Create and add the web view
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # Create and add the navigation buttons
        nav_layout = QHBoxLayout()
        layout.addLayout(nav_layout)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.web_view.back)
        nav_layout.addWidget(back_button)

        forward_button = QPushButton("Forward")
        forward_button.clicked.connect(self.web_view.forward)
        nav_layout.addWidget(forward_button)

        reload_button = QPushButton("Reload")
        reload_button.clicked.connect(self.web_view.reload)
        nav_layout.addWidget(reload_button)

        # Connect the URL bar to the web view
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Set the default URL
        self.url_bar.setText("https://www.google.com")
        self.navigate_to_url()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.web_view.setUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
