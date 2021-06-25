from __init__ import User
import os
user = User(os.environ['token'])
print(user.getGraphqlData("darkdarcool"))