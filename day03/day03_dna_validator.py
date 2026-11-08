# ==================================
# DNA SEQUENCE VALIDATOR
# DAY 3 - BIOINFORMATICS
# ==================================

# 1. Store DNA sequence

dna = "ATGCGTACCGTA"

# 2. Convert to uppercase

dna = dna.upper()

# 3. Define valid nucleotides

valid_bases = "ATGC"

# 4. Prepare an empty variable

invalid_bases = ""

# 5. Check every nucleotide

for nucleotide in dna:

    if nucleotide not in valid_bases:

        invalid_bases = invalid_bases + nucleotide

# 6. Determine DNA status

if dna == "":

    print("ERROR: Empty DNA sequence")

elif invalid_bases == "":

    print("DNA STATUS: VALID")

else:

    print("DNA STATUS: INVALID")
    print("Invalid nucleotides:", invalid_bases)

# 7. Display sequence information

print("DNA Sequence:", dna)
print("Sequence Length:", len(dna))