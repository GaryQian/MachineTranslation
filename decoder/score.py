import namedtuple
from decodegreedy import greedyHyp


def score(src, sen, lm, tm, l1, l2, l3):

#calculate Lmprob
lm_state = lm.begin() # initial state is always <s>
lmprob = 0.0
for word in sen.split():
    (lm_state, word_logprob) = lm.score(lm_state, word)
    lmprob += word_logprob
lmprob += lm.end(lm_state) # transition to </s>, can also use lm.score(lm_state, "</s>")[1]

#calculate tmProb

tmProb = 0.0

for gh in sen.split():
    fphrase = tuple(src.split(' ')[gh.frindex[0],gh.frindex[1]])
    for t in tm[fphrase]:
        if t.english == gh.phrase:
            tmProb += t.logprob

prob = (l1*lmprob) + (l2*tmProb) - (l3* len(sen)) 
