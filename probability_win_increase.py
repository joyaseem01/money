import random
from random import Random


class Probability():

   def Win_increase_calculator(self,list_result):
       reset = True
       win_row = False
       times = 0
       total_amount = 3000
       target_amount = 3050
       loss = 2000
       bet = 5
       list = list_result
       i = 0
       while total_amount > loss and total_amount <= target_amount and bet < 128:
               result_element = list[i]
               i += 1
               times += 1
               total_amount -= bet

               if result_element % 2 == 0 and result_element != 0:
                   if reset == True:
                       total_amount += 2*bet
                       bet = 1
                   elif reset == False:
                       if win_row == True:
                           total_amount += 2*bet
                           bet = 1
                           reset == True
                       elif win_row == False:
                           total_amount += 2*bet
                           win_row = True
                           bet = bet * 2
               elif result_element % 2 != 0 or result_element == 0:
                   win_row = False
                   reset = False
       if total_amount < loss:
           print("loss")
           print(times)
           print(bet)
       elif total_amount > target_amount:
           print("win")
           print(times)
       return total_amount







   def Roulette_picker(self):
      list_result = []
      list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      for i in range(0,2000):
         random_number = Random().sample(list,1)
         number = random_number[0]
         list_result.append(number)
      # print(list_result)
      result = self.Win_increase_calculator(list_result)
      return result

   def total_amount_calculator(self):
       amount = 0
       result_amount = []
       for i in range(0,30):
           result_cal = self.Roulette_picker()
           result_amount.append(result_cal)
       print(result_amount)
       for i in result_amount:
           amount = amount + i
       print(amount)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   pro = Probability()
   pro.total_amount_calculator()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/