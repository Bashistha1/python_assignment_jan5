class CheckError():
    def __init__(self,roll):
        if(roll>24):
            raise NameError()

dictionary = {
    1: "std1",
    2: "std2"
}
option = 1
while (option==1):
    try:
        option = int(input("choose an option"))
        if (option == 1):
            roll = int(input("sn no:"))
            name = input("address: ")
            CheckError(roll)
            dict.update({roll: name})
        elif (option == 2):
            roll = int(input("sn no.: "))
            print(dict[roll])
        elif (option == 3):
            del dict
    except KeyError:
        print("sn no. does not exist")
    except NameError:
        print("cannot accomadate more than 24 std")
    except ValueError:
        print("enter an ingteger sn no.")
    except TypeError:
        print("std doesnot exist")
    else:
        print("Error occured")
    finally:
        loop = input("would you like to continue? (yes/no)")
        if(loop == "yes"):
            option=1
        else:
            option=0
