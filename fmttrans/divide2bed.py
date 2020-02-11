#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) Aegicare License
# @Time    : 2020/2/10 2:18 PM
# @Author  : YUELONG.CHEN
# @Mail    : yuelong.chen.btr@gmail.com
# @File    : divide2bed
# @Software: PyCharm

from fmttrans.pattern import gtf_transcript_pattern
from fmttrans.utils import write_file, log


def divide2bed(args):
    tracking = '{}.tracking'.format(args.gffcompare_prefix)
    transcript_dict = {}
    transcript_dict.setdefault('consistent', {})
    transcript_dict['consistent'].setdefault('known', [])
    transcript_dict['consistent'].setdefault('known_gene', [])
    transcript_dict.setdefault('inconsistent', {})
    transcript_dict['inconsistent'].setdefault('novel', [])
    transcript_dict['inconsistent'].setdefault('novel_gene', [])
    transcript_dict['inconsistent'].setdefault('known', [])
    transcript_dict['inconsistent'].setdefault('known_gene', [])

    with open(tracking, 'r') as tkf:
        line = tkf.readline()
        tracking_n = 0
        while line:
            tracking_n += 1
            if tracking_n % 10000 == 0:
                log.info('Reading {} lines in tracking file'.format(str(tracking_n)))
            if line.startswith('#'):
                line = tkf.readline()
                continue
            cells = line.strip('\n').split('\t')
            if '|' in cells[2]:
                gene, known_tsp = cells[2].split('|')
                if gene not in args.gene_list:
                    line = tkf.readline()
                    continue
            else:
                line = tkf.readline()
                continue
                known_tsp = ''
            _, novel_tsp, *_ = cells[4].split('|')
            if cells[3] == '=':

                if known_tsp not in transcript_dict['consistent']['known']:
                    transcript_dict['consistent']['known'].append(known_tsp)
                    transcript_dict['consistent']['known_gene'].append(gene)
            else:

                if novel_tsp not in transcript_dict['inconsistent']['novel']:
                    transcript_dict['inconsistent']['novel'].append(novel_tsp)
                    transcript_dict['inconsistent']['novel_gene'].append(gene)
                if known_tsp not in transcript_dict['consistent']['known']:
                    transcript_dict['inconsistent']['known'].append(known_tsp)
                    transcript_dict['inconsistent']['known_gene'].append(gene)
            line = tkf.readline()

    consistent_output = '{}.consistent.bed'.format(args.prefix)
    inconsistent_output = '{}.inconsistent.bed'.format(args.prefix)
    consistent_bed = []
    inconsistent_bed = []
    with open(args.annotate_gtf, 'r') as ag:
        annogtf_n = 0
        line = ag.readline()
        while line:
            annogtf_n += 1
            if annogtf_n % 10000 == 0:
                log.info('Reading {} lines in annotate gtf file'.format(str(annogtf_n)))
            cells = line.strip().split('\t')
            if not line.startswith('#') and cells[2] == 'transcript':
                tsp = gtf_transcript_pattern.findall(line)[0]
                if tsp in transcript_dict['inconsistent']['known']:
                    inconsistent_bed.append([
                        cells[0],
                        cells[3],
                        cells[4],
                        transcript_dict['inconsistent']['known_gene'][
                            transcript_dict['inconsistent']['known'].index(tsp)]
                    ])
                if tsp in transcript_dict['consistent']['known']:
                    consistent_bed.append([
                        cells[0],
                        cells[3],
                        cells[4],
                        transcript_dict['consistent']['known_gene'][
                            transcript_dict['consistent']['known'].index(tsp)]
                    ])
            line = ag.readline()

    with open(args.test_gtf, 'r') as tg:
        testgtf_n = 0

        line = tg.readline()
        while line:
            testgtf_n += 1
            if testgtf_n % 10000 == 0:
                log.info('Reading {} lines in test gtf file'.format(str(testgtf_n)))
            cells = line.strip().split('\t')
            if not line.startswith('#') and cells[2] == 'transcript':
                tsp = gtf_transcript_pattern.findall(line)[0]
                if tsp in transcript_dict['inconsistent']['novel'].append(known_tsp):
                    inconsistent_bed.append([
                        cells[0],
                        cells[3],
                        cells[4],
                        transcript_dict['inconsistent']['novel_gene'][
                            transcript_dict['inconsistent']['novel'].index(tsp)]
                    ])
            line = tg.readline()

    log.info('Write consistent bed')
    write_file(consistent_output, consistent_bed)
    log.info('Write inconsistent bed')
    write_file(inconsistent_output, inconsistent_bed)
