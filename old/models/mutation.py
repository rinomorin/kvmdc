from graphene import ObjectType, String
# from models.MFA import GenerateRegistration


class Mutation(ObjectType):
    add_user = String(name=String())
    # registerUser(username: String!, password: String!): User!
    # generate_registration = GenerateRegistration.Field()
    # login = String(username=String(), password=String())

    def resolve_add_user(root, info, name):
        # Your logic to add a user here
        return f'Added user: {name}'

    # def resolve_register_user(parent, info, username, password):
    # # Call the function to register the user
    # return register_user(username, password)
