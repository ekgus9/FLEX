
shot=0
task=flex

python lm_eval \
    --model hf \
    --model_args pretrained=meta-llama/Llama-2-7b-hf \
    --tasks $task \
    --device cuda:0 \
    --batch_size 4 \
    --output_path ./output/llama2/$task/ \
    --seed 42 \
    --log_samples \
    --num_fewshot 0