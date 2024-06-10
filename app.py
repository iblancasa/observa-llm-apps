from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
import flask
from time import sleep
import requests
from random import randint

app = flask.Flask(__name__)

llm = LlamaCPP(
    # "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf"
    model_path="llama-2-7b-chat.Q4_K_M.gguf",
    temperature=0.1,
    max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=3900,
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 1},
    # transform inputs into Llama2 format
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=False,
)

@app.route('/', methods = ['POST', 'GET'])
def root():
    luck = randint(0,5)
    sleep(0.1*luck)
    if luck%2:
        prompt = "hello how are you doing?"

        if flask.request.method == 'POST':
            question = flask.request.json["question"]
            if question:
                prompt = question

        text = llm.complete(prompt)
        sleep(2)
        return flask.Response(text.text)
    return flask.Response(status=500, response="random failure :D")
    



if __name__ == "__main__":
    app.run()
