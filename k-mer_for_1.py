from Bio import SeqIO
import sys

#usage python k-mer_for_1.py target.fa #(kmer length(bp)) %(97)
def kmer_count2(dna, k, minimum_percentage):
    total_kmers = len(dna) - k + 1
    minimum_count = (total_kmers * minimum_percentage) / 100
    print("min count is " + str(minimum_count))
    # first assemble dict of kmer counts
    kmer2count = {}
    for x in range(len(dna)+1-k):
        kmer = dna[x:x+k]
        kmer2count[kmer] = kmer2count.get(kmer, 0) + 1
 
    # now select just the high-count kmers
    for kmer, count in kmer2count.items():
        if count < minimum_count:
            del kmer2count[kmer]
    print(len(kmer2count))
    return(kmer2count)

def main():
	
	for record in SeqIO.parse(sys.argv[1], "fasta"):
		#print(record.id)
		dna = record.seq
	k = int(sys.argv[2])
	minimum_percentage = float(sys.argv[3])
	kmer2count = kmer_count2(dna, k, minimum_percentage)

if __name__ == '__main__':
	main()
