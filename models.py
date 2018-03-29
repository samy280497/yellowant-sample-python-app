"""Generic db model classes for this YellowAnt (YA) application """
import uuid


class User:
    """User model for your application
    
    A very basic user model (only for demonstration purpose). Practically, you will be storing user credentials with the
    help of a library/framework which connects with your database.
    """    
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password


class UserIntegration:
    """User YellowAnt Integration model

    Holds the information which identifies your user with an integration on YA.
    
    Since a single YA user is allowed to have multiple integrations with your application on YA, you need to store
    a one-to-many relationship for a user to many YA user integrations.
    
    For example, if this is a mail application, users might want to connect their personal mail and work mail with YA.
    In this case, a single user will have two YA integrations, one which connects the personal mail, and the other which
    connects the work mail.

    Args:
        user (User): Your application user
        yellowant_user_id (int): YA user id
        yellowant_team_subdomain (str): YA user's team subdomain # each user on YA belongs to a team, irrespective of
            the team size
        yellowant_integration_id (int): Unique YA user integration id
        yellowant_integration_invoke_name (str): YA integration invoke name # each integration of your application is
            controlled by the user with the help of your application's default invoke name. Since a YA user is allowed
            to have multiple integrations with your application, YA will suffix the default invoke name for users who
            want to integrate more than once with your application, so that they can control the different integrations
            with their respective invoke names.
        yellowant_integration_token (str): Unique token per integration # This token allows your application to 
            perform actions on the YA platform for the YA user integration.
    """
    def __init__(self, user, yellowant_user_id, yellowant_team_subdomain, yellowant_integration_id,
            yellowant_integration_invoke_name, yellowant_integration_token):
        self.user = user
        self.yellowant_user_id = yellowant_user_id
        self.yellowant_team_subdomain = yellowant_team_subdomain
        self.yellowant_integration_id = yellowant_integration_id
        self.yellowant_integration_invoke_name = yellowant_integration_invoke_name
        self.yellowant_integration_token = yellowant_integration_token

class YellowAntRedirectState:
    """Model to store YA oauth requests with users"""    
    def __init__(self, user, state):
        """Create a new entry between the user and the oauth state

        Args:
            user (User): Your application user
            state (str): A unique ID which helps in matching an oauth2 code from YA to a user
        """
        self.user = user
        self.state = state

