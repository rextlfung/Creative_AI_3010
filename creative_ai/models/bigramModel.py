from creative_ai.utils.print_helpers import ppGramJson

class BigramModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.

        This function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.

        This function is done for you.
        """

        return ppGramJson(self.nGramCounts)


###############################################################################
# Begin Core >> FOR CORE IMPLEMENTION, DO NOT EDIT ABOVE OF THIS SECTION <<
###############################################################################

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.
                  Returns self.nGramCounts
        """
        word_count = 0
        joined_text = []
        for i in text:
            joined_text += i
        for word1 in joined_text:
            index = joined_text.index(word1)
            if index < len(joined_text) - 1:
                word2 = joined_text[index + 1]
                bigram = word1 + word2
                joined_words = ''.join(joined_text)
                word_count = joined_words.count(bigram)
                d2 = {}
                d2[word2] = word_count
                self.nGramCounts[word1] = d2

        return self.nGramCounts

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """
        possible_keys = []
        possible_keys = self.nGramCounts.keys()
        sentence_list = sentence.split()
        if sentence_list[-1] in possible_keys:
            return True
        else:
            return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        # FIX ME
        return_dict = {}
        sentence_list = sentence.split()
        word = sentence_list[-1]
        possible_values = []
        possible_values = self.nGramCounts.values()
        for pair in possible_values:
            return_dict[word] = pair
            return return_dict

###############################################################################
# End Core
###############################################################################

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    bi = BigramModel()
    text = [ [ 'brown' ] ]
    bi.trainModel(text)
    print(bi)

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'brown', 'fox'] ]
    bi.trainModel(text)
    print(bi)

    bi = BigramModel()
    sentence = "Eagles fly in the sky"
    print(bi.trainingDataHasNGram(sentence))
    bi.trainModel(text)
    print(bi.trainingDataHasNGram(sentence))

    bi = BigramModel()
    sentence = "Eagles are brown"
    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'brown', 'fox'] ]
    bi.trainModel(text)
    print(bi.trainingDataHasNGram(sentence))

    print(bi.getCandidateDictionary(sentence))
