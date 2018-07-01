def is_isogram(string):
    isogram=True
    string=string.lower()
    for i in string:
        if string.count(i)>1 and i!=" " and i!="-":
            isogram=False
    return isogram




