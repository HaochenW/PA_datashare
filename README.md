Dataset of yeast promoter
=====================================



## Source papers:

Genome Research: ["Probing the effect of promoters on noise in gene expression using thousands of designed sequences"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4199362/).

Nature Biotechology: ["Inferring gene regulatory logic from high-throughput measurements of thousands of systematically designed promoters"](https://www.nature.com/articles/nbt.2205)

## Files in the folder
- `GSE55346_TableS1_PromotersExpressionValues.txt`: Promoter expression mean and noise from paper ["Probing the effect of promoters on noise in gene expression using thousands of designed sequences"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4199362/).

- `GSM929011_promoter_sequence_and_experiment_replicate_1.txt`: Promoter sequence and expression mean from paper ["Inferring gene regulatory logic from high-throughput measurements of thousands of systematically designed promoters"](https://www.nature.com/articles/nbt.2205)
- `GSM929012_promoter_sequence_and_experiment_replicate_2.txt`: Another replicate experiment from ["Inferring gene regulatory logic from high-throughput measurements of thousands of systematically designed promoters"](https://www.nature.com/articles/nbt.2205)

- `data_deal.py`: Get the final sequence and expression data.

## Outputs
- `all_data.h5`: Include three parts as below:
- sequence: 6500 promoter sequences (150bps)
- GR_exp: The expression mean and noise in the Genome Research paper
- NBT_exp: The expression mean in the Nature biotechology paper
- `GR_exp.csv`: Sequence and expression mean and noise from ["Probing the effect of promoters on noise in gene expression using thousands of designed sequences"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4199362/).
- `NBT_exp.csv`: Sequence and expression mean from ["Inferring gene regulatory logic from high-throughput measurements of thousands of systematically designed promoters"](https://www.nature.com/articles/nbt.2205)

## Load the data
- Load the data by below python script
 
```python
import pandas as pd
store = pd.HDFStore('all_data.h5')
seq = store['sequence']
NBT_exp = store['NBT_exp']
GR_exp = store['GR_exp']
```