from sentence_transformers import SentenceTransformer, util, Tensor
from typing import List
MODEL_STRING = 'all-MiniLM-L6-v2'


class SemanticSim(object):
    def __init__(self):
        self.model = SentenceTransformer(MODEL_STRING)

    def create_emmbedings(self, sentences: List[str]) -> List[Tensor]:
        return self.model.encode(sentences)

    def calc_cosine_sim(self, s1, s2):
        """
        Calculate the embedding cosine similarity of two strings.
        """
        # TODO: cache?
        embs = self.create_emmbedings([s1, s2])
        return util.cos_sim(embs[0], embs[1])[0].item()

    def calc_cosine_sim_with_lists(self, list1, list2):
        """
        :param list1: list of strings (of size n)
        :param list2: another list of strings (of size m)
        :return: an n*m matrix of similarities between items of list1 and items of list2
        """
        embs1 = self.create_emmbedings(list1)
        embs2 = self.create_emmbedings(list2)
        return util.cos_sim(embs1, embs2)




############################## Example Use ############################
# semantic_sim = SemanticSim()
# # For comparing a single pair of strings
# semantic_sim.calc_cosine_sim("Cooking", "I need help with preparing soup"])
# result: 0.38
# semantic_sim.calc_cosine_sim("Cooking", "I need help with walking the dog")
# result: 0.06

# # For comparing two lists of strings
# list1 = ["I love cooking", "I am good with dogs"]
# list2 = ["I need help with preparing soup", "I need someone to walk the dog in the evening"]
# semantic_sim.calc_cosine_sim_with_lists(list1, list2)
# result: tensor([[0.2500, 0.1887],
#                 [0.1066, 0.4382]])