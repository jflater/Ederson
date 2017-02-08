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
```{bash}
curl -s 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_017775,NC_017810&rettype=fasta'
```
This would retrieve sequnces for NC_017775 and NC_017810, you can add more by seperating the IDs by a comma. Perhaps make a for loop for this. 
