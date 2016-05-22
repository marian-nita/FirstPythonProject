spam = ['apples', 'bananas', 'tofu', 'cats']


def rreplace(s, old, new, occurence):
    li = s.rsplit(old, occurence)
    return new.join(li)

def list2str(list):
    list.insert(len(list) - 1, 'and')
    string = ''
    for i in list:
        string += str(i) + ', '
    newString = rreplace(string, ',', '', len(list) - 2)
    return newString

print(list2str(spam))