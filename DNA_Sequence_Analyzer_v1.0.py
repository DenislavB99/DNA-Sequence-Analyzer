valid=True  # Sequence Validation segment.

seq = input("Enter your sequence here: ").upper() # Converts sequence input to uppercase.
valid_bases = ["A","C","G","T"] # Holds the bases for validation.
for base in seq:
    if base not in valid_bases: # If the input doesn't match one of the bases, analysis stops and points out the missmatch.
        print("Invalid base: ", base)
        valid=False
        break

if valid:   # Sequence Validation segment continues with analysis.

    motif = input("Search for motif (leave blank to skip search): ").upper()  # Converts motif input to uppercase.

    print() # Analysis segment start.
    print("Length of Original Sequence: ", len(seq),"bp")
    print()

    print("==== Base count & Per-base composition (%) ====")    # Counting nucleotides and their per-base composition.
    print("A:", seq.count("A"), "-",round( seq.count("A") / len(seq) * 100,2), "%")
    print("T:", seq.count("T"), "-",round( seq.count("T") / len(seq) * 100,2), "%")
    print("G:", seq.count("G"), "-",round( seq.count("G") / len(seq) * 100,2), "%")
    print("C:", seq.count("C"), "-",round( seq.count("C") / len(seq) * 100,2), "%")
    print()

    print("=== GC Content ===") # GC content segment counts the percentages og G and C bases in the sequence.
    gc_count = seq.count("G") + seq.count("C")
    gc_content = gc_count / len(seq) * 100
    print("GC content: ",round(gc_content,2), "%")
    print()

    print("=== Motif Search ===")
    if motif:
        motif_count = 0 # Stores found motifs form the sequence.
        for i in range(len(seq) - len(motif) + 1): # Looks for the motif along the whole sequence in a moving window the size of the motif.
            if seq[i:i + len(motif)] == motif:
                motif_count += 1
                print("motif found at position: ", i + 1)   # Prints the positions of the motifs and adjusts for their biological positions with "i + 1".
        print("Total motifs found: ", motif_count)
    print()

    complement = "" # Stores the complementary reverse sequence.
    for base in seq:    # Reads the bases in the sequence and replaces them with their complementary bases.
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    reverse_strand = complement[::-1]

    print("==== Reverse complement sequence ====\n",reverse_strand)
    # Analysis segment ends.

    # ====== Future addons =========
    # - GC content by regions
    # - Codon analysis