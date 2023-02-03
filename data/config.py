from environs import Env

# using the environs library
env = Env()
env.read_env()

# We read the following from the .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # list of admins
IP = env.str("ip")  # The host ip address


DB_USER = env.str("DB_USER")  # Database user
DB_PASS = env.str("DB_PASS")  # Database password
DB_NAME = env.str("DB_NAME")  # Database name
DB_HOST = env.str("DB_HOST")  # Database host
