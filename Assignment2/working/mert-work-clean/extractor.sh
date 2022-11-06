#!/usr/bin/env bash
cd /home/wujunchao/mosesdecoder/corpus/working/mert-work
/home/wujunchao/mosesdecoder/bin/extractor --sctype BLEU --scconfig case:true  --scfile run17.scores.dat --ffile run17.features.dat -r /home/wujunchao/mosesdecoder/corpus/clean_dev.en -n run17.best100.out.gz
