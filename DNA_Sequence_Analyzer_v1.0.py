valid=True

seq = input("Enter your sequence here: ").upper()
valid_bases = ["A","C","G","T"]
for base in seq:
    if base not in valid_bases:
        print("Invalid base: ", base)
        valid=False
        break

if valid:
    motif = input("Motif to search for: ").upper()

    print("")
    print("Length of Original Sequence: ", len(seq),"bp")
    print()

    print("==== Base count & Per-base composition (%) ====")
    print("A:", seq.count("A"), "-",round( seq.count("A") / len(seq) * 100,2), "%")
    print("T:", seq.count("T"), "-",round( seq.count("T") / len(seq) * 100,2), "%")
    print("G:", seq.count("G"), "-",round( seq.count("G") / len(seq) * 100,2), "%")
    print("C:", seq.count("C"), "-",round( seq.count("C") / len(seq) * 100,2), "%")
    print()

    gc_count = seq.count("G") + seq.count("C")
    gc_content = gc_count / len(seq) * 100
    print("GC content: ",round(gc_content,2), "%")

    motif_count = 0
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i + len(motif)] == motif:
            motif_count += 1
            print("motif found at position: ", i + 1)
    print("Total motifs found: ", motif_count)
    print()

    complement = ""
    for base in seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    print("==== Reverse complement sequence ====\n",complement)
