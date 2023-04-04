from os import environ
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from config import *

CMND = [".", "/", ":"]
CHATS = [int(chnel) for chnel in environ.get("CHANNELS", None).split()]       

main_chat = filters.chat(CHATS) if CHATS else (filters.group | filters.channel)         

User = Client(
    name = "acceptUser",
    session_string = SESSION,
    api_id = API_ID,
    api_hash = API_HASH
)

@User.on_message(filters.command(["run", "approve"], CMND) & main_chat)                     
async def approve(client: User, message: Message):
    chat=message.chat 
    try:
       try:
          await client.approve_all_chat_join_requests(chat.id)#1
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#2
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#3
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#4
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#5
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#6
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#7
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#8
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#9
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#10
          return
       except FloodWait as x:
          asyncio.sleep(x.value)
          await client.approve_all_chat_join_requests(chat.id)#1
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#2
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#3
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#4
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#5
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#6
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#7
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#8
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#9
          await asyncio.sleep(4)
          await client.approve_all_chat_join_requests(chat.id)#10
         #incresed Accept Count
          return    
    except Exception as e:
       print(e)
    msg = await client.send_message(chat.id, "mission completed ✅️ approved all joinrequest approved 1k users")
    await asyncio.sleep(5)
    await msg.delete()
 

print("bot started....")
User.run()
