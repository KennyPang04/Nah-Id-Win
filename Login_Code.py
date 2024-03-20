




# def register(self,request: Request):
#     info = extract_credentials(request)

#     if validate_password(info[1]):
#         salt = bcrypt.gensalt()
#         hash = bcrypt.hashpw(info[1].encode('utf-8'),salt)
#         data = {"username":info[0],"salt":salt,"hash":hash}
#         self.accounts.insert_one(data)
#         response = request.http_version
#         response += " 302 Found redirect\r\n"
#         response +="Content-Type: text/html\r\n"
#         response += "X-Content-Type-Options: nosniff\r\n"
#         response +="Content-Length: 0" + "\r\n"
#         response += "Location: /\r\n\r\n"
#         return response.encode()
#     else:
#         return self.bad_response(request)




# def login(self, request):
#     cred = extract_credentials(request)
#     acc = self.accounts.find_one({"username":cred[0]})
#     if acc == None:
#         return self.bad_response(request)
#     else:
#         salt = acc["salt"]
#         hash = bcrypt.hashpw(cred[1].encode(),salt)
#         if(hash == acc["hash"]):
#             token = secrets.token_hex(16)
#             hashed_token = hashlib.sha256(token.encode()).hexdigest()
#             self.accounts.update_one({"_id":acc["_id"]},{"$set":{"hashed_token":hashed_token}})
#             response = request.http_version
#             response += " 302 Found redirect\r\n"
#             response +="Content-Type: text/html\r\n"
#             response += "X-Content-Type-Options: nosniff\r\n"
#             response +="Content-Length: 0" + "\r\n" + "Set-Cookie: auth_token= " + str(token)+ "; Max-Age=3600; HttpOnly\r\n"
#             response += "Location: /\r\n\r\n"
#             print("logined worked")
#             return response.encode()
#         else:
#             return self.bad_response(request)
        