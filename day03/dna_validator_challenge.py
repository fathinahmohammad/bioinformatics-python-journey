# ======================
# DNA SEQUENCE VALIDATOR CHALLENGE
# ======================

# 1. I gotta store DNA seq 

dna = "ATGCATGC"

# 2. Convert to uppercase 

dna = dna.upper()

# 3. Keep DNA seq in a variable

for nucleotide in dna:
    print(nucleotide)


# 4. Define valid nucleotide 

valid_bases = "ATGC"

# 5. Prepare empty variable

invalid_bases = ""

# 6. Check every nucleotide

for nucleotide in dna:
    if nucleotide not in valid_bases:
        invalid_bases = invalid_bases + nucleotide

# 7. Determine DNA status

if dna == "":
    print ("ERROR: Empty DNA Sequence")

elif invalid_bases  == "":

    print("DNA STATUS: VALID")


else:

    print("DNA STATUS: INVALID")
    print("Invalid nucleotides:" , invalid_bases)


# 8. Display sequence information 

print ("DNA Sequence:"  , dna)
print("Sequence Length:"  , len(dna))