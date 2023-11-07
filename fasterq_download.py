import subprocess

sra_numbers = [
    "SRR1976144", "SRR1976143", "SRR1976141", "SRR1976140",
"SRR1976138", "SRR1976137", "SRR1976135", "SRR1976134",
"SRR1976132", "SRR1976131", "SRR1976127", "SRR1976125",
"SRR1976123", "SRR1976122", "SRR1976120", "SRR1976119",
"SRR1976116", "SRR1976115", "SRR1976113", "SRR1976112",
"SRR1976110", "SRR1976109", "SRR1976107", "SRR1976106",
"SRR1976105", "SRR1976103", "SRR1976101", "SRR1976100",
"SRR1976098", "SRR1976097", "SRR1976095", "SRR1976094"
    ]

input_directory = "/path/to/input_directory"  # Change this to your desired directory

# Ensure the custom directory exists
subprocess.call(f"mkdir -p {input_directory}", shell=True)

for sra_id in sra_numbers:
    print("Currently downloading: " + sra_id)
    prefetch_cmd = f"prefetch -O {input_directory} {sra_id}"
    print("The command used was: " + prefetch_cmd)
    subprocess.call(prefetch_cmd, shell=True)

# this will convert the .sra files from above into .fastq files
for sra_id in sra_numbers:
    print("Generating fastq for: " + sra_id)
    fasterq_dump_cmd = f"fasterq-dump {sra_id} --outdir {input_directory}/fastq"
    print("The command used was: " + fasterq_dump_cmd)
    subprocess.call(fasterq_dump_cmd, shell=True)

    # now compress the resulting .fastq files with gzip
    print("Compressing fastq files for: " + sra_id)
    gzip_cmd = f"gzip {input_directory}/fastq/{sra_id}*.fastq"
    print("The command used was: " + gzip_cmd)
    subprocess.call(gzip_cmd, shell=True)
