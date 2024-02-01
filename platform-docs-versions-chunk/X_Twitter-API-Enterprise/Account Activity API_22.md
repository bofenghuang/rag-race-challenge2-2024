platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks


# Defines a route for the GET request
@app.route('/webhooks/twitter', methods=\['GET'\])
def webhook\_challenge():

  # creates HMAC SHA-256 hash from incomming token and your consumer secret
  sha256\_hash\_digest = hmac.new(TWITTER\_CONSUMER\_SECRET, msg=request.args.get('crc\_token'), digestmod=hashlib.sha256).digest()

  # construct response data with base64 encoded hash
  response = {
    'response\_token': 'sha256=' + base64.b64encode(sha256\_hash\_digest)
  }

  # returns properly formatted json response
  return json.dumps(response)

#### Example JSON response:  

With the route defined as above your webapp should return a response similar to below when navigating to https://your-app-domain/webhooks/twitter?crc\_token=foo in your web browser.

{
  "response\_token": "sha256=x0mYd8hz2goCTfcNAaMqENy2BFgJJfJOb4PdvTffpwg="
}

#### Other examples:

* [HERE](https://github.com/twitterdev/account-activity-dashboard/blob/master/helpers/security.js) is an example CRC response method written in Node/JS.
* [HERE](https://github.com/twitterdev/SnowBotDev/blob/master/app/controllers/snow_bot_dev_app.rb) is an example CRC response method written in Ruby (see the _generate\_crc\_response_ and the /GET route that receives CRC events).