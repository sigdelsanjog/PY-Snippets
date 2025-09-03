''' Example2 Here we implement the concept of OOP in python to model a Gene.and
Class has three methods which are functionalities used in gene analysis. They arefollowing:
Method 1: Calculate GC Content,
Method 2: Transcribe DNA to RNA,
Method 3: Reverse Complement.
'''
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()

    def length(self):
        return len(self.sequence)

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self.sequence) * 100

    def transcribe(self):
        return self.sequence.replace("T", "U")

    def reverse_complement(self):
        complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
        return "".join(complement[base] for base in reversed(self.sequence))

''' 
Here we create an instance of the Gene class and assign it to the variable gene1.
Then we print the various attributes and methods of the gene1 object.
'''
gene1 = Gene("BRCA1", "ATGCGTACGTAGCTAG")
print("Gene:", gene1.name)
print("Length:", gene1.length())
print("GC Content:", gene1.gc_content())
print("mRNA Transcript:", gene1.transcribe())
print("Reverse Complement:", gene1.reverse_complement())


'''
Biological Concepts Behind OOP Methods
1. GC Content
DNA is made of 4 bases: A, T, G, C
GC content = % of nucleotides that are either G or C

- Higher GC → more stable DNA (3 hydrogen bonds vs 2 for AT)
- Used in PCR primer design, genome analysis
Example:
DNA = ATGCGT → GC = 3 out of 6 → 50% GC content

2. Transcription (DNA → RNA)
In cells, DNA is used as a template to make RNA
Rule: T in DNA is replaced with U in RNA
Python method: .replace("T", "U")
Useful for simulating gene expression
Example:
DNA = ATGC → RNA = AUGC

3. Reverse Complement
DNA is double-stranded, complementary and anti-parallel
Base-pairing rules:
A ↔ T
G ↔ C
Reverse complement = reverse the sequence + replace with complement bases
Used in sequencing, primer design, and understanding both DNA strands
Example:
DNA = ATGC → Reverse = CGTA → Complement = GCAT
'''
