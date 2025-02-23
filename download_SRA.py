import os #module for operating system interactions
import subprocess #creation of new processes

project_directory = "PipelineProject_Your_Name" #name project directory 
os.makedirs(project_directory, exist_ok=True) #make project directory
os.chdir(project_directory) #change current working directory

SRA_ids = {"2dpi" : "SRR5660030", #SRX2896360
           "6dpi": "SRR5660033"} #SRX2896363

for label, sra_id in SRA_ids.items():
    subprocess.run(f"fastq-dump --split-files {sra_id} -O .", shell=True, check=True)
    #convert to fastq files
