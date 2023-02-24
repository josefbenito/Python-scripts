#!/usr/bin/env python2
# -*- coding: utf-8 -

#Consolidating individual protein coding genes 


f_1 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP25A/Raw_kmer_31/MITOS_rearranged/MP25A_PCG.fasta", "r")
f_2 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/grabb-master/grabb_results/MP26A/MITOS_rearranged/MP26A_PCG.fasta", "r")
f_3 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP28A/Kmer_45/MITOS/MP28A_PCG.fasta", "r")
f_4 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP31B/kmer_31_rev/MITOS/MP31B_PCG.fasta", "r")
f_5 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP53A/Kmer_45/MITOS/MP53A_PCG.fasta", "r")
f_6 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Bahadzia-jaraguensis/NC0196611.fas", "r")
f_7 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Brachyuropus-grewingkii/NC0263091.fas", "r")
f_8 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Caprella-mutica/NC0144921.fas", "r")
f_9 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Caprella-scaura/NC0146871.fas", "r")
f_10 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-cyaneus/NC0333601.fas", "r")
f_11 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-verrucosus/NC0231041.fas", "r")
f_12 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-vittatus/NC0255641.fas", "r")
f_13 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eurythenes-maldoror/NC0364291.fas", "r")
f_14 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gam-duebeni/NC0177601.fas", "r")
f_15 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gam-fossarum/NC0349371.fas", "r")
f_16 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gmelinoides-fasciatus/NC0333611.fas", "r")
f_17 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gondogeneia_antarctica/NC0161921.fas", "r")
f_18 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-dominicanus/NC0196541.fas", "r")
f_19 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-goulmimensis/NC0196551.fas", "r")
f_20 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-ilvanus/NC0196561.fas", "r")
f_21 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-longicaudus/NC0196581.fas", "r")
f_22 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-longipes/NC0130321_PCG.fas", "r")
f_23 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-panousei/NC0196591.fas", "r")
f_24 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-remyi/NC0196601.fas", "r")
f_25 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-repens/NC_019653.1.fas", "r")
f_26 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-spinicaudatus/HE8605061.fas", "r")
f_27 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Onisimus-nanseni/NC0138191.fas", "r")
f_28 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pallaseopsis-kessleri/NC0333621.fas", "r")
f_29 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pseudoniphargus-daviui/NC0196622.fas", "r")
f_30 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Sty-indentatus/NC0302611.fas", "r")

outfile = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP25A/Raw_kmer_31/MITOS_rearranged/Exp_Ref_Nad2_r.fasta","w")

genes = ['nad1','nad4','nad4l','nad5','atp6','atp8','cob','cox1','cox2','cox3','nad2','nad3','nad6']

def ParsePCG(f, pcg):
    
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

g_6 = ParsePCG(f_6, genes[10])
outfile.write(g_6)
g_7 = ParsePCG(f_7, genes[10])
outfile.write(g_7)
g_8 = ParsePCG(f_8, genes[10])
outfile.write(g_8)
g_9 = ParsePCG(f_9, genes[10])
outfile.write(g_9)
g_10 = ParsePCG(f_10, genes[10])
outfile.write(g_10)
g_11 = ParsePCG(f_11, genes[10])
outfile.write(g_11)
g_12 = ParsePCG(f_12, genes[10])
outfile.write(g_12)
g_13 = ParsePCG(f_13, genes[10])
outfile.write(g_13)
g_14 = ParsePCG(f_14, genes[10])
outfile.write(g_14)
g_15 = ParsePCG(f_15, genes[10])
outfile.write(g_15)
g_16 = ParsePCG(f_16, genes[10])
outfile.write(g_16)
g_17 = ParsePCG(f_17, genes[10])
outfile.write(g_17)
g_18 = ParsePCG(f_18, genes[10])
outfile.write(g_18)
g_19 = ParsePCG(f_19, genes[10])
outfile.write(g_19)
g_20 = ParsePCG(f_20, genes[10])
outfile.write(g_20)
g_21 = ParsePCG(f_21, genes[10])
outfile.write(g_21)

g_23 = ParsePCG(f_23, genes[10])
outfile.write(g_23)
g_24 = ParsePCG(f_24, genes[10])
outfile.write(g_24)
g_25 = ParsePCG(f_25, genes[10])
outfile.write(g_25)
g_26 = ParsePCG(f_26, genes[10])
outfile.write(g_26)
g_27 = ParsePCG(f_27, genes[10])
outfile.write(g_27)
g_28 = ParsePCG(f_28, genes[10])
outfile.write(g_28)
g_29 = ParsePCG(f_29, genes[10])
outfile.write(g_29)
g_30 = ParsePCG(f_30, genes[10])
outfile.write(g_30)

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
f_14.close()
f_15.close()
f_16.close()
f_17.close()
f_18.close()
f_19.close()
f_20.close()
f_21.close()
f_22.close()
f_23.close()
f_24.close()
f_25.close()
f_26.close()
f_27.close()
f_28.close()
f_29.close()
f_30.close()

outfile.close()



