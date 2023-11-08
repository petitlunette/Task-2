library(DESeq2) # Load required library and set directory
setwd("path/to/trimmed_directory")
samples_info <- data.frame(
run_accession = c(
"SRR1976094", "SRR1976095", "SRR1976097", "SRR1976098", "SRR1976100", "SRR1976101", "SRR1976103", "SRR1976105", "SRR1976106", "SRR1976107", "SRR1976109", "SRR1976110", "SRR1976112", "SRR1976113", "SRR1976115", "SRR1976116", "SRR1976119", "SRR1976120", "SRR1976122", "SRR1976123",
"SRR1976125", "SRR1976127", "SRR1976131", "SRR1976132", "SRR1976134", "SRR1976135", "SRR1976137", "SRR1976138", "SRR1976140", "SRR1976141", "SRR1976143", "SRR1976144"),
cultivar = rep(c("SC 782", "SC 803", "SC 60", "SC 110", "SC 25", "SC 15", "SC 1076", "SC 1439"), each = 4),
treatment = rep(c("Control", "Drought stress"), 16),
tissue = rep(c("Leaf", "Leaf", "Root", "Root"), 8),
stringsAsFactors = FALSE
)
# Reading the counts and assigning gene IDs as row names
allCounts <- sapply(samples_info$run_accession, function(accession) {
  counts <- read.delim(paste0(accession, "_ReadsPerGene.out.tab"), header=FALSE, skip=4)
  gene_ids <- counts[,1] 
  counts_unstranded <- counts[,2]
  names(counts_unstranded) <- gene_ids  # Assign gene IDs as names
  return(counts_unstranded)
})

allCounts <- do.call(cbind, allCounts) # Convert the counts from a list to a matrix
rownames(allCounts) <- gene_ids # Ensure the row names of the matrix are the gene IDs
# Create a DESeqDataSet
deseqdataset <- DESeqDataSetFromMatrix(countData = allCounts,
                              colData = samples_info,
                              design = ~ cultivar + treatment + tissue)
deseqdataset <- DeSeq(deseqdataset)
