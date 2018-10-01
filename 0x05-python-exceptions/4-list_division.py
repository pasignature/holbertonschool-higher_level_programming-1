#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            ans = int(my_list_1[i]) / int(my_list_2[i])
        except IndexError:
            print("out of range")
            ans = 0
        except ValueError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        finally:
            result.append(ans)
    return result
