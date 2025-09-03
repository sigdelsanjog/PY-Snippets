""" Example 1: Modeling a Gene in python OOP Concepts: Class Objects and Methods.
Here we define a Gene class with methods to analyze DNA sequences.
"""
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def length(self):
        return len(self.sequence)

'''
To call an object or creating an object we define a new variable and assign it an instance of the class. 
Here we create an instance of the Gene class and assign it to the variable gene1
'''
gene1 = Gene("BRCA1", "ATGCGTACGTAGCTAG")
print(gene1.name, gene1.length())
