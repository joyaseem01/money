import random
from random import Random


class Probability():



    def simulate_betting_with_controlled_4_losses_diff(self, list_result):
        times = 0
        wins = 0
        losses = 0
        balance = 1000
        bet = 5
        unit_change = 2
        target_wins = 1010
        list = list_result
        i = 0
        balance_loss_control = self.loss_control(balance,bet,target_wins,list,i,times)
        # print("balance loss controlled")
        # print(balance)
        return balance_loss_control

    def loss_control(self,balance,bet,target_wins,list,i,times):
        loss = 0
        blackspecialtimes = 0
        while balance < target_wins and balance > 0:

            balance -= bet
            try :
                outcome = list[i]
            except IndexError:
            # Code to handle the exception (when a division by zero occurs)
                print(balance)
                break
            if outcome == "black":
                balance = balance + bet + 1
            elif outcome == "red":
                balance = balance + bet + 1
            elif outcome == "blackspecial":
                balance = balance + bet + 7
                blackspecialtimes += 1
            else:
                loss += 1
            times += 1
            i += 1
        print(blackspecialtimes)
        print(loss)
        return balance





    # def times_and_amount_comparsion(self):
    #     times = 0
    #     deposit_amount = 1000
    #     amount_with_loss_control = 0
    #     amount_with_loss_control_only_diff = 0
    #     amount_without_loss_control = 0
    #     negative_value = 0
    #     result_amount = []
    #     while times < 10:
    #         times += 1
    #         result_cal = self.Roulette_picker_with_probability()
    #         profit_or_loss_with_loss_control = result_cal[0] - deposit_amount
    #         profit_or_loss_with_loss_control_of_max_loss = result_cal[1] - deposit_amount
    #         profit_or_loss_without_loss_control = result_cal[2] - deposit_amount
    #         print(profit_or_loss_with_loss_control)
    #         print(profit_or_loss_with_loss_control_of_max_loss)
    #         print(profit_or_loss_without_loss_control)
    #         amount_with_loss_control += profit_or_loss_with_loss_control
    #         amount_with_loss_control_only_diff += profit_or_loss_with_loss_control_of_max_loss
    #         amount_without_loss_control += profit_or_loss_without_loss_control
    #     print("Amount_without_control")
    #     return amount_with_loss_control,amount_with_loss_control_only_diff,amount_without_loss_control
    #
    #
    # def month_end_report(self):
    #     monthly_amount_loss_control_at_start = 0
    #     monthly_amount_loss_control_by_diff = 0
    #     monthly_amount_without_loss_control = 0
    #     for i in range(0,30):
    #         amount_per_day = self.times_and_amount_comparsion()
    #         monthly_amount_loss_control_at_start += amount_per_day[0]
    #         monthly_amount_loss_control_by_diff += amount_per_day[1]
    #         monthly_amount_without_loss_control += amount_per_day[2]
    #     print(monthly_amount_loss_control_at_start)
    #     print(monthly_amount_loss_control_by_diff)
    #     print(monthly_amount_without_loss_control)



    def Roulette_picker_with_probability(self):
        list_result = []
        for i in range(0, 100):
            options = ["black","red","blackspecial","loss"]
            probabilities = [0.378, 0.216, 0.108, 0.298]  # These should add up to 1

            # Generate a random number based on the specified probabilities
            random_number = random.choices(options, probabilities)[0]
            list_result.append(random_number)

        # print(list_result)
        # list_result = [21, 32, 17, 23, 0, 29, 4, 36, 25, 32, 13, 10, 22, 17, 8, 19, 2, 0, 12, 33, 0, 18, 27, 16, 8, 14, 30, 15, 20, 6, 5, 1, 23, 30, 19, 32, 27, 25, 35, 27, 13, 30, 12, 2, 12, 28, 18, 21, 33, 12, 18, 19, 2, 16, 1, 30, 34, 29, 8, 27, 30, 5, 33, 15, 6, 24, 33, 35, 35, 2, 13, 0, 11, 8, 29, 3, 20, 10, 29, 16, 31, 0, 19, 13, 9, 18, 8, 31, 17, 36, 30, 11, 5, 31, 31, 10, 7, 35, 4, 14, 8, 13, 25, 21, 23, 35, 33, 8, 33, 36, 1, 14, 31, 3, 28, 26, 18, 15, 34, 6, 28, 11, 25, 33, 22, 2, 31, 16, 6, 31, 27, 1, 14, 29, 16, 22, 7, 16, 34, 14, 22, 7, 16, 19, 33, 9, 21, 19, 21, 24, 4, 11, 35, 25, 23, 26, 16, 9, 32, 36, 21, 36, 12, 25, 29, 10, 34, 3, 36, 17, 6, 21, 36, 25, 35, 10, 0, 18, 1, 13, 11, 30, 14, 28, 28, 18, 32, 13, 8, 19, 13, 29, 31, 23, 3, 11, 4, 33, 36, 13]
        # self.simulate_betting_with_controlled_4_losses_diff(list_result)
        # print(self.simulate_betting_with_controlled_3_losses(list_result))
        # print(self.simulate_betting_without_controlled_losses(list_result))
        # print(self.total_amount_calculator())
        result = self.simulate_betting_with_controlled_4_losses_diff(list_result)
        print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pro = Probability()
    pro.Roulette_picker_with_probability()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
