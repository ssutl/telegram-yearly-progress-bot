# Telegram Yearly Progress Bot
A quick project I created to remind the fam on the Telegram GC that we got to keep going. Regular reminders of our progress through the year to ensure everyone is on track and fufilling full potential ⚡


![image](https://github.com/ssutl/telegram-yearly-progress-bot/assets/76885270/bfcfadba-a02f-43fe-bbd7-90e6026b19e0)
![image](https://github.com/ssutl/telegram-yearly-progress-bot/assets/76885270/2cee5682-96a0-41d5-9523-cdc75d35c2b9)



# Technologies Used
### Backend
1. Python

### API
1. Telegram

# Features Implemented
1. Routine scheduled messages

# How it works
Code is hosted on a server and ran on regular intervals, code uses percentage through the year to select the corresponding image alongside some motivational text to send the groupchat.


# How to run application<br/>
### General config
1. Create an `.env` file in the root directory
2. Add api_key={Your Telegram secret key} to the `.env`
3. Add user_id={Your Telegram user ID} to the `.env`
4. A tutorial on how to access them can be found
5. Add `Quotes` folder with images labelled 1-100

![image](https://github.com/ssutl/telegram-yearly-progress-bot/assets/76885270/e361462b-a0c2-4921-bd72-94cd5888bbff)


### Setup locally
1. `PIP install` (to install needed dependencies)
2. `python bot.py`

### Setup on server
1. Create project and upload code alongside images
