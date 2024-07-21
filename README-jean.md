# Notes on using 

Exploration on `llama.cpp`

## Installation

```bash
make (compile - slowly)
make -j 8 (compile more faster)
```

## Run

```bash
./llama-cli -m models/name --prompt "Who's the US president?" (inference with logs)
./llama-cli -m models/name --prompt "Who's the US president?" 2>/dev/null (inference without logs)
```

## The more useful will be llama-cli

```html
general:
    --no-display-prompt (don't print prompt at generation)
model:
    -m <model_path>
--prompt (-p) <prompt>
logging:
    --log-disable <disable_log>
retrieval:
    --context-file <context_file> 
backend:
    --mlock (force the system to keep the model in memory)
parallel section could be interesting for optimization
sampling:
    --temp (for temperature)
```

## Avoid repetition penalties

```html
--ctx_size 1024
--batch-size 2048
--temp 0.82
--top-k 30
--top-p 1.8
--tfs 2.0
--typical 1.0
--keep -1
--repeat-last-n 1024
--repeat-penalty 1.2
--no-penalize-nl
--mirostat 1
--mirostat-lr 0.5
--mirostat-ent 4.0
```

## Better build process

```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
ccache -c (clean cache before rebuilding)
```

## Convert to gguf and quantize

```bash
python3 download.py # modify and apply
python3 convert_hf_to_gguf.py <base_model> --outfile <model_name>.gguf --outtype <quantize_type> (e.g. q8_0) # not all of the quantize method available here
cd llama.cpp/build/bin && ./quantize ./models/Llama-2-7b-chat-hf/ggml-model-f16.gguf ./models/Llama-2-7b-chat-hf/ggml-model-q4_0.gguf q4_0
```