#! /usr/bin/env python3

import pandas as pd

def fpkm(df,counts,lengths):
    df=df.copy()
    if isinstance(counts,str):
        rate = df[counts] / df[lengths]
        df[counts] =  rate / df[counts].sum() * 1e6
    elif isinstance(counts,list):
        for count in counts:
            rate = df[count] / df[lengths]
            df[count] =  rate / df[count].sum() * 1e6
    else:
        raise TypeError('counts can only be str or list, not '+type(counts))
    return df[counts]

def tpm(df,counts,lengths):
    df=df.copy()
    if isinstance(counts,str):
        rate = df[counts] / df[lengths]
        df[counts] = rate / rate.sum() * 1e6
    elif isinstance(counts,list):
        for count in counts:
            rate = df[count] / df[lengths]
            df[count] = rate / rate.sum() * 1e6
    else:
        raise TypeError('counts can only be str or list, not '+type(counts))
    return df[counts]

def reads_count(df,counts):
    return df[counts]


def featurecounts2others(featurecounts,info,prefix):
    '''

    :param list[str] featurecounts: featurecounts files
    :param str info: sample info file including 'sample\tbam', because featurecounts may specific the sample name as the bam file name
    :param str prefix: output prefix, including prefix_TMP.txt prefix_FPKM.txt prefix_count.txt
    '''
    info_df = pd.read_csv(info,sep='\t',comment='#')
    md=None
    for i in featurecounts:
        if None is md:
            md = pd.read_csv(i,sep='\t',comment='#',index_col=1)
        else:
            md=md.merge(pd.read_csv(i,sep='\t',comment='#',index_col=1),how='inner')

    rename={}
    for i,j in zip(info_df['sample'],info_df['bam']):
        rename[j]=i
    md.rename(rename,axis=1,inplace=True)
    count_value=md[['Geneid','Length']+list(info_df['sample'])]
    count_value.set_index('Geneid',inplace=True)
    fpkm_df = fpkm(count_value,list(info_df['sample']),'Length')
    tpm_df = tpm(count_value,list(info_df['sample']),'Length')
    count_df = reads_count(count_value,list(info_df['sample']))

    fpkm_df.to_csv(prefix+'_FPKM.txt',sep='\t')
    tpm_df.to_csv(prefix+'_TPM.txt',sep='\t')
    count_df.to_csv(prefix+'_COUNT.txt',sep='\t')