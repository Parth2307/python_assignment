

lst= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst1= [item for sublist in lst for item in sublist]

print(lst1)


'''
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in list_of_lists for item in sublist]

print(flat_list)
'''