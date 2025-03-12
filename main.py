from bot import Bot
from web import keep_alive

if __name__ == "__main__":
    keep_alive()
    Bot().run()