# build_phylogenetic_tree
## 1 Introduction

Use phylophlan to build a phylogenetic tree and then visualize it using graphlan.

## 2 Usage
### 2.1 Use conda to install related dependencies
```
conda env create -n build_phylogenetic_tree -f env.yaml
conda activate build_phylogenetic_tree
```

### 2.2 Gtdbtk
```
gtdbtk classify_wf --genome_dir 0.genome --out_dir gtdbtk/result --cpus 8 --extension fa
```

### 2.3 Integrated protein file
```
cp result/identify/intermediate_results/marker_genes/*/*.faa 1.protein
```

### 2.4 Generate the configuration file custom_config_nt.cfg
```
python phylophlan_write_config_file.py \
    -o custom_config_nt.cfg \
    -d a \
    --db_aa diamond \
    --map_aa diamond \
    --msa muscle \
    --trim trimal \
    --tree1 fasttree
```

### 2.5 phylophlan
```
phylophlan -i 1.protein \
-d phylophlan \
-f custom_config_nt.cfg \
--diversity high \
--fast \
-o output \
--nproc 4 \
--verbose 2>&1 | tee logs/phylophlan.log
```

### 2.6 graphlan
```
python graphlan.py
/ldfssz1/ST_META/P19Z10200N0314_LXP/2.feng_project/graphlan/graphlan/graphlan_annotate.py --annot annot.txt all_sgb_18607.tree all_sgb_18607.xml
/ldfssz1/ST_META/P19Z10200N0314_LXP/2.feng_project/graphlan/graphlan/graphlan.py --dpi 360 --size 3.5 all_sgb_18607.xml all_sgb_18607.pdf
```