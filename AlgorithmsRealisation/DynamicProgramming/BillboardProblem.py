def find_optimal_value(list):
    j = 0
    for i in range(x[0], M):
        if j < list_length:
            if x[j] != i:
                list[i] = list[i - 1]
                continue
            else:
                if i <= n:
                    list[i] = max(list[i - 1], r[j])
                else:
                    list[i] = max(list[i - n - 1] + r[j], list[i - 1])
                j += 1
        else:
            print(list[x[0]:i])
            break
    print("Max value is: ", list[i - 1])
    return list


data_file = open("BillboardProblemData.txt", "r")
x = []
r = []

for val in data_file.readline().split():
    x.append(int(val))
for val in data_file.readline().split():
    r.append(int(val))

M = int(data_file.readline())
n = int(data_file.readline())
data_file.close()
list_length = len(x)
result_list = [0] * M

result_list = find_optimal_value(result_list)
# result_file = open("BillboardProblemResult.txt", "w")
# for item in result_file:
#     result_file.write("%d" % item)
# result_file.close()
