"""Generic URLS for this YellowAnt (YA) application"""
from views import request_yellowant_oauth_code, yellowant_oauth_redirect, yellowant_api


### static urls ###
# URL to obtain oauth2 access for a YA user
YA_OAUTH_URL = "https://www.yellowant.com/api/oauth2/authorize/"
# URL to receive oauth2 codes from YA for user authentication. As a developer, you need to provide this URL in the YA
# developer console so that YA knows exactly where to send the oauth2 codes.
YA_REDIRECT_URL = "https://www.myapp.com/redirecturl/"
# URL to receive requests from a user to perform actions with this application through YA
YA_API_URL = "/ya-api"


url_views = {
    "/create-new-integration/": request_yellowant_oauth_code,
    YA_REDIRECT_URL: yellowant_oauth_redirect,
    YA_API_URL: yellowant_api,
}