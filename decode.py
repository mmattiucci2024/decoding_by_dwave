#####################################################
# THIS IS JUST AN EASY EXAMPLE.
# IT WORKS BUT YOU NEED A DWAVE SUBSCRIPTION AND AN ACTIVE
# VENV (Virtual Environment) FOR IT TO WORK.
#####################################################
# Task:
# The quantum annealer DWAVE is decoding a matrix Q (dictionary format)
# that encodes the binary sequence [1, 0, 0, 1].
# The solution to the QUBO problem for the quadratic form Q
# is unique and consists of more than 4 bits.
# Remember that the only decoding indices to consider are [0, 1, 3, 5].
#
from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
Q = {('x0', 'x3'): 1, ('x0', 'x4'): -2, ('x0', 'x7'): 5, ('x0', 'x8'): -10, ('x1', 'x1'): -5, ('x1', 'x2'): 21, ('x1', 'x3'): -2, ('x2', 'x2'): -5, ('x2', 'x3'): -2, ('x2', 'x6'): 5, ('x2', 'x7'): -10, ('x3', 'x3'): -2, ('x3', 'x4'): 18, ('x4', 'x4'): -2, ('x4', 'x5'): 5, ('x4', 'x6'): -10, ('x4', 'x7'): 1, ('x4', 'x8'): -2, ('x5', 'x6'): -9, ('x5', 'x7'): -2, ('x6', 'x6'): 15, ('x6', 'x7'): -12, ('x7', 'x7'): 18, ('x7', 'x8'): -12, ('x8', 'x8'): 2}
sampleset = sampler.sample_qubo(Q, num_reads=5000, label='Encoded sequence [1, 0, 0, 1]')
print(sampleset)
quit()
