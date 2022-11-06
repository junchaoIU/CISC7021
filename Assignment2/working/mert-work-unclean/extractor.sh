#!/usr/bin/env bash
cd /home/wujunchao/mosesdecoder/corpus/working/mert-work
/home/wujunchao/mosesdecoder/bin/extractor --sctype BLEU --scconfig case:true  --scfile run11.scores.dat --ffile run11.features.dat -r /home/wujunchao/mosesdecoder/corpus/true_dev.en -n run11.best100.out.gz
