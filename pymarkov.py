import numpy as np



class MarkovChain(object):

    def __init__(self, states, t_matrix=None):
        self.states = states
        self.index_dict = {self.states[index]: index for index in range(len(self.states))}

        #If we have a transition matrix, we can add it here
        if t_matrix:
            self.transistion_matrix = t_matrix

    def _row_mod(self, row):
        if (sum(row) > 0):
            return row / sum(row)

    def generate_tmatrix(self, sequence):
        """
        Given a sequence, generate a transition matrix.
        sequence: list -> list of values to generate matrix from.
        """
        n = len(set(sequence))


        #To allow differnt types of data,
        #We need to setup a dittionary
        #That maps to each value within the sequence
        seq_dict = {j: i for i, j in zip(list(range(n)), set(sequence))}

        matrix = [[0] * n for _ in range(n)]

        for (i, j) in zip(sequence, sequence[1:]):
            matrix[seq_dict[i]][seq_dict[j]] += 1

        for row in matrix:
            
            s = sum(row)
            if s > 0:
                row = [f / s for f in row]


        #Set transistion matrix value here
        self.transistion_matrix = matrix

    def generate_tmatrix_2(self, sequence):
        """
        Given a sequence, generate a transition matrix.
        sequence: list -> list of values to generate matrix from.
        """
        n = len(set(sequence))


        #To allow differnt types of data,
        #We need to setup a dittionary
        #That maps to each value within the sequence
        seq_dict = {j: i for i, j in zip(list(range(n)), set(sequence))}

        matrix = np.array([[0] * n for _ in range(n)])

        for (i, j) in zip(sequence, sequence[1:]):
            matrix[seq_dict[i]][seq_dict[j]] += 1

        jeff = np.apply_along_axis(self._row_mod, 1, matrix)


        #Set transistion matrix value here
        self.transistion_matrix = jeff


    def normalize_weights(self, weights):
        """Python has a floating point problem,
        where not every number is equal to the int.
        eg. 0.1 + 0.2 + 0.7 = 1.000000001.

        To solve this, we can normalize the weights before we use them.
        """
        
        weights /= np.sum(weights)
        return weights


    def next_state(self, current_state):
        """Calculates and returns the next state in the markov chain."""
        weights = self.transistion_matrix[self.index_dict[current_state]]
        normalized = self.normalize_weights(weights)

        return np.random.choice(
            self.states,
            p=normalized
            )


    def generate_states(self, current_state, no=10):
        """
        Generate sequence on length no.
        """
        future = []
        for i in range(no):
            next_state = self.next_state(current_state)
            future.append(next_state)
            current_state = next_state

        return future


def generate_from_sequence(sequence):
    """
    If we do not know the states, and are only given a sequence,
    this function will transform the sequence into a Markov chain.
    
    sequence -> list: list containing possible states
    """
    states = set(sequence)
    chain = MarkovChain(list(states))
    chain.generate_tmatrix_2(sequence)
    
    return chain

    
if __name__ == "__main__":

    matrix = [[0.8, 0.19, 0.1],
              [0.2, 0.7, 0.1],
              [0.1, 0.2, 0.7]]



    chain = MarkovChain(["Sunny", "Rainy", "Snowy"], t_matrix=matrix)
    print(chain.next_state("Snowy"))

    sequence = chain.generate_states("Snowy", no=100)

    #newChain = MarkovChain(["Sunny", "Rainy", "Snowy"])
    #newChain.generate_tmatrix(sequence)
    newChain = generate_from_sequence(sequence)

    print(newChain.generate_states("Sunny", no=20))
