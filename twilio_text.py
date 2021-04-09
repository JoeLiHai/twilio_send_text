from twilio.rest import Client

account_sid = "AC46b44455738c67cbb21c2b3cbe1b626d"

auth_token = "..................................."

client = Client(account_sid, auth_token)

message = client.messages.create(
	to="+886.........",
	from_="+13126263470",
	body="OMG SMS sent！！！")

print(message.sid)