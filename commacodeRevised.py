spam = ['apples', 'bananas', 'tofu', 'cats', 'ogres']

def list2str(list):
    list.insert(len(list) - 1, 'and')
    string = ''
    for i in list:
        string += str(i) + ' '

    newString = string.replace(' ', ', ', int(len(list) - 2))
    return newString

print(list2str(spam))
