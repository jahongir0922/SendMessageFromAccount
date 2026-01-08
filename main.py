import asyncio
import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone)
        
            username = 'Oisha_0208'
                message = 'Salom!'
                    interval = 60  # soniyada
                        
                            while True:
                                    await client.send_message(username, message)
                                            print(f"Yuborildi: {message}")
                                                    await asyncio.sleep(interval)

                                                    with client:
                                                        client.loop.run_until_complete(main())
                                                    

                                                    
                                                
                                            
                                                        
                                                        