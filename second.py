my_list = list(range(0,100))

#4 filter prime numbers
fp = open("\\prime.txt","a")

for num in my_list:
    for i in range(2,num-1):
        if (num%i == 0):
            break
    else:
        fp.write("{}\t".format(str(num)))
fp.close()

#5 using context manager
with open("\\prime_one.txt","a") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            fp.write("{}\t".format(str(num)))

#6 read txt file created
with open("\\prime_one.txt","r")as fp:
    print(fp.read())