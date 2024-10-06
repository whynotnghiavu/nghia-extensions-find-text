import jwt

def decode_token(self, token):
    try:
        payload = jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algorithm])
        return payload["sub"], payload.get("scopes", [])
    except jwt.ExpiredSignatureError:
        return "Expired signature", []
    except jwt.InvalidTokenError:
        return "Invalid token", []