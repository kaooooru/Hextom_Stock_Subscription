from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf790e37fc8dc05e01de60d1ca899fc0e"
# Your Auth Token from twilio.com/console
auth_token  = "21991e47a869d8c814a5369901e12450"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16478695209", 
    from_="+12158762820",
    body="Hello from Python!")

print(message.sid)