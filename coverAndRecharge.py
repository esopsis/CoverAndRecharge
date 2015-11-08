""" coverAndRecharge.py
by Eric J.Parfitt (ejparfitt@gmail.com)

I wrote this code specifically to work with some geology data.  I was
given a spreadsheet with "cover types" for the land, and "average
recharge rates" for each cover type.  This code gathered each data point
by cover type and sorted each cover type group by its average recharge
rate.

"""

def stringToArray(string):
    linessplit = string.splitlines()
    out = []
    for line in linessplit:
        col = []
        for string in line.split(' '):
            try:
                col.append(float(string))
            except ValueError:
                pass
        out.append(col)
    return out

def sheetToArray(sheet):
    string = open(sheet).read()
    return stringToArray(string)

class CoverType:
    def __init__(self, myType):
        self.myType = myType
        self.recharges = []
        self.average = None

covers = sheetToArray("flowdir.txt")
recharges = sheetToArray("recharges.txt")

coverTypes = []
for i in range(len(covers)):
    print(i)
    for j in range(len(covers[0])):
        if not covers[i][j] in (coverType.myType for coverType in coverTypes):
            coverTypes.append(CoverType(covers[i][j]))
        for coverType in coverTypes:
            if coverType.myType == covers[i][j]:
                coverType.recharges.append(recharges[i][j])
for coverType in coverTypes:
    coverType.averageRecharge = sum(coverType.recharges) / \
            len(coverType.recharges)
coverTypes.sort(key=lambda coverType: coverType.myType)
for coverType in coverTypes:
    print int(coverType.myType), coverType.averageRecharge
    
