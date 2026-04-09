import sys
import psutil
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel
)
from PyQt6.QtCore import QTimer
from datetime import datetime


class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("uwumonitor")
        self.setGeometry(300, 200, 350, 220)

        # style
        self.apply_neon_style()

        # Layout
        layout = QVBoxLayout()

        # Title
        title = QLabel("uwugui")
        title.setStyleSheet("""
            color: #ff4fd8;
            font-size: 16px;
            font-weight: bold;
            padding: 8px;
        """)
        layout.addWidget(title)

        # Labels
        self.time_label = QLabel()
        self.cpu_label = QLabel()
        self.ram_label = QLabel()
        self.disk_label = QLabel()

        # label styling
        self.time_label.setStyleSheet("color: #ff4fd8; font-weight: bold;")
        self.cpu_label.setStyleSheet("color: #39ff14;")
        self.ram_label.setStyleSheet("color: #39ff14;")
        self.disk_label.setStyleSheet("color: #39ff14;")

        layout.addWidget(self.time_label)
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.disk_label)

        self.setLayout(layout)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def apply_neon_style(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0a0a0a;
                color: #39ff14;
                font-family: Consolas;
                font-size: 14px;
            }

            QLabel {
                padding: 6px;
                margin: 3px;
                border: 1px solid #ff4fd8;
                border-radius: 8px;
                background-color: #111111;
            }
        """)

    def update_stats(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(f"Time: {now}")

        cpu = psutil.cpu_percent()
        self.cpu_label.setText(f"CPU Usage: {cpu}%")

        ram = psutil.virtual_memory()
        self.ram_label.setText(f"RAM Usage: {ram.percent}%")

        disk = psutil.disk_usage("/")
        self.disk_label.setText(f"Disk Usage: {disk.percent}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemMonitor()
    window.show()
    sys.exit(app.exec())
