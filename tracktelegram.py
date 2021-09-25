from pyrogram import Client
import config

app = Client("cyberpunk", config.api_id, config.api_hash, config.phone_number)

@app.on_message()
def message(Client, message):
    if message.chat.username == "spotify_down_bot":
        print(message)

        log = open("log", "a")
        log.write(f"\n {message}")
        log.close()
    if message.chat.username == "KirMozor":
        if message.text == "Send":
            app.send_message("spotify_down_bot", "https://open.spotify.com/track/1T18xjRxt5m22ZOwMPMRhc?si=da06a69dcdce46f5")

if __name__ == '__main__':
    app.run()  # эта строка запустит все обработчики