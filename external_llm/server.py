import socket

SERVER_ADRESS = ('localhost', 8686)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADRESS)
server_socket.listen(5)


from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
# print(classifier("I love this!"))

print("server is running")

while True:
    connection, adress = server_socket.accept()
    print(f"new connection from {adress}")

    byte_data = connection.recv(1024)
    print(byte_data)

    decoded_data = byte_data.decode("utf-8")
    print(decoded_data)

    res = classifier(decoded_data)
    print(res)

    connection.send(bytes((res[0]['label']), encoding='UTF-8'))

    connection.close()