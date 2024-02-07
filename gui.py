import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)
import datetime

class WaitTime(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Estimated Wait Times')
        self.overall=QVBoxLayout()
        self.rides=QHBoxLayout()

        self.ride=QLabel("Ride")
        self.everest=QPushButton('Everest')
        self.everest.clicked.connect(self.ride_selected)
        self.space=QPushButton('Space Mountain')
        self.space.clicked.connect(self.ride_selected)
        self.rock=QPushButton("Rock 'n' Roller Coaster")
        self.rock.clicked.connect(self.ride_selected)

        self.date=datetime.datetime.now()
        self.month=self.date.month
        self.day=self.date.day
        self.hour=self.date.hour
        self.minutes=int(str(self.date.minute)[0])

        self.data=pd.read_csv('all_data.csv', index_col=0)

        self.display=QLabel('')

        self.rides.addWidget(self.everest)
        self.rides.addWidget(self.space)
        self.rides.addWidget(self.rock)

        self.overall.addWidget(self.ride)
        self.overall.addLayout(self.rides)
        self.overall.addWidget(self.display)
        self.setLayout(self.overall)

    def ride_selected(self):
        ride=self.sender()
        if ride==self.everest:
            df=self.data
            df=df[df['ride']=='Everest']
            df=df[df['month']==self.month]
            df=df[df['day']==self.day]
            df=df[df['time'].str[:4]==f'{self.hour}:{self.minutes}']
            mean=df['wait_time'].mean()
            self.display.setText('Estimated wait time: '+ str(mean)[:2]+' minutes.')
        elif ride==self.space:
            df=self.data
            df=df[df['ride']=='Space Mountain']
            df=df[df['month']==self.month]
            df=df[df['day']==self.day]
            df=df[df['time'].str[:4]==f'{self.hour}:{self.minutes}']
            mean=df['wait_time'].mean()
            self.display.setText('Estimated wait time: '+ str(mean)[:2]+' minutes.')
        else:
            df=self.data
            df=df[df['ride']=='Rock N Rollercoaster']
            df=df[df['month']==self.month]
            df=df[df['day']==self.day]
            df=df[df['time'].str[:4]==f'{self.hour}:{self.minutes}']
            mean=df['wait_time'].mean()
            self.display.setText('Estimated wait time: '+ str(mean)[:2]+' minutes.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WaitTime()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
