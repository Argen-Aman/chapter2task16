num_list = input('Type some integers(don\'t forget to put commas between them): ')

num_list = num_list.split(', ')

def new_list (num_list):
    for i in num_list:  
        if int(i) > 0:
            print(1)
        elif int(i) < 0:
            print(-1)
        else:
            print(0)
new_list (num_list)
