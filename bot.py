import asyncio
from telegram import Bot
from datetime import datetime
import math
import os
from dotenv import load_dotenv

Today = datetime.now()

def configure():
    load_dotenv()

async def send_message(GROUP_ID, bot):
    day_of_year = Today.timetuple().tm_yday
    year = Today.year
    interval = 3.65
    ##Short hand boolean for if the message should be sent now
    arrayOfDaysToSend = []
    
    ##Creating an array of days to send a reminder message
    for i in range(1,366):
        if(abs((i - 1) % interval) < 1):
            arrayOfDaysToSend.append(i)
    
    print(arrayOfDaysToSend)    
    arrayOfDaysToSend[-1] = 365
    dayToSend = day_of_year in arrayOfDaysToSend
    
    percentage = math.floor(((day_of_year) / 365) * 100)
    
    text = f"<b><span class='tg-spoiler'>{'Its the end of the year, you did great!!' if day_of_year == 365 else ('Happy New Year!!' if day_of_year == 1 else '')} We are {percentage}% through {year}, we have {100 - percentage}% left.🥭⚡</span></b>"

    
    
    if(dayToSend):
        ##Grabbing the media path for the specific day
        media_path = get_media(arrayOfDaysToSend.index(day_of_year) + 1)
        if media_path:
            ##So here im splitting the 
            _, extension = os.path.splitext(media_path)
            try:
                if extension.lower() in ['.jpg', '.png']:
                    await bot.send_photo(chat_id=GROUP_ID, photo=media_path, caption=text, write_timeout=60, read_timeout=60, parse_mode='html')
                    print("Sent photo")
                elif extension.lower() == '.gif':
                    await bot.send_animation(chat_id=GROUP_ID, animation=media_path, caption=text, write_timeout=60, read_timeout=60, parse_mode='html')
                    print("Sent gif")
                elif extension.lower() == '.mp4':
                    await bot.send_video(chat_id=GROUP_ID, video=media_path, caption=text, write_timeout=60, read_timeout=60, parse_mode='html')
                    print("Sent video")
            except:
                print("Error sending media")
        else:
            await bot.send_message(text=text, chat_id=GROUP_ID, parse_mode='html')


def get_media(index):
    # Define the path to your media folder
    media_folder = 'Quotes'

    # Check for both jpg, gif, and mp4 files
    for extension in ['jpg', 'gif', 'mp4', 'png']:
        #Creating the file path
        file_path = os.path.join(media_folder, f'{index}.{extension}')
        if os.path.exists(file_path):
            return file_path

    # If no file was found, return None
    print('No file found')  # Print a message if no file is found
    return None



async def main():
    configure()
    bot = Bot(os.getenv('api_key'))
    async with bot:
        # Clear updates
        updates = await bot.get_updates()
        ArrayOfGroupID = []
        ArrayOfChats = []
       
        
        for update in updates:
            if update.message is not None and update.message.chat.id not in ArrayOfGroupID:
                ArrayOfGroupID.append(update.message.chat.id)
                
        for chat in updates:
            if chat.message is not None and chat.message.chat not in ArrayOfChats:
                ArrayOfChats.append(chat.message.chat.title)
                
        print(ArrayOfChats)
        print(ArrayOfGroupID)
                                
        # Then we have to remove duplicate IDs
        cleanedArray = set(ArrayOfGroupID)
        
        if(os.getenv('user_id') in cleanedArray):
            cleanedArray.remove(os.getenv('user_id'))

        if len(cleanedArray) > 0:
            for ID in cleanedArray:
                # Use the first update if available
                await send_message(ID, bot)
        else:
            print("No updates found")
        



if __name__ == '__main__':
    asyncio.run(main())