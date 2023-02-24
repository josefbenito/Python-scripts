#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Consolidating individual protein coding genes 

outfile = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MAFFT_Alignment/PCG_all_Samples_all_trail4.fasta","w")

genes = ['cox1','cox2','atp8','atp6','cox3','nad3','nad5','nad4','nad4l','nad6','cob','nad1','nad2']

ex = len(genes)

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
            if (c == b-1):
                break
            word = a[c+1].split()
            for i in word:
                if "+;" in i or "-;" in i:
                    print_flag = False
                    break
            if print_flag == False:
                break
    return rec

outfile.write(">MP25A_Stygobromus-pizzinii" + "\n")
for x in range(ex):  
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP25A/Raw_kmer_31/MITOS_rearranged/Contig1.fas", "r")    
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">MP26A_Stygobromus-tenuis" + "\n")    
for x in range(ex):   
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/grabb-master/grabb_results/MP26A/MITOS_rearranged/edena1.fas", "r")  
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">MP28A_Bactrurus-brachycaudus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP28A/Kmer_45/MITOS/Contig1.fas", "r")  
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">MP29A_Gammarus-troglophilus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP29A/Raw_cob_kmer45/MITOS/Contig05b372b288c803b223b204b120b73c648b55c5340355656522.fas", "r")  
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">MP31B_Stygobromus-allegheniensis" + "\n")
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP31B/kmer_31_rev/MITOS/Contig03115680812.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">MP53A_Crangonyx-forbesi" + "\n")  
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/NOVOPlasty-master/NOVOPlasty_results_ASC/MP53A/Kmer_45/MITOS/Contig1.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Bahadzia-jaraguensis" + "\n") 
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Bahadzia-jaraguensis/NC0196611.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Brachyuropus-grewingkii" + "\n") 
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Brachyuropus-grewingkii/NC0263091.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Caprella-mutica" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Caprella-mutica/NC0144921.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
   
outfile.write(">Caprella-scaura" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Caprella-scaura/NC0146871.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
 
outfile.write(">Eulimnogammarus-cyaneus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-cyaneus/NC0333601.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Eulimnogammarus-verrucosus" + "\n")    
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-verrucosus/NC0231041.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Eulimnogammarus-vittatus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eulimnogammarus-vittatus/NC0255641.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Eurythenes-maldoror" + "\n")  
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eurythenes-maldoror/NC0364291.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Gammarus-duebeni" + "\n")    
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gam-duebeni/NC0177601.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Gammarus-fossarum" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gam-fossarum/NC0349371.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Gmelinoides-fasciatus" + "\n")       
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gmelinoides-fasciatus/NC0333611.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Gondogeneia_antarctica" + "\n") 
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Gondogeneia_antarctica/NC0161921.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Metacrangonyx-dominicanus" + "\n") 
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-dominicanus/NC0196541.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Metacrangonyx-goulmimensis" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-goulmimensis/NC0196551.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
 
outfile.write(">Metacrangonyx-ilvanus" + "\n") 
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-ilvanus/NC0196561.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-longicaudus" + "\n")   
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-longicaudus/NC0196581.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Metacrangonyx-longipes" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-longipes/NC0130321_PCG.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Metacrangonyx-panousei" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-panousei/NC0196591.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Metacrangonyx-remyi" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-remyi/NC0196601.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Metacrangonyx-repens" + "\n")  
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-repens/NC_019653.1.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Metacrangonyx-spinicaudatus" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-spinicaudatus/HE8605061.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Onisimus-nanseni" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Onisimus-nanseni/NC0138191.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Pallaseopsis-kessleri" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pallaseopsis-kessleri/NC0333621.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Pseudoniphargus-daviui" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pseudoniphargus-daviui/NC0196622.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Stygobromus-indentatus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Sty-indentatus/NC0302611.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 

outfile.write(">Stygobromus-foliatus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Sty-foliatus/KU8697131.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 
    
outfile.write(">Stygobromus-tenuis-potomacus" + "\n")     
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Sty-tenuis-potomacus/KU8697121.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n") 
    
outfile.write(">Eophreatoicus-sp-14" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Eophreatoicus-sp-14/NC0139761.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
 
outfile.write(">Ligia-oceanica" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Ligia-oceanica/NC0084121.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")

outfile.write(">Limnoria-quadripunctata" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Limnoria-quadripunctata/NC0240541.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Pseudoniphargus-sorbasiensis" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pseudoniphargus-sorbasiensis/LN8711751.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Pseudoniphargus-gorbeanus" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Pseudoniphargus-gorbeanus/LN8711761.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Platorchestia-parapacifica" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Platorchestia-parapacifica/MG0103711.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Platorchestia-japonica" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Platorchestia-japonica/MG0103701.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Parhyale-hawaiiensis" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Parhyale-hawaiiensis/AY6399371.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-sp-5-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-sp-5-MDMBR-2012/HE8604971.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-sp-4-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-sp-4-MDMBR-2012/HE8604981.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-sp-3-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-sp-3-MDMBR-2012/HE8605041.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-sp-2-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-sp-2-MDMBR-2012/HE8605071.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-sp-1-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-sp-1-MDMBR-2012/HE8605131.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Metacrangonyx-samanensis" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Metacrangonyx-samanensis/HE8605051.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Longipodacrangonyx-sp-1-MDMBR-2012" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Longipodacrangonyx-sp-1-MDMBR-2012/HE8604961.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Linevichella-vortex" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Linevichella-vortex_nad2-missing/KX3419671.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Hirondellea-gigas" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Hirondellea-gigas_nad1-nad4-missing/KU5589901.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")  
    
outfile.write(">Garjajewia-cabanisii" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Garjajewia-cabanisii/KX3419651.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Crypturopus-tuberculatus" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Crypturopus-tuberculatus/KX3419631.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
outfile.write(">Acanthogammarus-victorii" + "\n")      
for x in range(ex):    
    f = file("/Users/josefbenito/UAH_Docs/Fall_2017/Niemiller_Lab_Research/MITOS_Reference/Acanthogammarus-victorii/KX3419621.fas", "r")
    g = ParsePCG(f, genes[x])
    h = g.split()
    rec = ""
    rec += "".join(h[4: ])
    outfile.write(rec + "\n")
    
f.close()
outfile.close()
