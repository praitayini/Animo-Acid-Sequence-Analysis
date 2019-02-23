"""
Spyder Editor
Praitayini Kanakaraj
"""
# Import required Libraries
import numpy as np
# Refernce: https://pypi.python.org/pypi/hidden_markov/0.3.1
from hidden_markov import hmm
import re


#DNA Sequence from GenBank
#DNA sequence of Human alpha-type insulin gene
dna='CTGGGGCTGCTGTCCTAAGGCAGGGTGGGAACTAGGCAGCCAGCAGGGAGGGGACCCCTCCCTCACTCCCACTCTCCCACCCCCACCACCTTGGCCCATCCATGGCGGCATCTTGGGCCATCCGGGACTGGGGACAGGGGTCCTGGGGACAGGGGTCCGGGGACAGGGTCCTGGGGACAGGGGTGTGAGGACAGGGGTCCTGGGGACAGGGGTGTGGGGACAGGGGTGTGAGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGAAAAATACAGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGATAGGGGTGTGTGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGCTGTGGGGACAGGGGTGTGGGGACAGGGGTCCTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGGGGTGTGGGGACAGGGGTCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCCGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCTGGGGACAGGGGTCTGGGGATAGGGGTGTGGGGACAGGGGTCTGGGGACAGGGGTGTGGGGACAGGGGTCTGGGGATAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTGTGGGGACAGGGGTCCTGGGGACAGGGGTCTGGGGACAGCAGCGCAAAGAGCCCCGCCCTGCAGCCTCCAGCTCTCCTGGTCTAATGTGGAAAGTGGCCCAGGTGAGGGCTTTGCTCTCCTGGAGACATTTGCCCCCAGCTGTGAGCAGGGACAGGTCTGGCCACCGGGCCCCTGGTTAAGACTCTAATGACCCGCTGGTCCTGAGGAAGAGGTGCTGACGACCAAGGAGATCTTCCCACAGACCCAGCACCAGGGAAATGGTCCGGAAATTGCAGCCTCAGCCCCCAGCCATCTGCCGACCCCCCCACCCCAGGCCCTAATGGGCCAGGCGGCAGGGGTTGACAGGTAGGGGAGATGGGCTCTGAGACTATAAAGCCAGCGGGGGCCCAGCAGCCCTCAGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGGTTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGCCTGTCTCCCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGGTGAGCCAACCGCCCATTGCTGCCCCTGGCCGCCCCCAGCCACCCCCTGCTCCTGGCGCTCCCACCCAGCATGGGCAGAAGGGGGCAGGAGGCTGCCACCCAGCAGGGGGTCAGGTGCACTTTTTTAAAAAGAAGTTCTCTTGGTCACGTCCTAAAAGTGACCAGCTCCCTGTGGCCCAGTCAGAATCTCAGCCTGAGGACGGTGTTGGCTTCGGCAGCCCCGAGATACATCAGAGGGTGGGCACGCTCCTCCCTCCACTCGCCCCTCAAACAAATGCCCCGCAGCCCATTTCTCCACCCTCATTTGATGACCGCAGATTCAAGTGTTTTGTTAAGTAAAGTCCTGGGTGACCTGGGGTCACAGGGTGCCCCACGCTGCCTGCCTCTGGGCGAACACCCCATCACGCCCGGAGGAGGGCGTGGCTGCCTGCCTGAGTGGGCCAGACCCCTGTCGCCAGGCCTCACGGCAGCTCCATAGTCAGGAGATGGGGAAGATGCTGGGGACAGGCCCTGGGGAGAAGTACTGGGATCACCTGTTCAGGCTCCCACTGTGACGCTGCCCCGGGGCGGGGGAAGGAGGTGGGACATGTGGGCGTTGGGGCCTGTAGGTCCACACCCACTGTGGGTGACCCTCCCTCTAACCTGGGTCCAGCCCGGCTGGAGATGGGTGGGAGTGTGACCTAGGGCTGGCGGGCAGGCGGGCACTGTGTCTCCCTGACTGTGTCCTCCTGTGTCCCTCTGCCTCGCCGCTGTTCCGGAACCTGCTCTGCGCGGCACGTCCTGGCAGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGCCCTGCTGTGCCGTCTGTGTGTCTTGGGGGCCCTGGGCCAAGCCCCACTTCCC'
#DNA sequence of Human beta hemoglobin gene
dna2='AGACAAAACTCTTCCACTTTTAGTGTTCTTATTTGTGTAATAAGAAAATTGGGAAAACGATCTTCAATATGCTTACCAAGCTGTGATTCCAAATATTACGTAAATACACTTGCAAAGGAGGATGTTTTTAGTAGCAATTTGTACTGATGGTATGGGGCCAAGAGATATATCTTAGAGGGAGGGCTGAGGGTTTGAAGTCCAACTCCTAAGCCAGTGCCAGAAGAGCCAAGGACAGGTACGGCTGTCATCACTTAGACCTCACCCTGTGGAGCCACACCCTAGGGTTGGCCAATCTACTCCCAGGAGCAGGGAGGGCAGGAGCCAGGGCTGGGCATACAAGTCAGGGCAGAGCCATCTATTGCTTACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGTTGGTATCAAGGTTACAAGACAGGTTTAAGGAGACCAATAGAAACTGGGCATGTGGAGACAGAGAAGACTCTTGGGTTTCTGATAGGCACTGACTCTCTCTGCCTATTAGTCTATTTTCCCACCCTTAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGGTGAGTCTATGGGACCCTTGATGTTTTCTTTCCCCTTCTTTTCTATGGTTAAGTTCATGTCATAGGAAGGGGAGAAGTAACAGGGTACAGTTTAGAATGGGAAACAGACGAATGATTGCATCAGTGTGGAAGTCTCAGGATCGTTTTAGTTTCTTTTATTTGCTGTTCATAACAATTGTTTTCTTTTGTTTAATTCTTGCTTTCTTTTTTTTTCTTCTCCGCAATTTTTACTATTATACTTAATGCCTTAACATTGTGTATAACAAAAGGAAATATCTCTGAGATACATTAAGTAACTTAAAAAAAAACTTTACACAGTCTGCCTAGTACATTACTATTTGGAATATATGTGTGCTTATTTGCATATTCATAATCTCCCTACTTTATTTTCTTTTATTTTTAATTGATACATAATCATTATACATATTTATGGGTTAAAGTGTAATGTTTTAATATGTGTACACATATTGACCAAATCAGGGTAATTTTGCATTTGTAATTTTAAAAAATGCTTTCTTCTTTTAATATACTTTTTTGTTTATCTTATTTCTAATACTTTCCCTAATCTCTTTCTTTCAGGGCAATAATGATACAATGTATCATGCCTCTTTGCACCATTCTAAAGAATAACAGTGATAATTTCTGGGTTAAGGCAATAGCAATATTTCTGCATATAAATATTTCTGCATATAAATTGTAACTGATGTAAGAGGTTTCATATTGCTAATAGCAGCTACAATCCAGCTACCATTCTGCTTTTATTTTATGGTTGGGATAAGGCTGGATTATTCTGAGTCCAAGCTAGGCCCTTTTGCTAATCATGTTCATACCTCTTATCTTCCTCCCACAGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAATGATGTATTTAAATTATTTCTGAATATTTTACTAAAAAGGGAATGTGGGAGGTCAGTGCATTTAAAACATAAAGAAATGAAGAGCTAGTTCAAACCTTGGGAAAATACACTATATCTTAAACTCCATGAAAGAAGGTGAGGCTGCAAACAGCTAATGCACATTGGCAACA'

#Converting DNA to mRNA
mrna=dna.replace('A','U').replace('T','A').replace('G','C').replace('C','G')
mrna2=dna2.replace('A','U').replace('T','A').replace('G','C').replace('C','G')

#Picking the start codon of the protein synthesis
m = re.search('AUG(.+?)GGGGGUGAAGGG', mrna)
pmrna = m.group(0)
m2 = re.search('AUG(.+?)UGUGGAUUAGGUGUAAGGGUUGU', mrna2)
pmrna2 = m2.group(0)

#Converting mRNA into amino acid sequences
# Reference: http://www.petercollingridge.co.uk/book/export/html/474
bases = ['u', 'c', 'a', 'g']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))


def translate(seq):
    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''
    
    for i in range(0, len(seq),3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break

return peptide

#amnio acid sequences used as observations for Baum-Welch algorithm
obs1 = translate(pmrna)
obs2 = translate(pmrna2)
obs1 = list(obs1)
obs2 = list(obs2)

# Combine both observations to extract unique elements from them
combObs = obs1+obs2
sizeOfElements = len(set(combObs))
#print(sizeOfElements)

# Initializing Parameters
# States - the biochemical property of amnio acid n - non-polar p- polar, b-basic a-acidic.
states = list('n'*5) + list('p'*4) +  list('b'*1) +  list('a'*1)

#Possible observations
possible_observation = tuple(set(combObs))

# Number of observation sequece 1 and observation sequence 2
quantities_observations = [10, 20]
observation_tuple = []
observation_tuple.extend( [obs1,obs2] )

# Input parameters as Numpy matrices
#Matrix are random numbers between 0 and 1 and each column sums up to 1.
#These are inital start, emission, transition probability values for the model
start_probability = np.random.rand(len(states))
start_probability = np.matrix(start_probability/start_probability.sum(axis=0,keepdims=1))

transition_probability = np.random.rand(len(states), len(states))
transition_probability = np.matrix(transition_probability/transition_probability.sum(axis=1,keepdims=1))

emission_probability = np.random.rand(len(states), sizeOfElements)
emission_probability = np.matrix(emission_probability/emission_probability.sum(axis=1,keepdims=1))

# to put all the inputs to the hmm model; to define the model with all the parameters
test = hmm(states,possible_observation,start_probability, transition_probability,emission_probability)

# Baum-welch Algorithm
#the log probability is taken to prevent any overflow error
prob = test.log_prob(observation_tuple, quantities_observations)
print ("probability of sequence with original parameters : %f"%(prob))

#Sequence on which Baum welch algoritm was applied on
print("observation_tuple is",observation_tuple)
print("quantities_observations",quantities_observations)

#Apply Baum-welch Algorithm
num_iter=5000 #Number of iternation
#train the model and get emission, transition, and start as an ouput
emission,transition,start = test.train_hmm(observation_tuple,num_iter,quantities_observations)

#Print output after applying the algorithm
print("The emission probability",emission)
print("The start probability",start)
print("The transition probability",transition)

#the probability using the new emission, start and transition probability
prob = test.log_prob(observation_tuple, quantities_observations)
print ("probability of sequence after %d iterations : %f"%(num_iter,prob))

