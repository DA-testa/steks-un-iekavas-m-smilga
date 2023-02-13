from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    #opening_brackets_stack = []
    iekavas = []
    for i, next in enumerate(text):
        if next in "([{":
            iekavas.append(Bracket(text[i], i+1))
            
        if next in ")]}":
            iekavas.append(Bracket(text[i], i+1))
    return iekavas


def main():
    text = input()
    print(len(text))
    if(text[0] == "F"):
        text = text[3:]
        fails = open(text)
        text = fails.read()
    else:
        if(text[0] == "I"):
            text = text[3:]
    

        """
    text = ""
    text = input()
    if(text == "I"):
        text = input()
        
    else:
        if(text == "F"):
            text = input()
            fails = open(text)
            text = fails.read()

    """
    
    mismatch = find_mismatch(text)
    oldLen = 0

    while(len(mismatch) != oldLen):
        oldLen = len(mismatch)
        for i in range(0,len(mismatch) - 1):
            if(are_matching(mismatch[i].char, mismatch[i+1].char)):
                #print(mismatch)
                mismatch.pop(i)
                mismatch.pop(i)
                break

    if(len(mismatch) == 0):
        print("Success")
    else:
        aizverosas = None
        for i in range(0, len(mismatch)):
            if(mismatch[i].char in ["(", "[", "{"]):
                atverosa = mismatch[i]
            else:
                if(aizverosas == None):
                    aizverosas = mismatch[i]
        if(aizverosas):
            print(aizverosas.position)
        else:
            print(atverosa.position)


if __name__ == "__main__":
    main()
