#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2020/3/16 11:12 AM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : featurecounts
# @Software: PyCharm

import pandas as pd
import os


def featurecounts_rename(df, sep='.'):
    '''

    :param featurecounts:
    :param sep:
    :return:
    '''
    rename = {}
    df.drop_duplicates(inplace=True)
    for i in df.columns[df.columns.str.endswith(('.bam', '.sam'))]:
        rename[i] = os.path.basename(i).split(sep)[0]
    return df.rename(columns=rename), rename.values()


def r_featurecounts2expressionset(featurecounts_file, info_file, output, sep='\t',
                                  name_sep='.',
                                  rscript='/bin/env Rscript'):
    '''

    :param featurecounts_file:
    :param info_file:
    :param output:
    :param sep:
    :param name_sep:
    :param rscript:
    :return:
    '''
    df = pd.read_csv(featurecounts_file, sep=sep, comment='#')
    rename_fc, sample_names = featurecounts_rename(df, name_sep)
    rename_fc_file = featurecounts_file + '.rename.tsv'
    rename_fc.to_csv(rename_fc_file, sep=sep, index=False)

    r_script = r'''
#! {rscript}

library(Biobase)
file_in = read.csv('{featurecounts_file}',quote="",row.names=1,header=TRUE,sep='\t')
gene_samples = file_in[c({sample_names})]
exp_array=as.matrix(gene_samples)

info_demo=read.csv('{info_file}',quote='',row.names=1)
info_array=info_demo[c({sample_names}),]

all(rownames(info_array)==colnames(exp_array))
colnames(info_array)

metadata <- data.frame(labelDescription=colnames(info_array),
                       row.names=colnames(info_array))

phenoData <- new("AnnotatedDataFrame",
                 data=info_array, varMetadata=metadata)
dataSet <- ExpressionSet(assayData=exp_array,
                            phenoData=phenoData)
saveRDS(dataSet, file = "{output}")
    '''.format(
        featurecounts_file=featurecounts_file + '.rename.tsv',
        output=output,
        sample_names=','.join(["'{i}'".format(i=i) for i in sample_names]),
        info_file=info_file,
        rscript=rscript
    )
    return r_script


def main():
    pass


if __name__ == '__main__':
    main()
