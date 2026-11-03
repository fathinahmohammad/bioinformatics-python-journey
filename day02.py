# ==================================
# DNA COMPOSITION ANALYZER
# Day 2 - Bioinformatics Python
# ==================================

# 1. DNA sequence

dna = "ATGCGTACCGTA"

# 2. Convert to uppercase

dna = dna.upper()

# 3. Count nucleotides

A = dna.count("A")
T = dna.count("T")
G = dna.count("G")
C = dna.count("C")

# 4. Calculate sequence length

total = len(dna)

# 5. Calculate GC content

gc_content = ((G + C) / total) * 100

# 6. Display report

print("==========================")
print("DNA COMPOSITION ANALYZER")
print("==========================")

print("DNA Sequence:", dna)

print("Total Length:", total)

print("Adenine (A):", A)
print("Thymine (T):", T)
print("Guanine (G):", G)
print("Cytosine (C):", C)

print("GC Content:", gc_content, "%")

print("==========================")