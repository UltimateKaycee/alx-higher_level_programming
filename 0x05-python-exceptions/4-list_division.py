#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    the_result = []
    for run in range(list_length):
        try:
            the_result.append(my_list_1[run] / my_list_2[run])
            continue
        except ZeroDivisionError:
            print("Can't divide by 0")
            the_result.append(0)
        except TypeError:
            print("invalid entry")
            the_result.append(0)
        except IndexError:
            print("invalid set")
            the_result.append(0)
        finally:
            pass
    return(the_result)
