from random import Random


class Probability():

    def find_consecutive_odd_numbers_with_index(self,numbers):
        count = 0
        start_index = None

        for i, num in enumerate(numbers):
            if num % 2 != 0 or num == 0:
                if count == 0:
                    start_index = i
                count += 1
                if count == 3:
                    return True, start_index
            else:
                count = 0










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   pro = Probability()
   print(pro.find_consecutive_odd_numbers_with_index([5, 9, 9, 16, 24, 23, 18, 17, 34, 30, 20, 13, 1, 10, 11, 7, 6, 11, 16, 27, 23, 16, 21, 19, 11, 30, 0, 11, 10, 18, 12, 35, 31, 26, 26, 26, 32, 32, 4, 24, 3, 33, 23, 2, 4, 14, 32, 5, 27, 9, 8, 33, 31, 29, 2, 1, 29, 18, 34, 11, 19, 10, 31, 3, 34, 31, 10, 6, 11, 2, 29, 19, 22, 0, 18, 22, 17, 10, 32, 36, 0, 11, 26, 0, 11, 9, 14, 5, 22, 29, 13, 10, 26, 33, 28, 16, 25, 4, 0, 36, 15, 20, 28, 18, 34, 5, 8, 24, 20, 12, 5, 34, 4, 31, 3, 29, 5, 0, 29, 35, 18, 36, 15, 22, 6, 3, 20, 9, 15, 34, 13, 5, 32, 13, 20, 17, 7, 29, 7, 29, 23, 21, 12, 36, 0, 6, 8, 10, 31, 9, 24, 27, 14, 23, 31, 36, 27, 24, 20, 36, 21, 24, 31, 19, 26, 6, 15, 4, 19, 4, 16, 32, 22, 25, 13, 32, 1, 16, 21, 26, 32, 24, 25, 20, 11, 5, 15, 15, 0, 3, 34, 35, 26, 21, 21, 13, 3, 22, 7, 35]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/