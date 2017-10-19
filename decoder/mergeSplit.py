
from collections import namedtuple

greedyHyp = namedtuple("greedyHyp","frindex", "phrase")


def pharoahToGreedy(hypothesis):
	if hypothesis.predecessor == None:
		return [greedyHyp(hypothesis.frindex, hypothesis.phrase.english)]
	else:
		return pharoahToGreedy(hypothesis.predecessor) + [greedyHyp(hypothesis.frindex, hypothesis.phrase.english)]


def mergeSentence(sent, source, trans_table):
	possible = []
	french_phrases = sorted(sent, key=lambda hyp: hyp.frindex)
	for i in range(len(french_phrases) - 1):
		index1 = sent.index(french_phrases[i])
		index2 = sent.index(french_phrases[i+1])
		mergedPhrase = (index1[0], index2[1])
		translations = trans_table[source[mergedPhrase[0], mergedPhrase[1]]]
		if translations is None:
			continue
		translation = max(translations, key=lambda phrase: phrase.logprob).english
		new_hyp = greedyHyp(mergedPhrase, translation)
		new_sent1 = copy.deepcopy(sent)
		new_sent1[index1] = new_hyp
		del new_sent1[index2]
		new_sent2 = copy.deepcopy(sent)
		new_sent2[index2] = new_hyp
		del new_sent2[index1]
		possible += [new_sent1, new_sent2]
	return possible

def splitSentence(sent, source, trans_table):
	possible = []
	for index,hyp in enumerate(sent):
		if hyp.frindex[1] - hyp.frindex[0] <2:
			continue
		for mid in range(hyp.frindex[0]+1, hyp.frindex[1]):
			phrase1 = (hyp.frindex[0], mid)
			phrase2 = (mid, hyp.frindex[1])
			translations1 = trans_table[source[phrase1[0], phrase1[1]]]
			translations2 = trans_table[source[phrase2[0], phrase2[1]]]
			if translations1 is None or translations2 is None:
				continue
			new_hyp1 = greedyHyp(phrase1, max(translations1, key=lambda phrase: phrase.logprob).english)
			new_hyp2 = greedyHyp(phrase1, max(translations2, key=lambda phrase: phrase.logprob).english)
			new_sent = copy.deepcopy(sent)
			new_sent[index] = new_hyp1
			new_sent.insert(index+1, new_hyp2)
			possible.append(new_sent)
	return possible

