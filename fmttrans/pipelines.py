#! /usr/bin/env python3

import defopt

from fmttrans.rna import featurecounts2others
def fc2o():
    defopt.run(featurecounts2others)

if __name__=='__main__':
    fc2o()