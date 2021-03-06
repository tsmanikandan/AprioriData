import csv, operator, numpy, collections, itertools

def stringstonum(s1, s2):
    j = 0
    for i in range(0, len(s1)):
        if ((s1[i] == '1') and (s2[i] == '1')):
            j += 1
    return j

def stringstonum3(s1, s2, s3):
    j = 0
    for i in range(0, len(s1)):
        if ((s1[i] == '1') and (s2[i] == '1') and (s3[i] == '1')):
            j += 1
    return j

dictof1 = dict()

with open('market_data_transaction.txt','rb') as market:
    transactionreader = csv.reader(market, delimiter = ',')
    for row in transactionreader:
        for i in row:
            i = i.replace(" ", "")
            if i in dictof1:
                dictof1[i] += 1
            else:
                dictof1[i] = 1

listof1 = sorted(dictof1)

index = []
with open('market_data_binary.txt', 'rb') as binary:
    binreader = csv.reader(binary, delimiter = ' ')
    for row in binreader:
        index.append(row)

binstrings = ["" for i in range(0,11)]
for i in range(0,11):
    for j in range(0,5):
        binstrings[i] += str(index[j][i])

bindict = {}
for i in range(0,11):
    bindict[listof1[i]] = binstrings[i]
#print bindict

finaldict = {key: value for key, value in dictof1.items() if value >= 2.5}
freqlist1 = sorted(finaldict)
print freqlist1

listof2 = []
for i in range(0,len(freqlist1)-1):
    for j in range(i+1, len(freqlist1)):
        if (stringstonum(bindict[freqlist1[i]], bindict[freqlist1[j]]) >= 2.5):
            smlist = []
            smlist.append(freqlist1[i])
            smlist.append(freqlist1[j])
            smlist.append(stringstonum(bindict[freqlist1[i]], bindict[freqlist1[j]]))
            listof2.append(smlist)

print listof2

listof3 = list(itertools.combinations(iter(freqlist1), 3))
print listof3[2][1]
