export DATA_DIR=../data/dataset/lrec/
export BERT_BASE_DIR=/Users/admin/Documents/data/chinese_L-12_H-768_A-12

python cn_punctor.py \
 --task_name Punctor \
 --do_train True \
 --data_dir $DATA_DIR/ \
 --vocab_file $BERT_BASE_DIR/vocab.txt \
 --bert_config_file $BERT_BASE_DIR/bert_config.json \
 --init_checkpoint $BERT_BASE_DIR/bert_model.ckpt \
 --max_seq_length 199 \
 --output_dir ../data/output_pd
