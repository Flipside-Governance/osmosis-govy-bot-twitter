import requests
import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

## Import Twitter API Keys From .env file 
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

## Twitter OAuth2 Handling 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Call the Flipside API 
query_url = 'https://node-api.flipsidecrypto.com/api/v2/queries/a55642c5-f5a3-48af-bc89-862e506ae374/data/latest'
query_result_set = requests.get(query_url)
data = query_result_set.json()

# Sort the results and prep the tweet body
for record in data: 
    tx_id = record['TX_ID']
    voter = record['VOTER']
    label = record['LABEL']
    proposal_id = record['PROPOSAL_ID']
    vote_option = record['VOTE_OPTION']
    memo = record['MEMO']
    link_tx = 'https://www.mintscan.io/osmosis/txs'+tx_id
    link_prop = 'https://www.mintscan.io/osmosis/proposals'+str(proposal_id)
    if vote_option == 1: 
        vote = 'voted yes'
    elif vote_option == 2: 
        vote = 'abstained'
    elif vote_option == 3: 
        vote = 'voted no'
    else: 
        vote = 'voted no with veto'

    time.sleep(1)
    # Set the payload (i.e. the body of the tweet)
    payload == f"{label} {vote} on proposal {proposal_id} with the following rational: {memo}.\n{link_prop}"
    
    # Update the status of the Twitter Bot 
    api.update_status(payload)
    print('Done!') ## This is a console log 