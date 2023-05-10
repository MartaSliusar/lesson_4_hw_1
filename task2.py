list = [1, 2, 3, 4, 5, 6, 7] #непарна кількість елементів
#list = [1,2,3,4,5,6,] #парна кількість елементів
#list = [1] #непарна кількість елементів
#ist = [] #пустий список
lenght = len(list)
half = lenght // 2
if lenght % 2 == 0:
    list1 = list[:half]
    list2 = list[half:]
    print(list1, list2)
else:
    half = half + 1
    list1 = list[:half]
    list2 = list[half:]
    print(list1, list2)
