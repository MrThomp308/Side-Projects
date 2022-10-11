def findSingle(nList):
    nList.sort()
    listString = ' ' + str(nList)[1:-1] + ','
    listString = listString.replace(',',', ')
    
    print(listString)
    
    exceptList = []
    dupeList = nList
    for i in range(0,len(nList)):
        numString = ' ' + str(nList[i]) + ','
        
        if(nList[i] not in exceptList):
            exceptList.append(nList[i])
        else:
            listString = listString.replace(numString,'')
         
        
    result = int(listString.strip()[:-1])
    print('results')
    print(result)
    return(result)

def main():
    print('main')
    
    numList = [1,1,3,3,4,5,5,6,6,10,10,20,20]
    findSingle(numList)
    
main()
