
from collections import namedtuple

greedyHyp = namedtuple("greedyHyp","frIndex", "phrase")


def pharoahToGreedy(hypothesis):
	if hypothesis.predecessor == None:
		return [greedyHyp(hypothesis.frIndex, hypothesis.phrase)]
	else:
		return pharoahToGreedy(hypothesis.predecessor) + [greedyHyp(hypothesis.frIndex, hypothesis.phrase)]
