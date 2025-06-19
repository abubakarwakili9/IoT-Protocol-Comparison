# Simple Matter server for testing
import asyncio
import json
from datetime import datetime

class SimpleMatterServer:
    def __init__(self):
        self.devices = {}
        self.running = False
    
    async def start_server(self):
        self.running = True
        print(f"[{datetime.now()}] Simple Matter Server Started")
        print("Listening for Matter devices...")
        
        while self.running:
            # This is a simplified server for testing
            # In real Matter, this would be much more complex
            await asyncio.sleep(1)
            
            # Check for new devices (simulation)
            if len(self.devices) == 0:
                print("Waiting for devices to connect...")
    
    def add_device(self, device_id, device_info):
        self.devices[device_id] = device_info
        print(f"Device added: {device_id}")
    
    def stop_server(self):
        self.running = False
        print("Server stopped")

if __name__ == "__main__":
    server = SimpleMatterServer()
    try:
        asyncio.run(server.start_server())
    except KeyboardInterrupt:
        server.stop_server()