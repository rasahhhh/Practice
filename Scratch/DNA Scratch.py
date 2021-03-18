

with open('old.csv', 'r') as t1, open('new.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()



with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)



def PatternCount(text, pattern):

    count = 0

    textlen = len(text)

    pattlen = len(pattern)

    for i in range(0, textlen - 1, pattlen - 1):

        if text[i:pattlen+i] == pattern:

            count += 1

    print(count)

    return count



def FrequentWords(text,k):

    FreqPattern = []

    Count = []

    for i in range(len(text)-k):

        FreqPattern.append(text[i:i + k])

        #print(text[i:i+k])

    my_dict = {i: FreqPattern.count(i) for i in FreqPattern}

    v = list(my_dict.values())

    k = list(my_dict.keys())

    print(k[v.index(max(v))])

    print(my_dict)

    #print(FreqPattern)

    return FreqPattern





def DNAtoRNA(code):

    rna = ""

    for i in code:

        if i=="T":

            i = "U"

        rna += i

    print(rna)

    return rna





def lineup(code, k):

    text = DNAtoRNA(code)

    x = [text[i:i + k] for i in range(0, len(text), k)]

    print(x)

    return x





# def ClumpFind(genome, k, L, t):





if __name__ == '__main__':

    #text = "GACGTTGCATGTCGCATGATGCATGAGAGC"

    code = "GACGTTGCATGTCGCATGATGCATGAGAGC"

    k = 3

    lineup(code, k)