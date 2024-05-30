import random
from random import Random


class Probability():

   def check_even_odd_zero(self,list_result):
      times = 0
      conservative = 0
      zero = 0
      even =0
      odd=0
      """
      Check if the given number is even, odd, or zero.
      """
      for i in list_result:
         if i == 0:
            zero = zero+ 1
            conservative = conservative +1
         elif i % 2 == 0:
            even = even + 1
            conservative = 0
         elif i % 2 != 0:
            odd = odd + 1
            conservative = conservative + 1
         if conservative == 4:
            times = times +1
            conservative = 0

      return times,even,odd,zero

   def check_the_number(self,list_result,number):
      occurance = 0
      """
      Check if the given number is even, odd, or zero.
      """
      for i in list_result:
         if i == number:
            occurance = occurance +1

      return occurance




   def Roulette_picker(self):
      list_result = []
      list = [0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      for i in range(0,2000):
         random_number = Random().sample(list,1)
         number = random_number[0]
         list_result.append(number)
      print(list_result)
      print(self.check_even_odd_zero(list_result))
      print(self.check_the_number(list_result,33))







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   pro = Probability()
   pro.Roulette_picker()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/