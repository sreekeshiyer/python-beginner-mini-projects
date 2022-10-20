import base64

string_to_encode = "test string"
string_bytes = string_to_encode.encode("ascii")

base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Base64 encoded string: {base64_string}")
