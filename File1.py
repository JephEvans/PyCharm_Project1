import os
# Data analyitics training

# sort and search algorithim

## sort
'''
print("its working")
print("try this")
'''


# Get the list to find from
def search(List_of_items = ['e', 'j', 'c', 'j', 'r', 'j', 'e', 'ro'], item_X = 'j'):
    # note what you are looking for in the list
    Locations_of_item_X = []
    count = 0
    # check throurgh the list to compeare the values with what we are looking for
    for item in List_of_items:
    # if it is the same note the location in the list and keep checking through
        if item == item_X:
            Locations_of_item_X.append(List_of_items.index(item, count))
        count += 1
    # return a list of the locations of all the places the item is found
    if Locations_of_item_X:
        return Locations_of_item_X
    # If it was not found in the list print "not in list"
    return None


# Get the list to find from
def searchIn(List_of_items = ['e', 'j', 'c', 'j', 'r', 'j', 'e', 'ro'], item_X = 'r'):
    # note what you are looking for in the list
    Locations_of_item_X = []
    count = 0
    # check throurgh the list to compeare the values with what we are looking for
    for item in List_of_items:
    # if it is the same note the location in the list and keep checking through
        if item_X in item:
            Locations_of_item_X.append(List_of_items.index(item, count))
        count += 1
    return Locations_of_item_X


def searchGroup(List_of_items = ['e', 'j', 'c', 'j', 'r', 'j', 'e', 'ro'], item_X = ['j', 'e']):
    dictionary_of_group_of_items = {}
    for el in item_X:
        dictionary_of_group_of_items[el] = search(List_of_items, el)
    return dictionary_of_group_of_items


def searchWord(List_of_items = ['Chichi', 'jedidah', 'Mummy', 'Jeph', 'joanne', 'Aunty'], item_X = 'ej', x = True):
    for el in item_X:
        lower_List_of_items = []
        for i in List_of_items:
            lower_List_of_items.append(str(i).lower())
        new_List_of_items = []
        for i in searchIn(lower_List_of_items, str(item_X if x else el).lower()):
            new_List_of_items.append(List_of_items[i])
        List_of_items = new_List_of_items
        if x:
            break
    return List_of_items


def searchStr(string = 'Chichi, jedidah, Mummy Jeph, Aunty joanne', item_X = 'e'):
    Locations_of_item_X = []
    count = 0
    # check throurgh the list to compeare the values with what we are looking for
    while item_X in string[count:]:
    # if it is the same note the location in the list and keep checking through
        Locations_of_item_X.append(string.index(item_X, count))
        count = Locations_of_item_X[-1] + 1
    # return a list of the locations of all the places the item is found
    return Locations_of_item_X


def searchFile(files = ['C:\\Users\\Jeph\\Desktop\\equilibrium.txt', 'C:\\Users\\Jeph\\Desktop\\Tosin\\Gst 222 2023.txt', 
                        'C:\\Users\\Jeph\\Desktop\\Tosin\\Gst 222 1st 2023.txt'], item_X = ('not','cat'), x = True):
    '''Returns a list of the index of all the places each of the strings in a list of strings can be found in a file'''
    files_read = ()
    for x in files:
        files_read += ((str(open(x, "rt").read()), x),)  # + tuple of string of the file, the string of the file name
    Locations_of_item_X = {}
    for i in item_X:
        for file_read in files_read:
            if file_read[1] in Locations_of_item_X:
                Locations_of_item_X[file_read[1]] += tuple(searchStr(file_read[0], str(i).lower()))
            else:
                Locations_of_item_X[file_read[1]] = tuple(searchStr(file_read[0], str(i).lower()))
    return Locations_of_item_X


def seachWordsInFiles(file):
    file_str = ()
    for i in file:
        file_str += (str(open(i, 'rt').read()).lower(),)
    # print(file_str)
    all_words = []
    word = ''
    for li in file_str:
        # print()
        for i in li:
            if (97 <= ord(i) <= 122):
                # print('[', file_str.index(li), i, ']', sep='', end='')
                word += i
            elif len(word) > 1 and word.count('-') <= 1:
                # print(word)
                all_words.append(word)
                word = ''
        
    return tuple(set(all_words))
    # Convert the tex file to a string 
    # ilterate through the string and creat a list of all the word in it (note:  creat a sepereate function for this)


# Get the list to sorted
def sort(List_of_items = [8, 6, 9, 3, 7, 0, 5, 1, 4, 2]):
    # creat an empty list
    sorted_List_of_items = []
    # search through the list to be sorted and
    for item in List_of_items:
    # if the new list is still empty put the item in it
        if not sorted_List_of_items:
            sorted_List_of_items.append(item)
            continue
    # also for each item compear it with each item in the new list,
        count = 0
        for el in sorted_List_of_items:
    # keep iltrating until the first item that is greater than or equal it
            if el >= item:
    # place it in the position of the value; that will sift it to the right
                sorted_List_of_items.insert(sorted_List_of_items.index(el, count), item)
                break
            if count == len(sorted_List_of_items)-1:
                sorted_List_of_items.append(item)
                break
            count += 1
    # after sorting it ouput the sorted value.
    return sorted_List_of_items


def sortWordsInFile(file_to_write = 'C:\\Users\\Jeph\\OneDrive\\Documents\\Github\\PyCharm_Project1\\Dictionary.txt', files_to_search = ('C:\\Users\\Jeph\\Desktop\\equilibrium.txt', 'C:\\Users\\Jeph\\Desktop\\Tosin\\Gst 222 2023.txt', 'C:\\Users\\Jeph\\Desktop\\Tosin\\Gst 222 1st 2023.txt'), sep = '\n'):

    # sort the list
    # sorted_list = sort(seachWordsInFiles(files_to_search))
    # # write the list of words in file_to_write sepereating each word by sep.
    # for word in sorted_list:
    #     print('in')
    #     open(file_to_write, 'a').write(word + sep)
    os.remove(file_to_write)
    # print(open(file_to_write).read())


# print(search())
# print(searchIn())
# print(searchGroup())
# print(searchWord(x=0))
# print(searchStr())
# print(searchFile())
# print(seachWordsInFiles())
# print(sort())
print(sortWordsInFile())

