import requests
import urllib3

LOGIN_URL=f'https://login.microsoftonline.com/6197edc2-01c0-4b24-8919-8f827d5c4dfa/oauth2/token'
CLIENT_ID='66827430-a267-471d-8a79-06940b2792a4'
GRANT_TYPE='client_credentials'
CLIENT_SECRET='Zn18Q~VwrI9orkNUHtbpweVmJcsZJpxK1~2Ebdfn'
RESOURCE='https://amtrakdev106c5dd72b7ca8401cdevaos.axcloud.dynamics.com'
response=requests.post(LOGIN_URL,data={'client_id':CLIENT_ID,'client_secret': CLIENT_SECRET,'resource':RESOURCE,'grant_type':GRANT_TYPE}).json()
get_access_token=response['token_type'],response['access_token']
print(get_access_token)

def get_access_token():
    return (response['token_type'],response['access_token'])
