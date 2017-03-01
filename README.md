# Ederson
# List of accesion numbers in Accession_numbers_for_Jared_and_Adina.xlsx
## Extract refseq IDs: extractcol.r
# G1:Rhizobium tropici CIAT 899 (+chromosome) 
1. NC_020059.1+
2. NC_020060.1
3. NC_020061.1
4. NC_020062.1
----
# G2:Rhizobium freirei PRF 81
5. NZ_AQHN01000095.1
6. NZ_AQHN01000096.1
7. NZ_AQHN1000084.1-could not find this on NCBI
---
## Find unique sequences in a refrence genome not found in a group of comparision genomes
k-mer.py
Python script that takes two arguments for the refrence genome and compares them another group
Usage:
```sh
python k-kmer.py [reference1.fa] [reference2.fa] [comparison1.fa] [comarison-n+1.fa]
```
This prints the k-mers from the refrence genome into a .txt file
###Note: k-mer script will not change output file name and also prints /n after each kmer string
