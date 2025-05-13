#Inheritance from other class
from Chef import Chef

#The ChineseChef class is going to use all the functionality of Chef class
class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")


#Inheritance
#class ChineseChef:
#    def make_chicken(self):
#        print("The chef makes a chicken")
#    
#    def make_salad(self):
#        print("The chef makes a salad")
#        
#    def make_special_dish(self):
#        print("The chef makes orange chicken")
#    
#    def make_fried_rice(self):
#        print("The chef makes fried rice")