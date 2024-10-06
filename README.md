tạo extensions khác tìm thấy thì lấy các dòng đó
tạo extensions khác tìm thấy thì thay thế văn bản khác










```python

def decode_token(self, token):
    try:
        payload = jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algorithm])

        tz = pytz.timezone('Asia/Ho_Chi_Minh')
        current_time = datetime.utcnow()
        current_time = current_time.replace(tzinfo=pytz.utc).astimezone(tz)
        current_time = current_time.timestamp()

        otp_expires = payload.get("otp_expires")

        if int(current_time) > int(otp_expires):
            message = "OTP expired"
            sub = payload["sub"]
            scopes = payload["scopes"]
            return message, sub, scopes

        message = "Success"
        sub = payload["sub"]
        scopes = payload["scopes"]
        return message, sub, scopes

    except jwt.ExpiredSignatureError:
        message = "Expired signature"
        sub = None
        scopes = []
        return message, sub, scopes

    except jwt.InvalidTokenError:
        message = "Invalid token"
        sub = None
        scopes = []
        return message, sub, scopes
```