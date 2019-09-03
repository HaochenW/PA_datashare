# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:26:54 2019

@author: wangpeng884112
"""

import pandas as pd
import matplotlib.pyplot as plt

# Get the data from files
GR_table = pd.read_table('GSE55346_TableS1_PromotersExpressionValues.txt')
NBT_table1 = pd.read_table('GSM929011_promoter_sequence_and_experiment_replicate_1.txt')
NBT_table2 = pd.read_table('GSM929012_promoter_sequence_and_experiment_replicate_2.txt')


# Get the sequence and expression data
seq = pd.DataFrame(NBT_table1['Sequence'])
GR_exp = GR_table[[ 'LibID','Replicate1_ExpressionMean','Replicate2_ExpressionMean',
 'Replicate1_ExpressionNoise','Replicate2_ExpressionNoise']]
NBT_exp = pd.concat([NBT_table1[['LibraryID',' Expression Replicate1']],NBT_table2[' Expression Replicate2']],axis=1)

# Draw the scatter plot of the expression data
# 1. The scatter plot between NBT expression and GR expression
plt.scatter(NBT_exp[' Expression Replicate1'],GR_exp['Replicate1_ExpressionMean'])
plt.xlabel(' Expression Replicate1_NBT')
plt.ylabel('Replicate1_ExpressionMean_GR')
plt.figure()
plt.scatter(NBT_exp[' Expression Replicate2'],GR_exp['Replicate2_ExpressionMean'])
plt.xlabel(' Expression Replicate2_NBT')
plt.ylabel('Replicate2_ExpressionMean_GR')
# 2. The scatter plot in the NBT_expression and GR expression
plt.figure()
NBT_exp.plot.scatter(x = ' Expression Replicate1', y = ' Expression Replicate2')
plt.figure()
GR_exp.plot.scatter(x = 'Replicate1_ExpressionMean', y = 'Replicate2_ExpressionMean')


# Print the pearson and spearman correlation of expression between NBT papers and GR papers
pearson_1 = NBT_exp[' Expression Replicate1'].corr(GR_exp['Replicate1_ExpressionMean'],method="pearson")
pearson_2 = NBT_exp[' Expression Replicate2'].corr(GR_exp['Replicate2_ExpressionMean'],method="pearson")
spearman_1 = NBT_exp[' Expression Replicate1'].corr(GR_exp['Replicate1_ExpressionMean'],method="spearman")
spearman_2 = NBT_exp[' Expression Replicate2'].corr(GR_exp['Replicate2_ExpressionMean'],method="spearman")

print('Pearson correlation of Replicate1: {exp}'.format(exp = pearson_1))
print('Pearson correlation of Replicate2: {exp}'.format(exp = pearson_2))
print('Spearman correlation of Replicate1: {exp}'.format(exp = spearman_1))
print('Spearman correlation of Replicate2: {exp}'.format(exp = spearman_2))

# Store the data in hdf5 file.
h5 = pd.HDFStore('all_data.h5','w')
h5['sequence'] = seq
h5['GR_exp'] = GR_exp
h5['NBT_exp'] = NBT_exp
h5.close()



