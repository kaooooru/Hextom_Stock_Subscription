from twilio.rest import Client

account_sid = "ACa2a8034dadd2bd364d00a64187ae037c"
auth_token  = "75f5feebbb1a43ed1a602e76709e0982"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16478695209", 
    from_="+16479059186",
    body="Hello from Python!")

print(message.sid)
