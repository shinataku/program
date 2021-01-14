import subprocess, os
command = ("arggluobj ~/protein/dataset/pdb_dataset/data0309_wh/2cg5A_B.pdb ~/protein/dataset/stride_dataset/data0309_wh/2cg5A_B.txt ~/protein/dataset/hb2_dataset/out_hb2_dir/data0309_wh/2cg5A_B.hb2 A B")
test = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,universal_newlines=True)
a = 0;
for line in test.stdout:
    if(line[0:4]=="Nohb"):
        print("NoHB :: "+line[5:7])
        a += int(line[5:7])
    if(line[0:4]=="Hb  "):
        print("HB :: "+line[5:7])
        a += int(line[5:7])

print(a)
