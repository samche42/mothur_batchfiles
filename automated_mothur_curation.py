#Usage: automated_mothur_curation.py ./ 
#This assumes that you are in the directory with only reads that you want to analyse 
#e.g. only fwd reads, or only rev reads, are in this directory, NOT BOTH

#!/usr/bin/env python3
import os
from glob import glob

files = []
start_dir = os.getcwd()

output = open("batchfile1","w")

trim_files = [file for file in os.listdir(start_dir) if file.endswith(".fastq")]
for trim in trim_files:
        base = os.path.basename(trim)
        file_name = str(os.path.splitext(base)[0])
        fasta_create = "fastq.info(fastq="+file_name+".fastq)\n"
        output.write(fasta_create)
        trim = "trim.seqs(fasta="+file_name+".fasta, qfile="+file_name+".qual, qwindowaverage=20, minlength=250, processors=16)\n"
        output.write(trim)

#Merging fasta files
output.write("merge.files(input=")
string = ""
fasta_files = [file for file in os.listdir(start_dir) if file.endswith(".fastq")]
for fasta in fasta_files:
    base = os.path.basename(fasta)
    file_name = os.path.splitext(base)[0]
    merge = str(file_name)+".trim.fasta-"
    string = string+merge

string = string[:-1]
string = string +",output=ABC.trim.contigs.fasta)\n"
output.write(string)

#Merging group files
output.write("merge.files(input=")
string = ""
fasta_files = [file for file in os.listdir(start_dir) if file.endswith(".fastq")]
for fasta in fasta_files:
    base = os.path.basename(fasta)
    file_name = os.path.splitext(base)[0]
    merge = str(file_name)+".trim.count_table-"
    string = string+merge

string = string[:-1]
string = string +",output=ABC.trim.count_table)"
output.write(string)

output.close()
