from huggingface_hub import snapshot_download
from huggingface_hub import login
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

model_id="mistralai/Mistral-Nemo-Base-2407"
models_path = "downloaded_hf_models/"
login(token=os.environ.get("HF_TOKEN"))
snapshot_download(repo_id=model_id, local_dir=models_path + "Mistral-Nemo-Base-2407",
                  local_dir_use_symlinks=False, revision="main")