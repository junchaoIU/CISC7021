#!/bin/bash
#SBATCH --job-name              E_task
#SBATCH --partition             gpu-normal
#SBATCH --nodes                 1
#SBATCH --tasks-per-node        1
#SBATCH --time                  40:00:00
#SBATCH --mem                   40G
#SBATCH --gres                  gpu:1
#SBATCH --output                E_task.out
#SBATCH --error                 E_task.err
#SBATCH --mail-type		ALL
#SBATCH --mail-user		MC25653@um.edu.mo

source /etc/profile
source /etc/profile.d/modules.sh

#Adding modules
module add cuda/9.2.148
module add amber/18/gcc/4.8.5/cuda/9

ulimit -s unlimited

#Your program starts here 

# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH: /share/apps/gcc/8.5.0/lib64/

echo $CUDA_VISIBLE_DEVICES
pmemd.cuda -O -i md2.in -o md2.out -p Pt-ADD4_solv.prmtop  -c md1.rst -r md2.rst  -x md2.mdcrd


# python general_distill.py --pregenerated_data /data/home/mc25653/Pretrained-Language-Model/TinyBERT_p/output/output --teacher_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_p/bert-base-cased --student_model student_model_config --do_lower_case --train_batch_size 16 --output_dir general_student_model_without_E

# python task_distill.py --teacher_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_p/ours/CoLA_finetuned_Bert_base_model --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/general_student_model_without_E_final --data_dir CoLA --task_name CoLA --output_dir tinybert_without_E --max_seq_length 64 --train_batch_size 32 --num_train_epochs 50 --aug_train --do_lower_case  

# python task_distill.py --pred_distill --teacher_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_p/ours/CoLA_finetuned_Bert_base_model --student_model tinybert_without_E --data_dir CoLA --task_name CoLA --output_dir tinybert_without_E2 --aug_train --do_lower_case --learning_rate 3e-5 --num_train_epochs  50 --eval_step 100 --max_seq_length 64 --train_batch_size 32

python task_distill.py --do_eval --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/tinybert_without_E2 --task_name CoLA --output_dir /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/eval_E_output --do_lower_case --eval_batch_size 32 --max_seq_length 64 --data_dir CoLA

python task_distill.py --do_eval --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/tinybert_without_E2 --task_name CoLA --output_dir /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/eval_E_output --do_lower_case --eval_batch_size 32 --max_seq_length 64 --data_dir CoLA

python task_distill.py --do_eval --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/tinybert_without_E2 --task_name CoLA --output_dir /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/eval_E_output --do_lower_case --eval_batch_size 32 --max_seq_length 64 --data_dir CoLA

python task_distill.py --do_eval --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/tinybert_without_E2 --task_name CoLA --output_dir /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/eval_E_output --do_lower_case --eval_batch_size 32 --max_seq_length 64 --data_dir CoLA

python task_distill.py --do_eval --student_model /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/tinybert_without_E2 --task_name CoLA --output_dir /data/home/mc25653/Pretrained-Language-Model/TinyBERT_E/eval_E_output --do_lower_case --eval_batch_size 32 --max_seq_length 64 --data_dir CoLA