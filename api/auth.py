import bcrypt

# Returns a hash of the password with a random salt
def hash(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

# Returns true on match, false otherwise
def authenticate(password, hashed):
    return bcrypt.hashpw(password, hashed) == hashed
