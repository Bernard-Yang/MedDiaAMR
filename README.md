# MedDiaAMR



Code for the paper "Improving medical dialogue generation with abstract meaning representations" 

### Dataset
```
├── resources/med-dialog
   └── large-english-dialog-corpus		# the raw dialogue corpus
          └── `train.source.txt`    
          └── `train.target.txt`       
          └── `val.source.txt` 
          └── `val.target.txt` 
          └── `test.source.txt` 
          └── `test.target.txt` 
    └── med_term_list.txt		# the terminology list
```
    
### Training commands
```
python Training.py --datasets [dd, personachat]
```
### Evaluation commands
```
python Evaluation.py --datasets [dd, personachat]
```

### Citation
If you found this repository or paper is helpful to you, please cite our paper.
```
@misc{yang2023improving,
      title={Improving Medical Dialogue Generation with Abstract Meaning Representations}, 
      author={Bohao Yang and Chen Tang and Chenghua Lin},
      year={2023},
      eprint={2309.10608},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
