from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1XXXX", 
    from_="+12158762820",
    body="Hello from Python!")

print(message.sid)
