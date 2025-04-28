from environs import Env

env = Env()
env.read_env()

# Weather api key
api_key = env.str("API_KEY")
# Location
city = env.str("CITY")
