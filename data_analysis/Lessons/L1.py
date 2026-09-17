def totin(phrase):
    all=0
    for i in phrase:
        all+=1
    return print(all)


def totex(phrase):
    all=0
    for i in phrase:
        if i!=" ":
            all+=1
        else:
            continue
    return print(all)

a="asd  "
totex(a)

