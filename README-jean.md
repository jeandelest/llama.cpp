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