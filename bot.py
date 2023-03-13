import requests
import tweepy
import time
import json
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

## Create function to call Keplr Wallet API to get thumbnail
thumbnail = requests.get("https://wallet.keplr.app/api/validator_thumbnails?ids=AE4C403A6E7AA1AC,E5F274B870BDA01D,00B79D689B7DC1CE,975D494265B1AC25,3A7D5C9B0B88BEA1,48608633F99D1B60,045D374A62F15B56,3804A3D13B6CB379,CA9AC67C3BF42517,90B597A673FC950E,7C88A757E65A5445,EBB03EB4BB4CFCA7,7BDD4C2E94392626,0878BA6BE556C132,C47845226662AF47,3EB2AEED134D7138,D0D8B80F1C5C70B5,209E3458ADC6CAF5,0BC47B3228CBF46C,D16E26E5C8154E17,06E24C7678282B53,3E38E52A12F94561,28DC4101DA38C22C,535BF8D68742ACED,67A577430DBBCEE0,6408AA029ADBE364,26FE476C84A3C760,CC434B6FE536F51B,2861F5EE06627224,8957C5091FBF4192,268AE2FE71E9E7C4,DCB176E79AE7D51F,8A9FC930E1A980D6,436039F82528A43A,F12B081334CBE0C6,CD80FCB702D70807,DE810BE47E3B73B3,A57DAB9B09C7215D,CF0852DD298E2B0D,5736C325251A8046,4801FCDCD4F93E9B,47434737FEC2418A,E2A5772A111FD119,5992A6D423A406D6,8E92184569CD8E2D,0A6AF02D1557E5B4,9AE70F9E3EDA8956,5F1D6AC7EA588676,6386E8C1B6217AC2,35892AC552B8A0A8,165F85FC0194320D,3999DA33020A4DBC,6783E9F948541962,FA260EE7A0113432,AD3CDBC91802F94A,F87ADDB700C0CC94,1ECD13F96C55C0CD,679281030DD1209A,D75509198CE782A6,29A97D4100A83471,8687EB49D3AC9208,ADBDB0178E4441BE,DD06F013A474ACA3,1C32EF4035953E8B,DA08751C2062AB36,C7449E61C271EAA8,C92C6965D89F07A3,4062E136FF6C8968,0B5217ACAE18F4C9,9C7571030BEF5157,103DCE407C9F1D13,D372724899D1EDC8,2ABCBF8F9F31AF0E,51468B615127273A,4D3303E20A4D2C32,913CE38447233C01,609F83752053AD57,5A8AB49CF5CAAF3C,FD3702E722561505,CC806AFFDB2EE85A,216E0EE1BA80B5F8,87D9921253A2A9EB,FEF740F1760E1B56,9203983F91296B66,A2EA7DE76AD57E1A,C46C8329BB5F48D8,9A516A1CD4116BBF,7F82E4F0CAA26298,5CCA4F526B9F85DA,06B033BAC39DA21C,94FEC9A766EF8D04,A2879F08F59FB0AF,63575EE3F0F9FAFC,55387C0472199D52,55A5F88B4ED52D3E,C5C28A947096C28A,F74595D6D5D568A2,55B2C411EE64C03A,B4750D7ECB3F0409,DA413860B22A8E07,B41FCF161C4B971B,F2E67996F3D5EB16,909A480D5643CCC5,11A2797A6DD3873D,F10E3CDCBC4EA7AA,E73AFD8985423B14,D41C757E7F05563FC04351B41E09665F32FE7217,6696D60A73064DFE,125E6FE219457130,805F39B20E881861,09A303A2C724C59,F422F328C14AFBFA,2E3A8285E6B547B2,536585A71903C50F,44937E3DA9AA699A,70C162B0473634FD,1326A75B9148A214,8D6FC89A2E9A7FC7,D540D0234B3AE1B8,0CE19EE3E4BA48E5,1441B829AD71D8F4,DF1CDD6E03CCF372,E308F774D80FF40B,8BD21C9C536D6CBF,146F545F37D34202,A0C8B5A2BDDCA82B,5F406D7064437F89,5505D3E11EF42968,86A0F841E24F3C34,4E0CE8E709527EE0,DEF3590B1DCD96A4,FD161E9548A427C9,2CC4D67B2136C051,3F5BD795E6AB49AC,355613DDE80039C8,833F4BCC70748155,1510797E867F484E,7ACD3320CCADD897,C8992BB62C009B9F,D0D9D1C2AEB79C5B,DFEAAB98E8D0975B,74D3AF53635231D9,6257A55EA42BA680,E0A6A3980E464A66,70D77FD98E48B033,C7D6DBE2CB576363,EB3470949B3E89E2,85130F5D06D9DC5E,9BDCB96F2AB4EAA9,A3431CED2751636A,3C91979AF36E303E,3912AE47B45446D7,059BCF656623D0BE,94F50BA69A2BEFEA,BA341405E1973689,AB99C8D824487B05,4700D12228CC5EB5,7AAAA066B64C3034,0EE0E1ADCAEC1633,38172502B043D302,FF4B91B50B71CEDA,26FA2B24F46A98EF,3D7812E90AFB1548,8265DEAF50B61DF7,EC771B7A05CDF1D4,834d3ed959fe610fa2154c34ecdd85340e88a1ae,716F93BF335CF0B0,EC3443CC6E038CFA,F8FCC108B0120E16,562B310A60D8A06D,69A46F39FB01F4D4,2CB281A714F6133B,BEAC09B6FE7F908B,3D6E2861B47F2F9F,6CE4A2AB30E12FB6,AD6C05DA12E42B70,48CE867E6AB5ED72,A15273DFFD11E62E,EDEA30F3AD071CD2,654899A548A41038,EBBAB54C972A579A,3EB183235B56FFFD,2C12B61930DF3586,59C635D1CD02FEEC,EC3443CC6E038CFA,E831E23101940CAC,F40C96DBD7D48202,4006E2C214ACAA86,E46A1AC121BEAD77,86AFEC0A2EB34700,CE1BB434CBA5182E,834d3ed959fe610fa2154c34ecdd85340e88a1ae,29639AC899E40A48,56FCAA9342EBA2D5,D55266E648F3F70B,A0E5C01E81CA39B6,27FD74457A21B020,D32EF9EE3E16B2A3,A2E180C6914F7F87,35191C15DC57FC10,C5B2D58B41BEB336,03CB5B59890F30A3,28B672FCE6BBD562,C47845226662AF47,A713F5C07C453731,9B2EB22C7DAC8684,812E82D12FEA3493,xyz,0AA6F85BA53FD248,862C5270EE4D7EB6,CE33078D690BAC6A,FFB0AA51A2DF5954,C5337EB8B55DFA0C,86AC709C230079D0,C0522DF992B0C407,9334AA066991F571,0AB0957AA5A01AD1,E3543DBAC0CBEB98,9E31CFA37DA22B31,34C75DF5D1C3133C,008D9883E39DBD65,%20,6DE451B1AF56C274,FA,ASKDJKSJAD")
pics = thumbnail.json()

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
    project_name = record['PROJECT_NAME']
    print(project_name)
    memo = record['MEMO']
    link_tx = 'https://www.mintscan.io/osmosis/txs'+tx_id
    link_prop = 'https://www.mintscan.io/osmosis/proposals/'+str(proposal_id)
    if vote_option == 1: 
        vote = 'voted yes'
    elif vote_option == 2: 
        vote = 'abstained'
    elif vote_option == 3: 
        vote = 'voted no'
    else: 
        vote = 'voted no with veto'

    img = 'images/{}.jpg'.format(project_name)
        
    time.sleep(10)
    # Set the payload (i.e. the body of the tweet)
    media = api.media_upload(img)
    payload = f"{label} {vote} on proposal {proposal_id} with the following rational:\n{memo}.\n{link_prop}"
    api.update_status(status=payload, media_ids=[media.media_id])
    # Update the status of the Twitter Bot 
    #api.update_status(payload)
    print('Done!') ## This is a console log 