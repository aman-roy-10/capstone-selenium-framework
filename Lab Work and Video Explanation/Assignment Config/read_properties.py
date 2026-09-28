from configparser import ConfigParser

config = ConfigParser()

# Read properties file
config.read("config.properties")

# Print values
print("Browser:", config.get("DEFAULT", "browser"))
print("URL:", config.get("DEFAULT", "url"))
print("Username:", config.get("DEFAULT", "username"))
print("Password:", config.get("DEFAULT", "password"))