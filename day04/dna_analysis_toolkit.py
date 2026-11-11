# ==========================================
# DNA ANALYSIS TOOLKIT
# DAY 4 - BIOINFORMATICS PYTHON
# ==========================================


# FUNCTION 1: DNA VALIDATION

def validate_dna(dna):

    dna = dna.upper()

    valid_bases = "ATGC"

    if len(dna) == 0:
        return False

    for nucleotide in dna:

        if nucleotide not in valid_bases:
            return False

    return True


# FUNCTION 2: COUNT NUCLEOTIDES

def count_nucleotide(dna, base):

    return dna.count(base)


# FUNCTION 3: CALCULATE GC CONTENT

def calculate_gc(dna):

    total = len(dna)

    if total == 0:
        return 0

    G = dna.count("G")
    C = dna.count("C")

    gc_content = ((G + C) / total) * 100

    return gc_content


# ==========================================
# MAIN PROGRAM
# ==========================================

dna = "ATGCGTACCGTA"

dna = dna.upper()

print("==============================")
print("       DNA ANALYSIS TOOL")
print("==============================")

print("DNA Sequence:", dna)

if validate_dna(dna):

    print("DNA Status: VALID")

    print("Sequence Length:", len(dna))

    print("A:", count_nucleotide(dna, "A"))
    print("T:", count_nucleotide(dna, "T"))
    print("G:", count_nucleotide(dna, "G"))
    print("C:", count_nucleotide(dna, "C"))

    print("GC Content:", calculate_gc(dna), "%")

else:

    print("DNA Status: INVALID")

print("==============================")