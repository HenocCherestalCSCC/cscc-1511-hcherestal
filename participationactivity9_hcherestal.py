'''
Program Name: Device Tracker Example 
Author: Henoc Cherestal 
Purpose: This program creates a class that models an IT device that someone might use everyday, like a laptop or desktop. 
This class stores data about the device
and has funcitons that let me view and change that data. 
''' 

class Device:
    def __init__(self, name, status):
        self.name = name 
        self.status = status 
    
    def show_info(self): 
        print(f"Device: {self.name}")
        prirint(f"Status: {self.status}")

    def change_status(self, new_status):
        self.status = new_status    