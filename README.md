# MedDiaAMR



Code for the paper "[Improving medical dialogue generation with abstract meaning representations]([url])" 

### Dataset and Resources
The dataset is from [https://github.com/tangg555/meddialog]([url])

The structure of raw dataset should be like this:
```
├── dataset
       └── `train.source.txt`    
       └── `train.target.txt`       
       └── `val.source.txt` 
       └── `val.target.txt` 
       └── `test.source.txt` 
       └── `test.target.txt` 
```
To get the AMR graph (.concept and .path files) of each sentence, you can follow the preprocess in [https://github.com/Soistesimmer/AMR-multiview]([url])

The structure of final dataset should be like this:
```
├── dataset
       └── `train.source.txt`
       └── `train.source.concept`
       └── `train.source.path`
       └── `train.target.txt`       
       └── `val.source.txt`
       └── `val.source.concept`
       └── `val.source.path`
       └── `val.target.txt` 
       └── `test.source.txt`
       └── `test.source.concept`
       └── `test.source.path`
       └── `test.target.txt` 
```
### Preprocessing commands
```
bash preprocess.sh
```
### Training commands
```
bash run-dual.sh
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
