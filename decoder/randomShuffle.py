from random import shuffle
import copy

def randomShuffle(sen, n):
  out = []
  for i in range(n):
    out.append(copy.copy(sen))
    shuffle(out[i])
  return out