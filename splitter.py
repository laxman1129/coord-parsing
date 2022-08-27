import os

[print(x) for x in os.listdir('./out')]
file_no = input("choose file number from below : ")

file_name = './out/' + file_no + ".dat"
print('file location is : ' + file_name)

split_count = int(input("enter number of splits : "))
file = open(file_name, 'r')
content = file.readlines()
lines = len(content)
print(lines)
print('-' * 20)

if split_count > lines:
    print('split count is more than number of lines. Enter value lesser than ' + str(lines))

for i in range(1, split_count + 1):
    flag = True
    file = open(r"./split/" + str(file_no) + '_' + str(i) + '.dat', "w+")
    while flag:
        print('split : ' + str(i))

        val = input('''
        Enter line number to include in this split
        OR
        Enter H to see available lines
        OR
        Enter C to complete this split        
        ''')

        if val == 'c':
            flag = False
            print('Split : ' + str(i) + " Completed")
            print('-' * 20)
            break
        elif val == 'h':
            print('-' * 20)
            print('Available lines are : ')
            [print(x) for x in enumerate(content)]
            print('-' * 20)
        else:
            crd = content[int(val)]
            file.write(crd)
