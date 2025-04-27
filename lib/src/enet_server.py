import enet
import dearpygui.dearpygui as dpg
import time

dpg.create_context()
dpg.create_viewport(title="The Roc Server",width=200,height=400,always_on_top=True)
dpg.setup_dearpygui()

host = enet.Host(enet.Address(b"127.0.0.1", 12345), 32, 0, 0, 0)

server_list = []
server_num = 0

with dpg.window(label="Background",tag="Background"):
    with dpg.group(horizontal=True):
        dpg.add_text("Active Clients : ")
        client_num = dpg.add_text(default_value=0)
    dpg.add_text("Live Clients")
    dpg.add_spacer(height=3)

    with dpg.table(tag="client_list",borders_innerH=True,borders_innerV=True,borders_outerH=True,borders_outerV=True):
        dpg.add_table_column(label="Client ports")
        dpg.add_table_column(label="")

dpg.show_viewport()
while dpg.is_dearpygui_running():
    dpg.set_primary_window("Background",True)

    event = host.service(0)

    def kick(sender,app_data,user_data):
        user_data.send(0, enet.Packet(b"1003", enet.PACKET_FLAG_RELIABLE))
        time.sleep(0.1)
        user_data.disconnect()
        print("passed")
     
            
    if event.type == enet.EVENT_TYPE_CONNECT:                           
        print(f"New client connected: {event.peer.address}")
        server_list.append(event.peer.address.port)
        server_num += 1 
        dpg.set_value(client_num,server_num)

        with dpg.table_row(parent="client_list",tag=event.peer.address.port):
            dpg.add_text(default_value=event.peer.address.port,)
            dpg.add_button(label="kick",user_data=event.peer,callback=kick)

    elif event.type == enet.EVENT_TYPE_RECEIVE:
        print(f"Received: {event.packet.data}")
        event.peer.send(0, enet.Packet(b"Hello back!", enet.PACKET_FLAG_RELIABLE))

   
    elif event.type == enet.EVENT_TYPE_DISCONNECT:
        server_num -=1 
        dpg.set_value(client_num,server_num)
        if event.peer.address.port in server_list:
            server_list.remove(event.peer.address.port)
        dpg.delete_item(event.peer.address.port)

        print(f"Port {event.peer.address.port} Disconnected or failed to connect.")
        print("Current server list")
        print(server_list)

    dpg.render_dearpygui_frame()
    
    if len(server_list) == 0:
        print("Waiting for clients")

    if len(server_list) > server_num:
        print("Current server list")
        print(server_list)


dpg.destroy_context()

