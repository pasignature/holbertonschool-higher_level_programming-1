#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        ans = 0
        try:
            ans = int(my_list_1[i]) / int(my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except ValueError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(ans)
    return result
