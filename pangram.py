def is_pangram(sentence):
    pangram=False
    sentence=sentence.lower()
    abc=[0]*26
    for i in range(1,27):
        abc[i-1]=i
    for i in sentence:
        if ord(i)>96:
            for j in abc:
                if j==ord(i)-96:
                    abc[j-1]=0
    if sum(abc)==0:
        pangram=True
    return pangram