# import credentials as creds

# def get_login_credentials():
#     """
#     Retrieve login credentials from the credentials module.

#     Returns:
#         tuple: A tuple containing the username and password.
#     """
#     username = creds.FYERS_SECRET_ID
#     password = creds.FYERS_API_ID
#     return username, password

# if __name__ == "__main__":
#     user, pwd = get_login_credentials()
#     print(f"Username: {user}")
#     print(f"Password: {pwd}")


# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = "WJ8C9FNSA4-100"
secret_key = "ZWWMH2N2YV"
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "code"  
state = "sample_state"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)
