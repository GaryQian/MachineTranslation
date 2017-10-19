def move(sentence=list):

    #sort

    greedyH = []

    frlist = sorted(sentence, lambda x : x.frindex)

    for i in range(len(frlist) - 1):

        cureval = sentence.index(frlist[i])
        nexteval = sentence.index(frlist[i+1])

        if abs(cureval - nexteval) > 2:
            bigger = max(cureval,nexteval)
            temp1 = sentence.copy()
            temp2 = sentence.copy()
            temp1[bigger-2],temp1[bigger] = sentence[bigger], sentence[bigger-2]
            temp1[bigger-1],temp2[bigger] = sentence[bigger], sentence[bigger-1]
            
            greedtH.append(temp1)
            greedtH.append(temp2)