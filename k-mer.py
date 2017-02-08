
#bp = target length of k-mer
#g = metagenome sequence to look for k-mers 

def kmer_count(g,bp)
   f={}
   for x in range(len(g)+1-bp):
      kmer=g[x:x+bp]
      f[kmer]=f.get(kmer,0)+1
   return(f)
