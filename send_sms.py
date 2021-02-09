from twilio.rest import Client

account_sid = "XXXX"
auth_token  = "XXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16478695209", 
    from_="+16479059186",
    body="Hello from Python!")

print(message.sid)
