spam = ['apples', 'bananas', 'tofu', 'cats']

def list2str(list):
    list.insert(len(list) - 1, 'and')
    string = ''
    for i in list:
        string += str(i) + ', '
    newString = string.replace(',', '')
    lastString = newString.replace(' ', ', ', len(list) - 2)
    return lastString

print(list2str(spam))