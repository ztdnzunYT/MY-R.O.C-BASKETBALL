import enet
import pygame
import sys
import time
pygame.init()
WIDTH,HEIGHT = 500,500 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

client = enet.Host(None, 1, 0, 0, 0)
peer = client.connect(enet.Address(b"127.0.0.1", 12345), 1)
connected = False

print("Searching for server...")
running = True
while running:

    event = client.service(0)
    if event.type == enet.EVENT_TYPE_CONNECT:
        connected = True
        print("Connected to server")
        peer.send(0, enet.Packet(b"Hello server!", enet.PACKET_FLAG_RELIABLE)) 

    if event.type == enet.EVENT_TYPE_RECEIVE:
        server_message = event.packet.data
        if str(server_message ) == "b'1003'":
            print("Error code 1003: Client kicked from server...")
            connected = False
    
    

    message = f"client pressed the space bar"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("this is working")
                peer.send(0,enet.Packet(message.encode(),enet.PACKET_FLAG_RELIABLE))

    screen.fill((255,255,255))
    pygame.display.flip()

pygame.quit() 
sys.exit()
