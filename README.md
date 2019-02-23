# Animo-Acid-Sequence-Analysis
The main.py file converts DNA sequences (taken from NCBI GenBank) into amino acid sequences.
Then, the probability of these observed amino acid sequences are determined given initial parameters. Baum-Welch algorithm is used as a model to get better model parameters to increase the probability of the observed sequence. So, the model parameters (start, emission and transition probability) are obtained for the observed sequence. 

The python version used was 3.5. 
numpy and hidden_markov packages are required to run this file
hidden_markov package can be found in this folder or https://pypi.python.org/pypi/hidden_markov/0.3.1
