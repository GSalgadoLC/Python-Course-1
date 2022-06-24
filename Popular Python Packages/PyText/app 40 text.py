from twilio.rest import Client
account_sid = "AC869895a19fcaa357958753f7cbe05128"
autho_token = "c23745018eaa5c1e79baca9a58ac3c4c"

client = Client(account_sid, autho_token)

client.messages.create(
    to="18008085555",
    from_="3235537470",
    body="Hi Mark"
)
print("Message Sent")
