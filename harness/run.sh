
python lm_eval \
    --model hf \
    --model_args pretrained=distilgpt2 \
    --tasks bbq_none,bbq_easy,bbq_hard \
    --device cuda:0 \
    --batch_size 1 \
    --output_path ./output/ \
    --cache_requests "refresh" \
    --seed 42 \
    --verbosity DEBUG

# meta-llama/Llama-2-7b-chat-hf
# meta-llama/Meta-Llama-3-8B-Instruct
# distilgpt2
# upstage/SOLAR-10.7B-Instruct-v1.0
