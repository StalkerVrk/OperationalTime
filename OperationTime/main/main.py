import time
from typing import Text
from kivy.lang.builder import Instruction
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock


class Digt(ScreenManager):
    pass

class Main(MDApp):
    count = time.time()
    count2 = 0

    def updateTime(self, *args):
        localTime = time.ctime(self.count)[11:-5] + "   " + time.ctime(self.count)[8:10] + "." + Main.convertedTime(self.count) + "." + time.ctime(self.count)[20:]
        self.count = self.count + 1
        self.root.ids.localTime.text = localTime
        
        self.count2 = self.count2 + 1
        oper_time = time.ctime(self.count2)[11:-5] + "   " + time.ctime(self.count2)[8:10] + "." + Main.convertedTime(self.count2)+"." + time.ctime(self.count2)[20:]
        self.root.ids.operationTime.text = oper_time
        
    def convertedTime(number):
        readyValue = ''
        month = [["Jan","01"],
        ["Feb","02"],
        ["Mar","03"],
        ["Apr","04"],
        ["May","05"],
        ["June","06"],
        ["July","07"],
        ["Aug","08"],
        ["Sept","09"],
        ["Oct","10"],
        ["Nov","11"],
        ["Dec","12"],
        ]
        for i in range(len(month)):
            if (time.ctime(number).split(" "))[1] == month[i][0]:
                readyValue += month[i][1]
        
        return(readyValue)

    def getTime(self):
        global readyTime
        readyTime = (self.root.ids.getTime.text).split(" ") 
        try:
            valuesTimesForOperTime = (
                                    int(readyTime[0]), 
                                    int(readyTime[1]), 
                                    int(readyTime[2]), 
                                    int(readyTime[3]), 
                                    int(readyTime[4]),
                                    int(readyTime[5]),
                                    0, 
                                    362, 
                                    0)
            operTime = time.mktime(valuesTimesForOperTime) 
            self.count2 = operTime
        except BaseException:
            print("Неверный ввод")

    def addOperTime(self, data):
        data.text = "test"

    def build(self):
        Clock.schedule_interval(self.updateTime,1)
        Builder.load_file("digital.kv")
        return Digt()
    
Main().run()