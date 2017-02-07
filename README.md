# Ederson
Retrive sequences from refseq:
```{bash}
curl -s 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_017775,NC_017810&rettype=fasta'
```
This would retrieve sequnces for NC_017775 and NC_017810, you can add more by seperating the IDs by a comma. Perhaps make a for loop for this. 
