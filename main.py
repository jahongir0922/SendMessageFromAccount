import asyncio
import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    api_id = os.getenv('API_ID')
        api_hash = os.getenv('API_HASH')
            phone = os.getenv('PHONE')
                username = os.getenv('TARGET_USERNAME')
                    
                        if not api_id or not api_hash or not phone or not username:
                                print("Xatolik: .env faylini tekshiring!")
                                        return
                                            
                                                client = TelegramClient('session', int(api_id), api_hash)
                                                    await client.start(phone)
                                                        
                                                            message = 'Salom!'
                                                                interval = 60
                                                                    
                                                                        while True:
                                                                                await client.send_message(username, message)
                                                                                        print(f"Yuborildi: {message}")
                                                                                                await asyncio.sleep(interval)

                                                                                                asyncio.run(main())