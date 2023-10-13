import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        if packet.haslayer(scapy.TCP):
            print("Paquete TCP detectado:")
            print(f"Origen: {packet[scapy.IP].src}:{packet[scapy.TCP].sport}")
            print(f"Destino: {packet[scapy.IP].dst}:{packet[scapy.TCP].dport}")
            print(f"Datos: {packet[scapy.Raw].load}")
        elif packet.haslayer(scapy.UDP):
            print("Paquete UDP detectado:")
            print(f"Origen: {packet[scapy.IP].src}:{packet[scapy.UDP].sport}")
            print(f"Destino: {packet[scapy.IP].dst}:{packet[scapy.UDP].dport}")
            print(f"Datos: {packet[scapy.Raw].load}")

scapy.sniff(filter="udp or tcp", prn=packet_callback)
