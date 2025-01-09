from cryptography.fernet import Fernet

# Generate a valid Fernet key
key = Fernet.generate_key()

# Print the key as a base64 URL-safe string
print(key.decode())
