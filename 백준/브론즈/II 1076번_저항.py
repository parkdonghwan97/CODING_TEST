
mydict = {
'black'     : '0'	,
'brown'	    : '1'	,
'red'	    : '2'	,
'orange'	: '3'	,
'yellow'	: '4'	,
'green'     : '5'	,
'blue'      : '6'	,
'violet'	: '7'	,
'grey'	    : '8'	,
'white'     : '9',
}

color=[]
for i in range(3):
    color.append(input())

print(int(mydict[color[0]]+mydict[color[1]])* (10**int(mydict[color[2]]))   )