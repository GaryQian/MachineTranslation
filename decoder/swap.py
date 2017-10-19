import namedtuple
from decodegreedy import greedyHyp
import copy

def swap(sen):
  out = []
  for i in range(len(sen) - 1):
    newsen = copy.copy(sen)
    newsen[i], newsen[i+1] = newsen[i+1], newsen[i]
    out.append(newsen)
  return out
      
    

