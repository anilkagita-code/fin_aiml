import pyotp as tp


totp_key='QWYC42SBO6ZLG45E2WREOIDK2MQCVMHW'
key = tp.TOTP(totp_key).now()
print(key)