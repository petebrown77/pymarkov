# pymarkov
Python implementation of a simple Markov chain

# Warning
This is still in it's beta stages, and many breaking changes will be made in the future.  This is not the implementation to use in production.

# Installation
To install, simply clone this repo to your computer:

```
git clone https://www.github.com/petebrown77/pymarkov.git
``` 

# Usage
```python
from pymarkov import MarkovChain, generate_from_sequence

#Initiate with a transistion matrix...
matrix = [[0.8, 0.1, 0.1],
          [0.2, 0.3, 0.5],
          [0.3, 0.6, 0.1]]
          
chain = MarkovChain(['Sunny', 'Rainy', 'Snowy'], t_matrix=matrix)
chain.next_state("Sunny")

#Or with a sequence.  The class will infer the markov chain from there
sequence = ["Sunny", "Sunny", "Rainy", "Rainy", "Rainy", "Rainy", "Snowy", "Sunny"]
chain = generate_from_sequence(sequence)
