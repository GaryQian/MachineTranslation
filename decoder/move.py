import copy

def move(sentence=list):

    #sort

    greedyH = []

    frlist = sorted(sentence, key=lambda x : x.frindex)

    for i in range(len(frlist) - 1):

        cureval = sentence.index(frlist[i])
        nexteval = sentence.index(frlist[i+1])
        if abs(cureval - nexteval) > 2:
            bigger = max(cureval,nexteval)
            temp1 = copy.copy(sentence)
            temp2 = copy.copy(sentence)
            #print cureval
            #print nexteval
            temp1[bigger-2],temp1[bigger] = temp1[bigger], temp1[bigger-2]
            temp2[bigger-1],temp2[bigger] = sentence[bigger], sentence[bigger-1]
            #print str(temp1) + " " + str(temp2)
            greedyH.append(temp1)
            greedyH.append(temp2)
    return greedyH