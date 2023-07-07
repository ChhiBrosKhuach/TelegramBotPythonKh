import requests


def sendMessage(bot_token, chat_id, message):
	url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
	params = {"chat_id": chat_id, "text": message}
	response = requests.get(url, params=params)
	if response.status_code == 200:
		print("Message sent successfully!")
	else:
		print("Failed to send message.")

def sendPhoto(bot_token, chat_id, photo, message):
  url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    params = {
        "chat_id": chat_id,
        "caption": message
    }
    files = {
        "photo": open(photo, "rb")
    }
    response = requests.post(url, params=params, files=files)
    if response.status_code == 200:
        print("Photo sent successfully!")
    else:
        print("Failed to send photo.")
      
def main():
    # Call function 1
    print('Hello')

if __name__ == "__main__":
    main()
