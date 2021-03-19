# storing-passwords-sqlite console app
# Short description
Project is storing username and hashed password with salt in SQLite database. 
# How it works
User enter username and password. Then program makes hashes using pbkdf2_hmac from the hashlib python library and generate random unique salt. 
After all hashing stuff program creates table in the database if it already does not exist.
Next data are inserting into the password table in the database.
The program also verify passwords.
