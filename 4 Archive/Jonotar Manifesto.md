---
tags:
  - inbox
type: Idea
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 


### Thoughts on 2013
1. 


- new political party with the ideology of fixing the system
- reform and strengthening of our civil and political Institutions: credibly free judiciary, credible system of free election (likely a caretaker govt)
- ensuring valid political opposition and respect of opposition speech (even if it is from BAL)

- putting economic strengthening right after strengthening the Institutions

- getting a meritocratic board of advisors for the new government and put all focus on the points above (assuming we get there)


## References
1. Rubayet bhai's post: https://www.facebook.com/rubayat.khan/posts/pfbid0CGG4Q1KVSQP9T7CpcUjvUMFw5rzzE1oKDCnmjQc4ujGYjtFCQxBJXJVTpsu5icQZl?comment_id=1165502584714491&reply_comment_id=1006219990967192&notif_id=1722692370364473&notif_t=comment_mention&ref=notif
2. books: https://drive.google.com/drive/folders/12eX--99lupTeZka2_-xssm1p06-HCAy5?fbclid=IwZXh0bgNhZW0CMTEAAR3DqHRcQ7uqxVNPKqalPVnuFMEBw_8GFGBubK4p3F4CpEk8jJvPFO1KwT8_aem_CXT5etGRGi_XD1LxP9sccQ


BNP Jamat
https://www.facebook.com/100006429341653/posts/4620635324827400/?rdid=C4yIsMeVK3PqaIRF



Nazrul 

Teachers:
Tanzim Uddin
Anu Muhammad

Nurul Haque Nur -- GOP -- Populist with no clue (no good option)

Gono Shokti came out of this--BSW (germany)--not my cup of tea acording yo meem
Gono Shonghoti -- (with likely merge) Zunayed Saki 
Nahid -- econ left, socailly conservative, liaison Zunayed Saki 


National demiocrartic movement (NDM) -- bobby hazzaz (musas kid), Rashna Imam on negotiation table 

Taz -- next AL (not a good option now)

Jatiya Party -- Andalib

Interim: army, lawyers, business people, teachers (easier)

### Data Collection / Saimum
1. students will go do data collecting
2. might need funding
3. law reform of telecom
4. Shoib is Nahid's fried 

=====
Interim Govt
- Tanzim Uddin Khan (DU)
- Bobby Hazzaz, Zunayed Saki 



2yrs
reach out to teachers

if shorter
reach out to polticial parties


python benchmark_throughput.py --model meta-llama/Meta-Llama-3.1-8B-Instruct --gpu-memory-utilization 0.98 -tp 1 --input-len 128 --output-len 128 --kv-cache-dtype fp8_e4m3 --max-model-len 2048 --enforce-eager


python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.95 -tp 1 --input-len 128 --output-len 128 --max-model-len 2048 --enforce-eager


CUDA_VISIBLE_DEVICES=0,1 python benchmark_throughput.py --model meta-llama/Meta-Llama-3.1-8B-Instruct --gpu-memory-utilization 0.96 -tp 2 --input-len 512 --output-len 512 --max-model-len 2048  --enforce-eager


CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 -tp 1 --input-len 512 --output-len 512 --max-model-len 4096  --enforce-eager --quantization compressed-tensors

CUDA_VISIBLE_DEVICES=0,1 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-70B-Instruct-quantized.w4a16 --gpu-memory-utilization 0.96 -tp 2 --input-len 512 --output-len 512 --max-model-len 2048  --enforce-eager

 --kv-cache-dtype fp8 


pip install -U "huggingface_hub[cli]"

huggingface-cli login --token [REDACTED] --add-to-git-credential



Date: Nov 1, 2024


VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --quantization compressed-tensors  --kv-cache-dtype fp8 --enable-chunked-prefill --max_num_batched_tokens 1024 --block-size 16


CUDA_VISIBLE_DEVICES=0,1 python benchmark_throughput.py --model meta-llama/Meta-Llama-3.1-8B-Instruct --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --enable-chunked-prefill --max_num_batched_tokens 1024 --block-size 16


CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model iqbalamo93/Meta-Llama-3.1-8B-Instruct-GPTQ-Q_8 --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --enable-chunked-prefill --max_num_batched_tokens 1024 --block-size 16  --quantization gptq_marlin 

BEST

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 1024 --block-size 16


VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --input-len 512 --output-len 512 --max-model-len 1024  --enforce-eager --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 4096 --block-size 16


VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --quantization compressed-tensors --enable-chunked-prefill --max_num_batched_tokens 1024 --block-size 16


VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --input-len 128 --output-len 128 --max-model-len 1024  --enforce-eager --quantization compressed-tensors --enable-chunked-prefill --max_num_batched_tokens 16384 --block-size 16


BEST on dataset
VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.96 --max-model-len 1024  --enforce-eager --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --dataset ShareGPT_V3_unfiltered_cleaned_split.json

try 2: (performed better ) ~7.9K tok/s
VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json 

try 3: (performed best ) ~8648K tok/s
VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512

try 4: (performed best ) 
Throughput: 19.78 requests/s, 8347.56 total tokens/s, 3959.69 output tokens/s

having sample size of 4096: Throughput: 20.79 requests/s, 8944.39 total tokens/s, 4296.93 output tokens/s

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512 --enable_prefix_caching


CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization awq  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512

BESTEST with better scheduler

Throughput: 25.22 requests/s, 10648.51 total tokens/s, 5061.07 output tokens/s

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512 --enable_prefix_caching --num-prompts 1024 --num_scheduler_steps 16

Throughput: 25.21 requests/s, 10645.82 total tokens/s, 5059.79 output tokens/s
--max_logprobs 1

Throughput: 25.25 requests/s, 10660.92 total tokens/s, 5066.97 output tokens/s
--disable_log_stats

Throughput: 25.18 requests/s, 10632.85 total tokens/s, 5053.63 output tokens/s
--async_engine

RM:  --enable_prefix_caching (it is bad for high number of running request as it pollutes the cache??)

RM: --num_scheduler_steps 64 , lower to 16 (seems like 8-16 are the sweet spot)
Throughput: 25.96 requests/s, 10962.19 total tokens/s, 5210.16 output tokens/s

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512 --num-prompts 1024 --num_scheduler_steps 16 --max_logprobs 1 --async_engine


BESTEST 8k context
Throughput: 23.40 requests/s, 10069.91 total tokens/s, 4762.19 output tokens/s

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 256 --num-prompts 1024 --num_scheduler_steps 16 --max_logprobs 1 --async_engine --disable_log_stats


try 5: (new int8 model, fa2 backend) 
Throughput: 16.02 requests/s, 6762.65 total tokens/s, 3207.89 output tokens/s

CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512

try 6: (new int8 model, flashinfer backend) 
Throughput: 18.45 requests/s, 7788.45 total tokens/s, 3694.48 output tokens/s

VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512 --enable_prefix_caching

try 3: 7781 tok/s
VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024  --quantization compressed-tensors --max_num_batched_tokens 16384 --block-size 16  --seed 42 --enable-chunked-prefill  --disable-log-stats --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 512 --disable_log_stats 

https://images.nvidia.com/aem-dam/Solutions/Data-Center/l4/nvidia-ada-gpu-architecture-whitepaper-v2.1.pdf

```

[-h] [--backend {vllm,hf,mii}] [--dataset DATASET] [--input-len INPUT_LEN] [--output-len OUTPUT_LEN] [--model MODEL] [--tokenizer TOKENIZER]
                               [--quantization {aqlm,awq,deepspeedfp,tpu_int8,fp8,fbgemm_fp8,marlin,gguf,gptq_marlin_24,gptq_marlin,awq_marlin,gptq,squeezellm,compressed-tensors,bitsandbytes,qqq,None}]
                               [--tensor-parallel-size TENSOR_PARALLEL_SIZE] [--n N] [--use-beam-search] [--num-prompts NUM_PROMPTS] [--seed SEED] [--hf-max-batch-size HF_MAX_BATCH_SIZE] [--trust-remote-code]
                               [--max-model-len MAX_MODEL_LEN] [--dtype {auto,half,float16,bfloat16,float,float32}] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--enforce-eager]
                               [--kv-cache-dtype {auto,fp8,fp8_e5m2,fp8_e4m3}] [--quantization-param-path QUANTIZATION_PARAM_PATH] [--device {auto,cuda,cpu,openvino,tpu,xpu}] [--enable-prefix-caching]
                               [--enable-chunked-prefill] [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS] [--download-dir DOWNLOAD_DIR] [--output-json OUTPUT_JSON] [--distributed-executor-backend {ray,mp}]
                               [--load-format {auto,pt,safetensors,npcache,dummy,tensorizer,bitsandbytes}]
```



GPU:
1 LLM GPU unit = 2K token / second -> 2 x 3.6 x 24 x 30 = 5184M token / month = 31GB of data -> 310GB data (10x junk for API)
1 user = 100 query per month avg 500 tokens -> 50K tokens -> 1 GPU = 103K users

AWS 
1000 connection per mind -> 1 x 3.6 x 24 x 30 = 2592M requests -> 43.2M users -> 4.2M users (10x load at peak hours)
10 GB per hour -> 10 x 24 x 30 = 7200 GB data per month -> 20 GPU?

main GPU choices
1. runpod
2. akash
3. ionet
4. vast ai


bash -c '
    apt update;
    apt install -y wget;
    mkdir -p /workspace;
    DEBIAN_FRONTEND=noninteractive apt-get install openssh-server -y;
    mkdir -p ~/.ssh;
    chmod 700 ~/.ssh;
    echo "$PUBLIC_KEY" >> ~/.ssh/authorized_keys;
    chmod 700 ~/.ssh/authorized_keys;
    service ssh start;
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py;
    python3 get-pip.py;
    rm get-pip.py;
    pip3 install -U --no-cache-dir jupyterlab jupyterlab_widgets ipykernel ipywidgets;
    jupyter lab --allow-root --no-browser --port=8888 --ip=* --ServerApp.terminado_settings="{\"shell_command\":[\"/bin/bash\"]}" --ServerApp.token=$JUPYTER_PASSWORD --ServerApp.allow_origin=* --FileContentsManager.preferred_dir=/workspace;
    sleep infinity

### Resizable bar
1. if pcie ends up becoming a bottleneck (which it does), resizable bar might be the fix: https://github.com/tinygrad/open-gpu-kernel-modules


### Demo

1. small startup with variable load, baselining at 8 req/sec
	1. perf: Throughput: 2.30 requests/s, 1044.29 total tokens/s, 547.63 output tokens/s
	2. VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 8 --num-prompts 96 --num_scheduler_steps 8 --max_logprobs 1 --async_engine
2. us: with 32 clinets (256 req / sec)
	1. perf:
	2. VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 256 --num-prompts 1024 --num_scheduler_steps 16 --max_logprobs 1 --async_engine





### Setup vllama on single H100 machine (lambda labs)
checklist:

1. Cuda version and gpu info: `nvidia-smi` (check persistent mode on gpu)
2. make sure have `nvtop`
3. Conda install https://docs.anaconda.com/miniconda/
	1. `source ~/miniconda3/bin/activate`
	2. activate new conda env
4. install vllm https://docs.vllm.ai/en/latest/getting_started/installation.html
	1. `pip install vllm`
5. Hugging face setup
	1. pip install -U "huggingface_hub[cli]"
	2. huggingface-cli login --token [REDACTED] --add-to-git-credential
	3. change directory for model cache: 
	4. install hf_transfer 
	5. `HF_HUB_ENABLE_HF_TRANSFER=1`


VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 256 --num-prompts 1024 --num_scheduler_steps 16 --max_logprobs 1 --async_engine

python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 256 --num-prompts 1024 --num_scheduler_steps 16 

VLLM_ATTENTION_BACKEND=FLASHINFER  python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8 --gpu-memory-utilization 0.9 --max-model-len 1024 --quantization compressed-tensors  --max_num_batched_tokens 16384 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 256 --num-prompts 48 --num_scheduler_steps 16 


70B param model:
VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=0 python benchmark_throughput.py --model neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 --gpu-memory-utilization 0.95 --max-model-len 8000 --quantization compressed-tensors  --kv-cache-dtype fp8  --max_num_batched_tokens 16000 --block-size 16 --seed 42  --dataset ShareGPT_V3_unfiltered_cleaned_split.json --max_num_seqs 16 --num-prompts 64  --num_scheduler_steps 16 --max_logprobs 1 --async_engine