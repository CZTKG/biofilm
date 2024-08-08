import subprocess

sra_list_file = 'SRR_Acc_List.txt'

# Read the accession numbers from the file
with open(sra_list_file, 'r') as file:
    sra_accessions = file.read().splitlines()

# Prefetch each SRA accession
for sra in sra_accessions:
    print(f"Prefetching {sra}...")
    subprocess.run(['prefetch', sra])

print("Prefetching completed.")
