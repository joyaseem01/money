import random
from random import Random


class Probability():

   def Winning_checker(self,list_result):
      par = 0
      continous_loss = 0
      checker = 0
      loss = 0
      list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      for i in list_result:
         if i in list1:
            checker = checker+1
            if i in [25,26,27,28,29,30,31,32,33,34,35,36]:
               par = par + 1
         else:
            loss = loss + 1
         # if loss == 1:
         #    continous_loss = continous_loss + 1
      return checker,par,loss


   def Roulette_picker(self):
      list_result = []
      list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      for i in range(0,20):
         random_number = Random().sample(list,1)
         number = random_number[0]
         list_result.append(number)
      print(list_result)
      print(self.Winning_checker(list_result))








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   pro = Probability()
   pro.Roulette_picker()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/