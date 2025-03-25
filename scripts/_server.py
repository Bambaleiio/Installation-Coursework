import os
import sys
import socket
import torch
import transformers

class _LLM_CONFIG:
    _Task : str = "text-classification"
    _LLM_Model : str = "transformers"
    _ModelName: str = "bhadresh-savani/distilbert-base-uncased-emotion"
    _Tokenizer : str = "bhadresh-savani/distilbert-base-uncased-emotion"

    @staticmethod
    def pipeline():
        try:
            _pipeline = transformers.pipeline
            return _pipeline(
                _LLM_CONFIG._Task,
                model=_LLM_CONFIG._ModelName,
                tokenizer=_LLM_CONFIG._Tokenizer,
                top_k=1
            )
        except Exception as e:
            print(e)

        return None

class _LLM:
    _Pipline = None

    @staticmethod
    def _set_pipeline(_f) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _LLM._Pipline):
                _LLM._Pipline = _LLM_CONFIG.pipeline()
            return _f(*args, **kwargs)
        return _w

    @_set_pipeline
    @staticmethod
    def proccess_word(word : str) -> str:
        try:
            _response = _LLM._Pipline(word)
            _emotions = { pred['label']: pred['score'] for pred in _response[0] }
            _main_emotion = max(_emotions, key=_emotions.get)
            return _main_emotion
        except Exception as e:
            print(e)


class ServerCore:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self._init_llm()
        self._init_server()

    def _init_llm(self) -> None:
        return
        token = os.getenv('HUGGINGFACE_TOKEN')
        login(token=token)

        self.tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

        self.model = AutoModelForCausalLM.from_pretrained(
            "mistralai/Mistral-7B-Instruct-v0.2",
            device_map='auto',
            quantization_config=BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16
            ),
            token=token
        )

    def _process_request(self, text) -> str:
        _w : str = _LLM.proccess_word(text)
        print(f"Generated emote : {_w}")
        return _w
        emotion: str = self._classify_emotion(text)
        return emotion
        synonyms = self._generate_synonyms(text)
        return f"{emotion}|{','.join(synonyms)}"

    def _classify_emotion(self, text):
        prompt = f"Classify emotion: {text}\nReturn one of: Happy, Sad, Angry, Fearful, Surprised, Neutral"
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=5)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.strip().split()[-1]

    def _generate_synonyms(self, text):
        prompt = f"Generate synonyms for: {text}\nOne per line, no commentary"
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=100, temperature=0.8)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return [line.strip() for line in response.split("\n") if line.strip()][5:]

    def _init_server(self) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

    def run(self) -> None:
        try:
            while True:
                conn, addr = self.server_socket.accept()
                print(f"New connection from {addr}")

                data: str | None = conn.recv(1024).decode('utf-8')
                if data:
                    response = self._process_request(data)
                    conn.send(response.encode('utf-8'))

        except KeyboardInterrupt:
            self.server_socket.close()
            print("Server stopped")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
        server = ServerCore(host, port)
        server.run()
    else:
        print("Usage: python _server.py <host> <port>")