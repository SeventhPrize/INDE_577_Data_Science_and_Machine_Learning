import numpy as np

class Neuron:
    '''
    Generic class for a single artificial neuron.
    '''
    weights = None                  # weights for preactivation function. 1-dimenional column array.

    def fire(self, signal):
        '''
        Fires neuron. Computes preactivation value using weights and input signal. Then returns activation_function applied to the preactivation value.
        INPUT
            signal; the vector of data observations
        RETURNS
            scalar-valued preactivation value
        '''
        return self.activation(np.dot(self.weights, signal))

    def activation(self, preactivation):
        '''
        Given a preactivation scalar, returns the post-activation scalar output.
        INPUT
            preactivation; scalar-valued preactivation value
        RETUNS
            post-activation value, equivalent to the neuron's prediction
        '''
        return 0

