from twilio.rest import Client


class Call:
    def __init__(self) -> None:
        account_sid = "ACc34dbe164d7eb4542a3bab9622e7da02"
        auth_token = "427b5061b6a336fd61e1253328870ba9"

        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml = "<Response><Say> fire alarm fire alarm. respond immediately</Say></Response>",
            to = "+919663628104",
            from_ = "+15136665835"
        )

        print(call.sid)
