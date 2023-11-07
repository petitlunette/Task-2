import subprocess

sra_numbers = [
    "SRRXXXXXXX", "SRRXXXXXXX" 
    ]

input_directory = "/path/to/input_directory"  # Change this to your desired directory, if a unicode error appears at this line use directory =r"path"

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
