# Pipeline-Project
COMP 383 Pipeline Project

**STEP 1**

**Download transcriptome data from NCBI using wget**

Donor1 2dpi SRA link: https://www.ncbi.nlm.nih.gov/sra/SRX2896360

Donor2 6dpi SRA link: https://www.ncbi.nlm.nih.gov/sra/SRX2896363

wget https://www.ncbi.nlm.nih.gov/sra/SRX2896360 

wget https://www.ncbi.nlm.nih.gov/sra/SRX2896363 

These two wget lines of code in the command line will retrieve SRA files from NCBI

**Convert SRA files to paired-end FASTQ files**

           import os #module for operating system interactions

           import subprocess #creation of new processes

           project_directory = "PipelineProject_SnehaChowdhury" #name project directory 

           os.makedirs(project_directory, exist_ok=True) #make project directory

           os.chdir(project_directory) #change current working directory

           SRA_ids = {"2dpi" : "SRR5660030", #SRX2896360
           "6dpi": "SRR5660033"} #SRX2896363

           for label, sra_id in SRA_ids.items():

               subprocess.run(f"fastq-dump --split-files {sra_id} -O .", shell=True, check=True)
    
               #convert to fastq files
