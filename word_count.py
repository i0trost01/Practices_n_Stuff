def word_count(phrase):
    counter={}
    nonstring=',.?!-_!@#$%^&*()+=:;'
    nonstring=list(nonstring)
    nonstring.append(' \'')
    nonstring.append('\' ')
    phrase=phrase.lower()

    for i in nonstring:
        phrase=phrase.replace(i," ")

    for i in phrase.split():
        if i in counter:
            counter[i]+=1
        else:
            counter[i]=1
    return counter

