def find_similar(seq1,seq2):
    match=0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            match+=1
    return match
if __name__ == "__main__":
    org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
    org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]
    threshold = 50
    similar_pairs=[(i,j) for i in org1 for j in org2 if (find_similar(i,j)/8)*100>=50]
    print(similar_pairs)
