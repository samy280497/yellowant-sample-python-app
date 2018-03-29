"""Mock database for this YellowAnt (YA) application"""
from models import RedirectStateYellowAnt, UserIntegration


class Database:
    def __init__(self):
        self.users = {}
        self.user_integrations = {}
        self.yellowant_redirect_states = {}
    
    def get_user(self, id):
        return self.users.get(id)
    

    def create_user_integration(self, user, yellowant_user_id, yellowant_team_subdomain, yellowant_integration_id,
            yellowant_integration_invoke_name, yellowant_integration_token):
        self.user_integrations[yellowant_integration_id] = UserIntegration(user=user,
            yellowant_user_id=yellowant_user_id, yellowant_team_subdomain=yellowant_team_subdomain,
            yellowant_integration_id=yellowant_integration_id,
            yellowant_integration_invoke_name=yellowant_integration_invoke_name,
            yellowant_integration_token=yellowant_integration_token)
    

    def get_user_integration(self, yellowant_integration_id):
        return self.user_integrations.get(yellowant_integration_id)


    def create_yellowant_redirect_state(self, user, state):
        self.yellowant_redirect_states[state] = RedirectStateYellowAnt(user=user, state=state)
    
    def get_yellowant_redirect_state(self, state):
        return self.yellowant_redirect_states.get(state)