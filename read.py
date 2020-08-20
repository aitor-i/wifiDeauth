output = open("myoutput-02.csv", "r")

target_list = []

for i in range(20):
    line = output.readline()
    target_list.append(line.split(","))


# print(target_list)

print(target_list[2][0])


