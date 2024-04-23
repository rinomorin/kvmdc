import crypt


def authenticate(username, password):
    shadow_file = '/etc/shadow'
    with open(shadow_file, 'r') as f:
        for line in f:
            fields = line.strip().split(':')
            if fields[0] == username:
                # Extract the hashed password from /etc/shadow
                hashed_password = fields[1]
                # Use crypt.crypt() to hash the provided password
                hashed_input = crypt.crypt(password, hashed_password)
                # Compare the hashed passwords
                if hashed_input == hashed_password:
                    return True
                else:
                    return False
    return False


# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate(username, password):
    print("Authentication successful")
else:
    print("Authentication failed")
