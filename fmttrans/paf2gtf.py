#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT License
# @Time    : 8/1/2020 6:18 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : paf2gtf
# @Software: PyCharm

from fmttrans.paf import Paf
from fmttrans.utils import *


def paf2gtf(args):
    '''

    :param args:
    :return:
    '''
    paf_file=args.paf
    gtf_file=args.gtf
    mapped_length_r = args.mapped_length_rate
    mapping_q = args.mapping_quality
    align_ident = args.align_identity
    tag = args.tag


    paf = Paf(paf_file)
    with open(gtf_file, 'w') as fout:
        number = 1
        for pafe in paf:
            if mapped_length_rate(pafe) >= mapped_length_r and \
                    float(pafe.mapping_quality) >= mapping_q and \
                    align_identity(pafe) >= align_ident:
                exons = align2exons(int(pafe.target_start),
                                    int(pafe.target_end),
                                    extract_cg_value(pafe.sam_tag['cg'].value),
                                    pafe.strand)
                transcript_attri = ['gene_id "{}.{}";'.format(tag.upper(), str(number)),
                                    'trascript_id "{}.{}";'.format(tag.upper(), str(number)),
                                    'total_exon_number "{}";'.format(len(exons))]
                transcript = [pafe.target_name,
                              tag,
                              'trascript',
                              pafe.target_start,
                              pafe.target_end,
                              pafe.mapping_quality,
                              pafe.strand,
                              '.',
                              ' '.join(transcript_attri)]
                fout.write('\t'.join(transcript)+'\n')
                for i, exon in enumerate(exons):
                    exon_attri = ['gene_id "{}.{}";'.format(tag.upper(), str(number)),
                                  'trascript_id "{}.{}";'.format(tag.upper(), str(number)),
                                  'total_exon_number "{}";'.format(len(exons)),
                                  'exon_number "{}";'.format(str(i+1))]
                    exon_out= [pafe.target_name,
                               tag,
                               'exon',
                               str(exon[0]),
                               str(exon[1]),
                               pafe.mapping_quality,
                               pafe.strand,
                               '.',
                               ' '.join(exon_attri)]
                    fout.write('\t'.join(exon_out)+'\n')
                number +=1

    return True
