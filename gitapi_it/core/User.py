from .utils import run_query
USER = """
  bio
  email
  avatarLink:avatarUrl
  accountCreatedAt:createdAt
  isAdmin:isSiteAdmin
  location
  name
  twitterUsername
  isDevMember:isDeveloperProgramMember
  userId:databaseId
  pinnedItems:anyPinnableItems 
"""
class User:
  def __init__(self, token):
    self.token = token 
    if self.token == None:
      raise Exception("Token argument must be filled out!")
  def getLargeGraphqlData(self, username = None):
    self.user = username
    if self.user == None:
      raise Exception("Username argument must be filled out!")
    
    query = """query UserData { 
          user(login: \"""" + self.user + """\") { 
            """ + USER + """
          } 
      }
    """
    return run_query(query, self.token)

class Repo:
  pass