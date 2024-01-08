import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from configparser import ConfigParser

async def main():
    config = ConfigParser()
    config.read('twitter_login.ini')

    login_id = config['twitter']['login_id']
    login_password = config['twitter']['login_password']
    email = config['twitter']['email']
    email_password = config['twitter']['email_password']
    api = API()

    # add accounts
    await api.pool.add_account(login_id, login_password, email, email_password)
    await api.pool.login_all()

    query = "#ethereum"
    async for tweet in api.search(query, limit=1):
        print(tweet.id, tweet.user.username, tweet.rawContent)

if __name__=='__main__':
    asyncio.run(main())