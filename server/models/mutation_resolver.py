# from graphene import Schema
# from flask import request, jsonify
# from models.mutation import Mutation
# from models.Query import Query


# def ResolvRegistration():
#     data = request.json
#     username = data.get('username')
#     password = data.get('password')
#     # code = data.get('code')
#     # Execute the registration mutation with GraphQL
#     result = schema.execute(f'''
#         mutation {{
#             registerUser(username: "{username}", password: "{password}") {{
#                 qrCode
#             }}
#         }}
#     ''')

#     qr_code = result.data['registerUser']['qrCode']

#     # Registration successful
#     return jsonify({"qr_code": qr_code}), 200


# schema = Schema(query=Query, mutation=Mutation)
