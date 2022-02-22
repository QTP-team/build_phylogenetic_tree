import math
genome_file = "taxo.txt"
annot_file = "annot.txt"


nodes_dict = {}
for i in open(genome_file):
    item = i.split("\t")
    k,v = item[1].rstrip(".fna"),item[0]
    nodes_dict[k] = v
print("nodes_dict:", len(nodes_dict))


rep_dict = {}
for i in open(genome_file).readlines():
    item = i.split("\t")
    phylum, rep_id = item[2].split(";")[1].lstrip("p__"), item[1].rstrip(".fna")
    rep_dict[rep_id] = [phylum]
print("genome_dict:", len(rep_dict))


f_o = open(annot_file, "w")
global_set = \
"total_plotted_degrees\t335\n\
start_rotation\t90\n\
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
{"Thermoproteota":"#125D98",\
 "Hydrothermarchaeota":"#B6C867",\
"Proteobacteria":"#F5A962"}

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
    nstr_node="%s\tclade_marker_color\t%s\n%s\tclade_marker_size\t10\n" %(nodes_dict[node], node_color[phylum], nodes_dict[node])
    nstr_node += "%s\tannotation_background_color\t%s\n" %(nodes_dict[node], node_color[phylum])
    nstr_node += "%s\tannotation_background_alpha\t0.1\n" %(nodes_dict[node])
    f_o.write(nstr_node)
    
f_o.close()
