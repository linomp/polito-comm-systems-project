from simple_websocket_server import WebSocketServer, WebSocket


def read_nfc_tag():
    # TODO: add the real code for NFC tag reading
    return "123456789"


class NfcTagReaderSocket(WebSocket):
    def connected(self):
        print(self.address, 'connected')
        for client in clients:
            client.send_message(self.address[0] + u' - connected')
        clients.append(self)

    def handle_close(self):
        clients.remove(self)
        print(self.address, 'closed')
        for client in clients:
            client.send_message(self.address[0] + u' - disconnected')

    def handle(self):
        if self.data == "read_nfc_tag":
            nfc_tag_value = read_nfc_tag()
            for client in clients:
                client.send_message(nfc_tag_value)


clients = []

server = WebSocketServer('', 9999, NfcTagReaderSocket)
server.serve_forever()
