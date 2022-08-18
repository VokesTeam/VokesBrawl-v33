import time
from threading import *

from Logic.Initial.Device import Device
from Logic.Initial.Player import Players
from Logic.Helpers.get.getName import whatIsIt
from Protocol.LaserMessageFactory import packets

class ClientThread(Thread):
	def __init__(self, client, address, clients, clientinfo, contime, contries): #looks like zezhka
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)
		self.clients = clients
		self.clientinfo = clientinfo
		self.contime = contime
		self.contries = contries

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					id = int.from_bytes(header[:2], 'big')
					name = whatIsIt.getPacketName(id)
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)

					if id in packets:
						print(f'Packet received: id: {id}, name: {name}, length: {length}')
						message = packets[id](self.client, self.player, data)
						message.decode()
						message.process()
					else:
						print(f'Unhandled packet: id: {id}, name: {name}')
				if time.time() - last_packet > 7:
					print(f"{self.address[0]} disconnected!")
					self.client.close()
					self.clients.remove(self.address[0])
					self.clients.remove(self.address[1])
					self.clientinfo.remove(self.contime)
					self.clientinfo.remove(self.contries)
					break
		except:
			self.client.close()
			self.clients.remove(self.address[0])
			self.clients.remove(self.address[1])
			self.clientinfo.remove(self.contime)
			self.clientinfo.remove(self.contries)