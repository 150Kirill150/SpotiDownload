from pyrogram import Client
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("config.ini")  # читаем конфиг

print(config)
print("---------------------------------------")
print(config["Telegram"])
print(type(config["Telegram"]))
print("---------------------------------------")
print(config["Telegram"]["api_id"])
print(type(config["Telegram"]["api_id"]))
api_id = config["Telegram"]["api_id"]
api_id = int(api_id)
print("---------------------------------------")
print(config["Telegram"]["api_hash"])
print(type(config["Telegram"]["api_hash"]))
api_hash = config["Telegram"]["api_hash"]
api_hash = str(api_hash)
print("---------------------------------------")
print(config["Telegram"]["phone_number"])
print(type(config["Telegram"]["phone_number"]))
phone_number = config["Telegram"]["phone_number"]
phone_number = str(phone_number)

app = Client("cyberpunk", str(api_id), str(api_hash))

@app.on_message()
def message(Client, message):
    print(message)
    log = open("log", "a")
    log.write(f"\n {message}")
    log.close

if __name__ == '__main__':
    app.run()  # эта строка запустит все обработчики