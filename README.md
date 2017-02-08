# Ederson
# List of accesion numbers in Accession_numbers_for_Jared_and_Adina.xlsx

##Extract refseq IDs: extractcol.r
```{r}
getwd()
setwd("/Users/jaredflater/Documents/Ederson/")
library(readxl)
Accession_numbers_for_Jared_and_Adina <- read_excel("~/Documents/Ederson/Accession numbers for Jared and Adina.xlsx")
View(Accession_numbers_for_Jared_and_Adina)

df <- Accession_numbers_for_Jared_and_Adina$Refseq

write.(df, "IDs.txt", sep="\t")
```
Retrive sequences from refseq:
#G1:Rhizobium tropici CIAT 899 (+chromosome) 
1. NC_020059.1+
2. NC_020060.1
3. NC_020061.1
4. NC_020062.1
#G2:
5. NZ_AQHN01000095.1
6. NZ_AQHN01000096.1
7. NZ_AQHN1000084.1-could not find this on NCBI
```{bash}
#Not working
curl -s 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_017775,NC_017810&rettype=fasta'
```
This would retrieve sequnces for NC_017775 and NC_017810, you can add more by seperating the IDs by a comma. Perhaps make a for loop for this. 
