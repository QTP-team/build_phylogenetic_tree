# build_phylogenetic_tree
## 1 Introduction

Use phylophlan to build a phylogenetic tree and then visualize it using graphlan.

## 2 Usage
### 2.1 Use conda to install related dependencies
```
conda env create -n build_phylogenetic_tree -f env.yaml
conda activate build_phylogenetic_tree
```

### 2.2 gtdbtk
Large memory(~1T) is required when using gtdbtk.
```
gtdbtk classify_wf --genome_dir 0.genome --out_dir 1.gtdbtk/result --cpus 4 --extension gz
```

### 2.3 Integrated protein file and classify file
```
cp 1.gtdbtk/result/identify/intermediate_results/marker_genes/*/*.faa 2.phylophlan/01.protein
awk '{print $1"\t"$2}' 1.gtdbtk/result/gtdbtk.ar122.summary.tsv | sed '1d' > 3.graphlan/gtdbtk.ar122.summary.tsv
awk '{print $1"\t"$2}' 1.gtdbtk/result/gtdbtk.bac120.summary.tsv | sed '1d' > 3.graphlan/gtdbtk.bac120.summary.tsv
cat 3.graphlan/gtdbtk.ar122.summary.tsv 3.graphlan/gtdbtk.bac120.summary.tsv > 3.graphlan/taxo.txt
```

### 2.4 Generate the configuration file custom_config_nt.cfg
```
python phylophlan_write_config_file.py \
    -o 2.phylophlan/custom_config_nt.cfg \
    -d a \
    --db_aa diamond \
    --map_aa diamond \
    --msa muscle \
    --trim trimal \
    --tree1 fasttree
```

### 2.5 phylophlan
```
phylophlan -i 2.phylophlan/01.protein \
	-d phylophlan \
	-f 2.phylophlan/custom_config_nt.cfg \
	--diversity high \
	--fast \
	-o 2.phylophlan/output \
	--nproc 4 \
	--verbose 2>&1 | tee 2.phylophlan/logs/phylophlan.log
```

### 2.6 graphlan

```
python 3.graphlan/graphlan.py
/ldfssz1/ST_META/P19Z10200N0314_LXP/2.feng_project/graphlan/graphlan/graphlan_annotate.py --annot 3.graphlan/annot.txt 2.phylophlan/output/01.protein.tre tree.xml
/ldfssz1/ST_META/P19Z10200N0314_LXP/2.feng_project/graphlan/graphlan/graphlan.py --size 3.5 tree.xml tree.pdf
```