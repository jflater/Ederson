df <- read.table("<filename.txt>", +
   header = TRUE)
IDs[paste(df[,[n-1]])]
write.table(IDs, "IDs.txt, sep="\t", col.names=T)

