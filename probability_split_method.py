from random import Random


class Probability():

    def Split_method(self,list_result):
        balance = 1000
        target_amount = 1050
        unit = 5
        j = 0
        times = 0
        lst = []
        list = list_result
        for i in range(0,10):
            lst.append(unit)
        balance_no_loss_control = self.no_loss_control(balance,target_amount,unit,j,times,lst,list)
        balance = 1000
        target_amount = 1050
        unit = 5
        j = 0
        times = 0
        lst = []
        list = list_result
        for i in range(0,10):
            lst.append(unit)
        balance_with_balance_control = self.balance_control(balance,target_amount,unit,j,times,lst,list)
        # balance = 1000
        # target_amount = 1050
        # unit = 5
        # j = 0
        # times = 0
        # lst = []
        # list = list_result
        # for i in range(0,10):
        #     lst.append(unit)
        # balance_with_loss_control = self.loss_control(balance,target_amount,unit,j,times,lst,list)
        return balance_no_loss_control,balance_with_balance_control




    def no_loss_control(self,balance,target_amount,unit,j,times,lst,list):
        while len(lst) > 0 and balance > 0:
            if len(lst) >= 2:
                balance = balance - (lst[0] + lst[-1])
            elif len(lst) == 1:
                balance = balance - lst[0]
            try :
                number = list[j]
            except IndexError:
            # Code to handle the exception (when a division by zero occurs)
                print(balance)
                break

            if number % 2 == 0 and number != 0:
                # Remove the first and last elements

                if len(lst) >= 2:
                    balance = balance + 2 * (lst[0] + lst[-1])
                    lst.pop(0)
                    lst.pop(-1)

                elif len(lst) == 1:
                    balance = balance + 2 * lst[0]
                    lst.pop(0)


            else:
                # Append the sum of the first and last elements
                if len(lst) >= 2:
                    lst.append(lst[0] + lst[-1])
                if len(lst) == 1:
                    lst.append(lst[0])

            times += 1
            j += 1
        print(times)
        return balance


    def balance_control(self,balance,target_amount,unit,j,times,lst,list):

        while len(lst) > 0 and balance > 500:
            if len(lst) >= 2:
                balance = balance - (lst[0] + lst[-1])
            elif len(lst) == 1:
                balance = balance - lst[0]
            try :
                number = list[j]
            except IndexError:
            # Code to handle the exception (when a division by zero occurs)
                print(balance)
                break

            if number % 2 == 0 and number != 0:
                # Remove the first and last elements

                if len(lst) >= 2:
                    balance = balance + 2 * (lst[0] + lst[-1])
                    lst.pop(0)
                    lst.pop(-1)

                elif len(lst) == 1:
                    balance = balance + 2 * lst[0]
                    lst.pop(0)


            else:
                # Append the sum of the first and last elements
                if len(lst) >= 2:
                    lst.append(lst[0] + lst[-1])
                if len(lst) == 1:
                    lst.append(lst[0])

            times += 1
            j += 1

        return balance


    def loss_control(self,balance,target_amount,unit,j,times,lst,list):

        while len(lst) > 0:
            if len(lst) >= 2:
                balance = balance - (lst[0] + lst[-1])
            elif len(lst) == 1:
                balance = balance - lst[0]
            try :
                number = list[j]
            except IndexError:
            # Code to handle the exception (when a division by zero occurs)
                print(balance)
                break

            if number % 2 == 0 and number != 0 :
                # Remove the first and last elements

                if len(lst) >= 2:
                    balance = balance + 2 * (lst[0] + lst[-1])
                    lst.pop(0)
                    lst.pop(-1)

                elif len(lst) == 1:
                    balance = balance + 2 * lst[0]
                    lst.pop(0)


            else:
                # Append the sum of the first and last elements
                if len(lst) >= 2:
                    lst.append(lst[0] + lst[-1])
                if len(lst) == 1:
                    lst.append(lst[0])

            times += 1
            j += 1

        return balance



    def times_and_amount_comparsion(self):
        times = 0
        deposit_amount = 1000
        amount_with_loss_control = 0
        amount_with_loss_control_only_diff = 0
        amount_without_loss_control = 0
        negative_value = 0
        result_amount = []
        while times < 10:
            times += 1
            result_cal = self.Roulette_picker()
            profit_or_loss_with_loss_control = result_cal[0] - deposit_amount
            profit_or_loss_with_loss_control_of_max_loss = result_cal[1] - deposit_amount
            # profit_or_loss_without_loss_control = result_cal[2] - deposit_amount
            print(profit_or_loss_with_loss_control)
            print(profit_or_loss_with_loss_control_of_max_loss)
            # print(profit_or_loss_without_loss_control)
            amount_with_loss_control += profit_or_loss_with_loss_control
            # amount_with_loss_control_only_diff += profit_or_loss_with_loss_control_of_max_loss
            # amount_without_loss_control += profit_or_loss_without_loss_control
        print("Amount_without_control")
        return amount_with_loss_control,profit_or_loss_with_loss_control_of_max_loss


    def month_end_report(self):
        monthly_amount_loss_control_at_start = 0
        monthly_amount_loss_control_by_diff = 0
        monthly_amount_without_loss_control = 0
        for i in range(0,30):
            amount_per_day = self.times_and_amount_comparsion()
            monthly_amount_loss_control_at_start += amount_per_day[0]
            monthly_amount_loss_control_by_diff += amount_per_day[1]
            # monthly_amount_without_loss_control += amount_per_day[2]
        print(monthly_amount_loss_control_at_start)
        print(monthly_amount_loss_control_by_diff)
        # print(monthly_amount_without_loss_control)






    def Roulette_picker(self):
      list_result = []
      list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
      for i in range(0,200):
         random_number = Random().sample(list,1)
         number = random_number[0]
         list_result.append(number)
      # print(list_result)
      # list_result = [5, 8, 9, 2, 17,3, 3, 30, 20, 1]
      result = self.Split_method(list_result)
      return result








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   pro = Probability()
   pro.month_end_report()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/