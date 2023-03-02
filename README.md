# Osmosis Govy Twitter Bot 
This repository constains a Twitter bot that tweets vote rationales published on-chain by validators on Osmosis Zone. Vote rationale can be published on-chain by submitting a transaction memo, which can be found in Keplr wallet on the "advanced features" tab accessible before submitting a transaction. 

If you are a validator and would like your rationales included in this bot, all you have to do is send a memo with your vote transaction. Your vote will then be tweeted out within 24 hours. 

This bot utilizes [Flipside Crypto](https://flipsidecrypto.xyz/) Osmosis data to monitor transactions. Flipside Crypto does not provide live data, but data on a 12 hour delay. Therefore, vote transactions will not alert immediately after confirmation on-chain, but within 24 hours. 

## Aims :dart: 
The aim of this Twitter bot is to auto-publish rationales for governance votes that take place on Osmosis. 

A major pain point for validators is publishing and explaining their governance votes. Without an auto-publishing feature, many validators receieve multiple messages from delegators asking them to explain a certain vote. Voters deserve a response, however many messages can get lost in notification shuffle. 

## Setup :construction:

#### Flipside Crypto
The Twitter bot pulls Osmosis voting data using [this query](https://app.flipsidecrypto.com/velocity/queries/a55642c5-f5a3-48af-bc89-862e506ae374) on Flipside Crypto. To modify the query, you will need a Flipside Crypto account. If you do not already have an account, you can sign up for free using either your email, Discord account, or Ethereum wallet. Then, fork the query and make the desired changes using Snowflake SQL. 

#### Twitter
This bot requires a Twitter Developer Account. To create a developer account, sign in to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/projects-and-apps) with the Twitter account you wish to use to send the automated tweets. Once your access has been approved, create a new application on the Twitter Developer Portal and generate your consumer and access keys and secrets. 

When generating your keys, it is important to ensure your application has 'read and write' access. When setting up the application in the Twitter developer portal, click the app settings button in the bottom right corner. Scroll down to the heading labelled "User authentication settings" and click "set up." Scroll down to edit the App Permissions and select the "read and write" option. 

## License :checkered_flag:
This bot is licensed using a GNU V3 license. Feel free to fork modify this repo for use in your own open-source projects. Closed-source use of this repo is not permitted. 


