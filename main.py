with open('data.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    k = []
    one = {}
    one['ingridient_name'] = []
    one['quantity'] = []
    one['measure'] = []
    for line in file:

        food = line.strip()
        # print(food)

        how_many = int(file.readline().strip())
        # print(how_many)
        for i in range(how_many):

            k = file.readline().split(' | ')

            one['ingridient_name'].append(k[0])
            one['quantity'].append(k[1])
            one['measure'].append(k[2])

        file.readline()

        cook_book[food] = one

    print(cook_book)

