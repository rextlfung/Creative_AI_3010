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
        for list in text:
            for word in list:
                index = list.index(word)
                if index < len(list) - 1:
                    if list[index] in self.nGramCounts:
                        if list[index + 1] in self.nGramCounts[list[index]]:
                            self.nGramCounts[list[index]][list[index + 1]] += 1
                        else:
                            self.nGramCounts[list[index]][list[index + 1]] = 1
                    else:
                        self.nGramCounts[list[index]] = {list[index + 1]: 1}

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
        if sentence[-1] in possible_keys:
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
        return self.nGramCounts[sentence[-1]]

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
    sentence = ['Eagles', 'fly', 'in', 'the', 'sky']
    print(bi.trainingDataHasNGram(sentence))
    bi.trainModel(text)
    print(bi.trainingDataHasNGram(sentence))

    bi = BigramModel()
    sentence = ['Eagles', 'are', 'brown']
    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'brown', 'fox'] ]
    bi.trainModel(text)
    print(bi.trainingDataHasNGram(sentence))

    print(bi.getCandidateDictionary(sentence))
