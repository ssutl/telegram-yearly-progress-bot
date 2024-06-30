# Telegram Yearly Progress Bot
A quick project I created to remind the fam on the Telegram GC that we got to keep going. Regular reminders of our progress through the year to ensure everyone is on track and fufilling full potential ⚡

![Screenshot 2024-06-30 213402](https://github.com/ssutl/telegram-yearly-progress-bot/assets/76885270/a9bcd10c-d82d-4299-a7f5-6f187fc36912)
![Screenshot 2024-06-30 213317](https://github.com/ssutl/telegram-yearly-progress-bot/assets/76885270/bd7a21dc-8360-4fbe-8a49-1e1eea2e4a9b)



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
