import socket

from llm_functions import *

SERVER_ADRESS = ('localhost', 8686)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADRESS)
server_socket.listen(5)


if __name__ == "__main__":

    while True:
        connection, address = server_socket.accept()
        print(f"new connection from {address}")

        byte_data = connection.recv(1024)

        text = byte_data.decode("utf-8")

        emotion = classify_emotion(text)
        print(f"Emotion: {emotion}")

        response = f"Emotion: {emotion}"
        connection.send(bytes(emotion, encoding='UTF-8'))

        # ---------------------------------------------------------

        synonyms = generate_synonyms(text)
        synonyms = synonyms[5:]

        print(f"Synonyms: {synonyms}")

        response = f"Synonyms: {synonyms}"

        connection.send(bytes(response, encoding='UTF-8'))

        connection.close()
