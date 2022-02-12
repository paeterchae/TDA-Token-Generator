# TDA-Token-Generator
 
TDA Token Generator allows users to generate a *token.json* file that can be used to securely authenticate their TD Ameritrade accounts and gain access to TDA's API endpoints. For users looking to utilize the **Trade Alert Bot**, the instructions below outline both offline and online methods to generate a token with limited scope such that the bot only gains access to the **minimum permissions necessary** to alert trades. This is to ensure that malevolent actors cannot use the token file or the bot to place trades or move money on connected accounts.

## TDA Developer Account and App Creation
Both methods require the creation of a TDA Developer Account and a subsequent App to create an API KEY.
1. Register for a developer account [here](https://developer.tdameritrade.com/apis).
2. To create a new app, go to [My Apps](https://developer.tdameritrade.com/user/me/apps) and select **Add a new App**.
3. Complete the fields with the following and select **Create App**:
    * **App Name**: TradeAlert
    * **Callback URL**: https://localhost
    * **What is the purpose of your application?** Send live updates of trading orders to discord channel
    * **Order Limit**: 0 
4. Your **Consumer Key** that you generate will be your API KEY.

## Restrictions
Due to the limitations of the TD Ameritrade Streaming API, specific conditions must be met for the Trade Alert Bot to successfully connect to an account.
1. The account used must not have any linked accounts. All linked accounts must first be unlinked through TD Ameritrade before proceeding.
2. The account used to authenticate and generate the token file must be the same account as the one being connected to the Trade Alert Bot.
3. Tokens must be regenerated every 90 days. The Trade Alert Bot is programmed to automatically do this starting 85 days after token generation, but **this only occurs if a successful API call is made**. This means that the Trade Alert Bot must be actively used in Discord at least once between days 85-90. If this condition is not met, the bot will fail and a new token must be manually generated and uploaded to restart it.

## Offline Method
This method is easiest, but requires you to run Python locally on your machine.
1. Open terminal.
2. Type *git clone https://github.com/stonkpab/TDA-Token-Generator.git*
3. Type *cd TDA-Token-Generator*
4. Plug in TDA API key in .env file
5. Type *pip install requirements-test.txt*
6. Type *python3 bot.py*
7. Follow instructions written in terminal
   * **IMPORTANT**: Add *&scope=AccountAccess* to the end of the generated link
8. Outputted token.json is your TDA token.

## Online Method
This method is best for those who do not want to download anything or are unfamiliar with using terminal.
1. Go to your auth URL by filling in your API KEY into the example link below (Replace **YOUR_API_KEY**).

    https://auth.tdameritrade.com/auth?response_type=code&redirect_uri=https://localhost&client_id=YOUR_API_KEY%40AMER.OAUTHAP&scope=AccountAccess
2. Authenticate with the TD Ameritrade account you plan on streaming trades from. This will lead you to an error page. Copy the part that comes after "code=" in the address bar.
3. Paste the part you copied [here](https://www.urldecoder.org/), decode the data, and copy the decoded data.
4. Paste the decoded data [here](https://developer.tdameritrade.com/authentication/apis/post/token-0) as the value for the **code** field.
5. Complete the fields with the following and press **Send**.
    * **grant_type**: authorization_code
    * **refresh_token**: (leave empty)
    * **access_type**: offline
    * **client_id**: **YOUR_API_KEY**@AMER.OAUTHUP
    * **redirect_uri**: https://localhost
6. Click on **Response** and copy the token (should look like this).
```
{
  "creation_timestamp": 1644624039,
  "token": {
    "access_token": "abcdefg",
    "scope": "AccountAccess",
    "expires_in": 1800,
    "token_type": "Bearer",
    "expires_at": 1644634062,
    "refresh_token": "abcdefg"
  }
}
```
7. Create a file named **token.json** and paste the token contents in the file.
