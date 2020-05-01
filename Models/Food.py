class Food:
     def __init__(self, name, quantity, calories, expiredate):
         self.name = name
         self.quantity = int(quantity)
         self.calories = int(calories)
         self.expiredate = int(expiredate)

     def expires(self):
         if self.expiredate <= 1:
             return True
         return False

     def compute_calories_perday(f):
         rez = f.calories / f.expiredate
         msg = "Please consume " + f.name +" "+ str(rez) +" calories per day in order to not waste food"
         return msg

     def compute_grams_perday(f):
         rez = f.quantity / f.expiredate
         msg = "Please consume " + f.name +" "+ str(rez) +" grams per day in order to not waste food"
         return msg