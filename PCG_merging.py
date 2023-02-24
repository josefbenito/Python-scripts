#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Merging individual protein coding genes alignment 


f_1 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad1_msa_mafft_rev.fasta", "r")
f_2 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad4_msa_mafft_rev.fasta", "r")
f_3 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad4l_msa_mafft_rev.fasta", "r")
f_4 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad5_msa_mafft_rev.fasta", "r")
f_5 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Atp6_msa_mafft_rev.fasta", "r")
f_6 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Atp8_msa_mafft_rev.fasta", "r")
f_7 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Cob_msa_mafft_rev.fasta", "r")
f_8 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Cox1_msa_mafft_rev.fasta", "r")
f_9 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Cox2_msa_mafft_rev.fasta", "r")
f_10 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Cox3_msa_mafft_rev.fasta", "r")
f_11 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad2_msa_mafft_rev.fasta", "r")
f_12 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad3_msa_mafft_rev.fasta", "r")
f_13 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Nad6_msa_mafft_rev.fasta", "r")

outfile = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Sty-indentatus_Alignment_rev.fasta","w")

samples = ['>MP25A;', '>MP26A;', '>MP28A;', '>MP31B;', '>MP53A;', '>NC_0196611;', '>NC_0263091;', '>NC_0144921;', '>NC_0146871;', '>NC_0333601;',\
           '>NC_0231041;', '>NC_0255641;', '>NC_0364291;', '>NC_0177601;', '>NC_0349371;', '>NC_0333611;', '>NC_0161921;', '>NC_0196541;', '>NC_0196551;',\
           '>NC_0196561;', '>NC_0196581;', '>NC_0130321;', '>NC_0196591;', '>NC_0196601;', '>NC_019653;', '>HE8605061;', '>NC_0138191;', '>NC_0333621;',\
           '>NC_0196622;', '>NC_0302611;']

def MergePCG(f, pcg):
    
    a = f.readlines()
    b = len(a)
    
    print_flag = False
    
    rec = ""
    
    for c in range(b):
        spl = a[c].split()
        if pcg in spl:
            print_flag = True
    
        if print_flag:
            rec += " ".join(spl)
            rec += "\n"
            word = a[c+1].split()
            for i in word:
                if "+;" in i or "-;" in i:
                    print_flag = False
                    break
            if print_flag == False:
                break
    return rec

g_1 = MergePCG(f_1, samples[29])
g_2 = MergePCG(f_2, samples[29])
g_3 = MergePCG(f_3, samples[29])
g_4 = MergePCG(f_4, samples[29])
g_5 = MergePCG(f_5, samples[29])
g_6 = MergePCG(f_6, samples[29])
g_7 = MergePCG(f_7, samples[29])
g_8 = MergePCG(f_8, samples[29])
g_9 = MergePCG(f_9, samples[29])
g_10 = MergePCG(f_10, samples[29])
g_11 = MergePCG(f_11, samples[29])
g_12 = MergePCG(f_12, samples[29])
g_13 = MergePCG(f_13, samples[29])

h_1 = g_1.split()
h_2 = g_2.split()
h_3 = g_3.split()
h_4 = g_4.split()
h_5 = g_5.split()
h_6 = g_6.split()
h_7 = g_7.split()
h_8 = g_8.split()
h_9 = g_9.split()
h_10 = g_10.split()
h_11 = g_11.split()
h_12 = g_12.split()
h_13 = g_13.split()

output = h_1[0] + "\n"
output += "".join(h_1[6: ]) + "".join(h_2[6: ]) + "".join(h_3[6: ]) + "".join(h_4[6: ]) + "".join(h_5[6: ]) + "".join(h_6[6: ]) \
        + "".join(h_7[6: ]) + "".join(h_8[6: ]) + "".join(h_9[6: ]) + "".join(h_10[6: ]) + "".join(h_11[6: ]) + "".join(h_12[6: ]) + "".join(h_13[6: ]) 
outfile.write(output)

f_1.close()
f_2.close()
f_3.close()
f_4.close()
f_5.close()
f_6.close()
f_7.close()
f_8.close()
f_9.close()
f_10.close()
f_11.close()
f_12.close()
f_13.close()
outfile.close()