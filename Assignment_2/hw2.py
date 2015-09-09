#1. fill in this class
#   it will need to provide for what happens below in the
#   main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
#    a function called showEvaluation, and an attribute carCount
class CarEvaluation:
   'A simple class that represents a car evaluation'
   carCount = 0

   def __init__(self,brand,price,safetyRating):
      self.__class__.carCount += 1
      self.Brand = brand
      self.Price = price
      self.SafetyRating = safetyRating
      #give a rank based on the price for ordering later
      if self.Price == 'High':
         self.PriceRank = 3
      elif self.Price == 'Med':
         self.PriceRank = 2
      elif self.Price == 'Low':
         self.PriceRank = 1

   def __repr__(self):
      return self.Brand

   def showEvaluation(self):
      print "The %s has a %s price and it's safety is rated a %d" % (self.Brand, self.Price, self.SafetyRating)

#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
#    otherwise by descending price
def sortbyprice(cars, sortDir):  #you fill in the rest
    return sorted(cars,key=lambda CarEvaluation : CarEvaluation.PriceRank, reverse= (sortDir == 'des') )

#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#   it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(carEvals, safetyRating): #you fill in the rest
   for ce in carEvals:
      if (ce.SafetyRating == safetyRating):
         return True
   return False

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
   eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
   eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false