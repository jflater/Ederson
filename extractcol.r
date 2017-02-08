library(xlsx)

df <- read.xlsx("<filename.xlsx>")
IDs[paste(df[,[n-1]])]
write.table(IDs, "IDs.txt, sep="\t", col.names=T)

