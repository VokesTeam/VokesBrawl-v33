from Networking.ClientThread import ClientThread
class NetworkFilter:
    def lvl1protect(self, clients, clientinfo, client, address, contime: str, contries):
        if address[0] not in clients:
            contries += 1
            ClientThread(client, address, clients, clientinfo, contime, contries).start()
            clients += address
            clientinfo.append(contime)
            clientinfo.append(contries)
        elif address[0] in clients and contries >= 3:
            print("Warning: strange connection: denying.")
        elif address[0] in clients and contries > 1 and contries < 3:
            contries += 1
            print(f'New connection! Ip: {address[0]}')