#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Consolidating all files final

f_1 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_MP25A_Alignment.fasta", "r")
f_2 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_MP26A_Alignment.fasta", "r")
f_3 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_MP28A_Alignment.fasta", "r")
f_4 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_MP31B_Alignment.fasta", "r")
f_5 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_MP53A_Alignment.fasta", "r")
f_6 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Bahadzia-jaraguensis_Alignment.fasta", "r")
f_7 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Brachyuropus-grewingkii_Alignment.fasta", "r")
f_8 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Caprella-mutica_Alignment.fasta", "r")
f_9 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Caprella-scaura_Alignment.fasta", "r")
f_10 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Eulimnogammarus-cyaneus_Alignment.fasta", "r")
f_11 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Eulimnogammarus-verrucosus_Alignment.fasta", "r")
f_12 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Eulimnogammarus-vittatus_Alignment.fasta", "r")
f_13 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Eurythenes-maldoror_Alignment.fasta", "r")
f_14 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Gammarus-duebeni_Alignment.fasta", "r")
f_15 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Gammarus-fossarum_Alignment.fasta", "r")
f_16 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Gmelinoides-fasciatus_Alignment.fasta", "r")
f_17 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Gondogeneia_antarctica_Alignment.fasta", "r")
f_18 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-dominicanus_Alignment.fasta", "r")
f_19 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-goulmimensis_Alignment.fasta", "r")
f_20 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-ilvanus_Alignment.fasta", "r")
f_21 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-longicaudus_Alignment.fasta", "r")
f_22 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-longipes_Alignment.fasta", "r")
f_23 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-panousei_Alignment.fasta", "r")
f_24 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-remyi_Alignment.fasta", "r")
f_25 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-repens_Alignment.fasta", "r")
f_26 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Metacrangonyx-spinicaudatus_Alignment.fasta", "r")
f_27 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Onisimus-nanseni_Alignment.fasta", "r")
f_28 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Pallaseopsis-kessleri_Alignment.fasta", "r")
f_29 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Pseudoniphargus-daviui_Alignment.fasta", "r")
f_30 = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Stygobromus-indentatus_Alignment.fasta", "r")

outfile = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/Exp_Ref_Final_Alignment.fasta","w")

samples = ['>MP25A;', '>MP26A;', '>MP28A;', '>MP31B;', '>MP53A;', '>NC_0196611;', '>NC_0263091;', '>NC_0144921;', '>NC_0146871;', '>NC_0333601;',\
           '>NC_0231041;', '>NC_0255641;', '>NC_0364291;', '>NC_0177601;', '>NC_0349371;', '>NC_0333611;', '>NC_0161921;', '>NC_0196541;', '>NC_0196551;',\
           '>NC_0196561;', '>NC_0196581;', '>NC_0130321;', '>NC_0196591;', '>NC_0196601;', '>NC_019653;', '>HE8605061;', '>NC_0138191;', '>NC_0333621;',\
           '>NC_0196622;', '>NC_0302611;']

def FinalPCG(f, pcg):
    
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

g_2 = FinalPCG(f_1, samples[0])


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



