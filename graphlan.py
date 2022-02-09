import math
sgb_file = "all_18607.txt"
annot_file = "annot.txt"


nodes_dict = {}
for i in open(sgb_file):
    item = i.split("\t")
    k,v = item[1].rstrip(".fa"),item[0]
    nodes_dict[k] = v
print("nodes_dict:", len(nodes_dict))


rep_dict = {}
for i in open(sgb_file).readlines():
    item = i.split("\t")
    phylum, known, Ass, Horse,Antelope,Sheep,Yak,Cattle,MAG,rep_id = item[2], item[3],item[4],item[5], item[6],item[7],item[8], item[9],item[10].rstrip("\n"), item[1].rstrip(".fa")
    rep_dict[rep_id] = [phylum,known,Ass,Horse,Antelope,Sheep,Yak,Cattle,MAG]
print("sgb_dict:", len(rep_dict))


f_o = open(annot_file, "w")
global_set = \
"total_plotted_degrees\t335\n\
start_rotation\t90\n\
ring_label\t1\tUnknownness\n\
ring_label\t2\tTA\n\
ring_label\t3\tTH\n\
ring_label\t4\tTAN\n\
ring_label\t5\tTS\n\
ring_label\t6\tYak\n\
ring_label\t7\tTC\n\
ring_label\t8\tGenomes\n\
ring_label_font_size\t1\t4\n\
ring_label_font_size\t2\t4\n\
ring_label_font_size\t3\t4\n\
ring_label_font_size\t4\t4\n\
ring_label_font_size\t5\t4\n\
ring_label_font_size\t6\t4\n\
ring_label_font_size\t7\t4\n\
ring_label_font_size\t8\t4\n\
ring_height\t1\t0.5\n\
ring_height\t2\t0.5\n\
ring_height\t3\t0.5\n\
ring_height\t4\t0.5\n\
ring_height\t5\t0.5\n\
ring_height\t6\t0.5\n\
ring_height\t7\t0.5\n\
ring_color\t8\t#000000\n\
ring_internal_separator_thickness\t1\t0.5\n\
ring_internal_separator_thickness\t2\t1\n\
ring_internal_separator_thickness\t3\t1\n\
ring_internal_separator_thickness\t4\t1\n\
ring_internal_separator_thickness\t5\t1\n\
ring_internal_separator_thickness\t6\t1\n\
ring_internal_separator_thickness\t7\t1\n\
ring_internal_separator_thickness\t8\t1\n\
ring_separator_color\t1\t#FFFFFF\n\
ring_separator_color\t2\t#FFFFFF\n\
ring_separator_color\t3\t#FFFFFF\n\
ring_separator_color\t4\t#FFFFFF\n\
ring_separator_color\t5\t#FFFFFF\n\
ring_separator_color\t6\t#FFFFFF\n\
ring_separator_color\t7\t#FFFFFF\n\
ring_separator_color\t8\t#FFFFFF\n\
class_legend_font_size\t5\n\
annotation_legend_font_size\t5\n\
clade_separation\t0.5\n\
clade_marker_shape\t.\n\
clade_marker_size\t0\n\
branch_thickness\t0.2\n\
clade_marker_edge_width\t0\n"
f_o.write(global_set)


#node_color
node_color = \
{"Actinobacteriota":"#125D98",\
 "Bacteroidota":"#B6C867",\
"Cyanobacteria":"#F5A962",\
"Elusimicrobiota":"#343A40",\
"Fibrobacterota":"#7952B3",\
 "Firmicutes":"#FFC107",\
 "Firmicutes_A":"#8AB6D6",\
 "Firmicutes_B":"#CCFFBD",\
 "Firmicutes_C":"#01937C",\
"Halobacteriota":"#D83A56",\
 "Methanobacteriota":"#68B0AB",\
 "Proteobacteria":"#C84B31",\
 "Spirochaetota":"#52006A",\
"Thermoplasmatota":"#00ff7f",\
 "Verrucomicrobiota_A":"#890596",\
 "Others":"#808080"}

# legend
for k,v in node_color.items():
    nstr_l = "%s\tannotation\t%s\n" %(k, k)
    nstr_l += "%s\tclade_marker_color\t%s\n" %(k, v)
    nstr_l += "%s\tclade_marker_size\t1\n" %(k)
    f_o.write(nstr_l)

for node in nodes_dict.keys():
    phylum = rep_dict[node][0]
    if phylum in node_color.keys():
        pass
    else:
        phylum = "Others"
    nstr_node="%s\tclade_marker_color\t%s\n%s\tclade_marker_size\t1\n" %(nodes_dict[node], node_color[phylum], nodes_dict[node])
    f_o.write(nstr_node)
    
#ring 1 known
r1_color = {"known":"#006000","unknown":"#FFA500"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][1]
    nstr_r1 = "%s\tring_color\t1\t%s\n" %(nodes_dict[node], r1_color[mtype])
    f_o.write(nstr_r1)


#ring 2 Host_Ass
r2_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][2]
    if mtype=="Tibetan_Ass":
        nstr_r2 = "%s\tring_color\t2\t%s\n" %(nodes_dict[node], r2_color[mtype])
    else:
        nstr_r2 = "%s\tring_color\t2\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r2)

#ring 4 Host_Horse
r3_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][3]
    if mtype=="Tibetan_Horse":
        nstr_r3 = "%s\tring_color\t3\t%s\n" %(nodes_dict[node], r3_color[mtype])
    else:
        nstr_r3 = "%s\tring_color\t3\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r3)

#ring 4 Host_Antelope
r4_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][4]
    if mtype=="Tibetan_Antelope":
        nstr_r4 = "%s\tring_color\t4\t%s\n" %(nodes_dict[node], r4_color[mtype])
    else:
        nstr_r4 = "%s\tring_color\t4\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r4)

#ring 5 Host_Sheep
r5_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][5]
    if mtype=="Tibetan_Sheep":
        nstr_r5 = "%s\tring_color\t5\t%s\n" %(nodes_dict[node], r5_color[mtype])
    else:
        nstr_r5 = "%s\tring_color\t5\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r5)

#ring 6 Host_Yak
r6_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][6]
    if mtype=="Tibetan_Yak":
        nstr_r6 = "%s\tring_color\t6\t%s\n" %(nodes_dict[node], r6_color[mtype])
    else:
        nstr_r6 = "%s\tring_color\t6\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r6)
    
#ring 7 Host_Cattle
r7_color = {"Tibetan_Ass":"#DC143B", "Tibetan_Horse":"#FF99FF","Tibetan_Antelope":"#0000CD","Tibetan_Cattle":"#00FF00","Tibetan_Yak":"#336600","Tibetan_Sheep":"#33FFCC"}
for node in nodes_dict.keys():
    mtype = rep_dict[node][7]
    if mtype=="Tibetan_Cattle":
        nstr_r7 = "%s\tring_color\t7\t%s\n" %(nodes_dict[node], r7_color[mtype])
    else:
        nstr_r7 = "%s\tring_color\t7\t%s\n" %(nodes_dict[node], "#FFFFFF")
    f_o.write(nstr_r7)

#ring 8 genomes
for node in nodes_dict.keys():
    size = math.log10(float(rep_dict[node][8]))
    nstr_r8 = "%s\tring_height\t8\t%.4f\n" %(nodes_dict[node], size)
    f_o.write(nstr_r8)
f_o.close()
