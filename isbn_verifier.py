def verify(isbn):
    isbn=list(isbn)
    if not len(isbn)==10 and not len(isbn) == 13:
        return False
    if isbn[1] == '-':
        del isbn[1], isbn[4], isbn[9]
    if isbn[-1] == 'X':
        isbn[-1] = '10'
    isbn2 = ''.join(isbn)
    if not isbn2.isdigit():
        return False
    isbn = list(map(int, isbn))
    if (isbn[0]*10+isbn[1]*9+isbn[2]*8+isbn[3]*7+isbn[4]*6+isbn[5]*5+isbn[6]*4+isbn[7]*3+isbn[8]*2+isbn[9])%11 == 0:
        return True
    else:
        return False
