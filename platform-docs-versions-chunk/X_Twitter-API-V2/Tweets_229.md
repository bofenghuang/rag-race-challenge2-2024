platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule


### Building a rule

#### Rule limitations

Limits on the number of rules will depend on which [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) is applied to your [Project](https://developer.twitter.com/en/docs/projects).

You can see how these limits apply via the [filtered stream introduction](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream) page.  
 

#### Operator availability

While most operators are available to any developer, there are several that are reserved for those that have been approved for Basic, Pro, or Enterprise access levels. We list which [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) each operator is available to in the [list of operators](#list) table using the following labels:

* **Essential operators:** Available when using any access level.
* **Elevated operators:** Available when using a Project with Pro, or Enterprise access.  
     

#### Operator types: standalone and conjunction-required

**Standalone operators** can be used alone or together with any other operators (including those that require conjunction).

For example, the following rule will work because it uses the #hashtag operator, which is standalone:

#twitterapiv2

**Conjunction required** operators cannot be used by themselves in a rule; they can only be used when at least one standalone operator is included in the rule. This is because using these operators alone would be far too general, and would match on an extremely high volume of Tweets.  

For example, the following rules are not supported since they contain only conjunction required operators:

has:media  
has:links OR is:retweet

If we add in a standalone operator, such as the phrase "twitter data", the rule would then work properly. 

"twitter data" has:mentions (has:media OR has:links)

####   
Boolean operators and grouping

If you would like to string together multiple operators in a single rule, you have the following tools at your disposal:

|     |     |
| --- | --- |
| **AND logic** | Successive operators **with a space between them** will result in boolean "AND" logic, meaning that Tweets will match only if both conditions are met. For example, snow day #NoSchool will match Tweets containing the terms snow and day and the hashtag #NoSchool. |
| **OR logic** | Successive operators with OR between them will result in OR logic, meaning that Tweets will match if either condition is met. For example, specifying grumpy OR cat OR #meme will match any Tweets containing at least the terms grumpy or cat, or the hashtag #meme. |
| **NOT logic, negation** | Prepend a dash (-) to a keyword (or any operator) to negate it (NOT). For example, cat #meme -grumpy will match Tweets containing the hashtag #meme and the term cat, but only if they do not contain the term grumpy. One common rule clause is \-is:retweet, which will not match on Retweets, thus matching only on original Tweets, Quote Tweets, and replies. All operators can be negated, but negated operators cannot be used alone. |
| **Grouping** | You can use parentheses to group operators together. For example, (grumpy cat) OR (#meme has:images) will return either Tweets containing the terms grumpy and cat, or Tweets with images containing the hashtag #meme. Note that ANDs are applied first, then ORs are applied. |

**A note on negations**

All operators can be negated except for sample:, and \-is:nullcast must always be negated. Negated operators cannot be used alone.

Do not negate a set of operators grouped together in a set of parentheses. Instead, negate each individual operator.

For example, instead of using skiing -(snow OR day OR noschool), we suggest that you use skiing -snow -day -noschool. 

####   
Order of operations

When combining AND and OR functionality, the following order of operations will dictate how your rule is evaluated.

1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied  
      
    

For example:

* apple OR iphone ipad would be evaluated as apple OR (iphone ipad)
* ipad iphone OR android would be evaluated as (iphone ipad) OR android  
      
    

To eliminate uncertainty and ensure that your rule is evaluated as intended, group terms together with parentheses where appropriate. 

For example:

* (apple OR iphone) ipad
* iphone (ipad OR android)  
     

#### Punctuation, diacritics, and case sensitivity

If you specify a keyword or hashtag rule with character accents or diacritics, it will match Tweets that contain the exact word with proper accents or diacritics, but not those that have the proper letters, but without the accent or diacritic. 

For example, rules with the keyword diacrítica or hashtag #cumpleaños will match Tweets that contain _diacrítica_ or _#cumpleaños_ because they include the accent or diacritic. However, these rules will not match Tweets that contain _Diacritica_ or _#cumpleanos_ without the tilde í or eñe.  
  

Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a rule with the keyword _cumpleaños_ would only match Tweets containing the word _cumpleaños_ and would not match Tweets containing _cumplea_, _cumplean_, or _os_.

All operators are evaluated in a case-insensitive manner. For example, the rule cat will match all of the following: _cat_, _CAT_, _Cat_.

The [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search) matching behavior acts differently from filtered stream. When [building a Search Tweets query](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-rule), know that keywords and hashtags that include accents or diacritics will match both the term with the accents and diacritics, as well as with normal characters. 

For example, Search Tweets queries that include a keyword Diacrítica or hashtag #cumpleaños will match both _Diacrítica_ and _#cumpleaños_, as well as _Diacritica_ or _#cumpleanos_ without the tilde í or eñe.

#### Specificity and efficiency

When you start to build your rule, it is important to keep a few things in mind.

* Using broad, standalone operators for your rule such as a single keyword or #hashtag is generally not recommended since it will likely match on a massive volume of Tweets. Creating a more robust rule will result in a more specific set of matching Tweets, and will hopefully reduce the amount of noise in the payload that you will need to sift through to find valuable insights. 
    * For example, if your rule was just the keyword happy you will likely get anywhere from 200,000 - 300,000 Tweets per day.
    * Adding more conditional operators narrows your search results, for example (happy OR happiness) place\_country:GB -birthday -is:retweet
* Writing efficient rules is also beneficial for staying within the characters rule length restriction. The character count includes the entire rule string including spaces and operators.
    * For example, the following rule is 59 characters long: (happy OR happiness) place\_country:GB -birthday -is:retweet  
        

####   
Quote Tweet matching behavior

When using the filtered stream endpoints, operators will match on both the content from the original Tweet that was quoted, as well as the content included in the Quote Tweet.

However, please note that the [Search Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/search) endpoints will not match on the content from the original Tweet that was quoted, but will match on the Quote Tweet's content.  
  

#### Iteratively building a rule

##### Test your rule early and often

Getting a rule to return the "right" results the first time is rare. There is so much on Twitter that may or may not be obvious at first and the rule syntax described above may be hard to match to your desired search. As you build a rule, it is important for you to periodically test it out with the stream endpoint to see what data it returns. You can also test with one of the [Search Tweet](https://developer.twitter.com/en/docs/twitter-api/tweets/search) endpoints, assuming the operators that you are using are also available via that endpoint. 

For this section, we are going to start with the following rule and adjust it based on the results that we receive during our test: 

happy OR happiness

##### Use results to narrow the rule

As you test the rule, you should scan the returned Tweets to see if they include the data that you are expecting and hoping to receive. Starting with a broad rule and a superset of Tweet matches allows you to review the result and narrow the rule to filter out undesired results.  

When we tested the example rule, we noticed that we were getting Tweets in a variety of different languages. In this situation, we want to only receive Tweets that are in english, so we’re going to add the lang: operator:

(happy OR happiness) lang:en

The test delivered a number of Tweets wishing people a happy birthday, so we are going to add \-birthday as a negated keyword operator. We also want to only receive original Tweets, so we’ve added the negated \-is:retweet operator:

(happy OR happiness) lang:en -birthday -is:retweet

##### Adjust for inclusion where needed

If you notice that you are not receiving data that you expect and know that there are existing Tweets that should return, you may need to broaden your rule by removing operators that may be filtering out the desired data. 

For our example, we noticed that there were other Tweets in our personal timeline that expressed the emotion that we are looking for and weren’t included in the test results. To ensure we have greater coverage, we are going to add the keywords, excited and elated.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet

##### Adjust for popular trends/bursts over the time period

Trends come and go on Twitter quickly. Maintaining your rule should be an active process. If you plan to use a single rule for a while, we suggest that you periodically check in on the data that you are receiving to see if you need to make any adjustments.

In our example, we notice that we started to receive some Tweets that are wishing people a “happy holidays”. Since we don’t want these Tweets included in our results, we are going to add a negated \-holidays keyword.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet -holidays 

#### Adding and removing rules

You will be using the [POST /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules) endpoint when both adding and deleting rules from your stream.

To add one or more rule to your stream, submit an add JSON body with an array that contains the value parameter including the rule, and the optional tag parameter including free-form text that you can use to [identify which returned Tweets match this rule](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets). 

For example, if you were trying to add a set of rules to your stream, your cURL command might look like this:

      `curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \ -H "Content-type: application/json" \ -H "Authorization: Bearer $ACCESS_TOKEN" -d \ '{   "add": [     {"value": "cat has:media", "tag": "cats with media"},     {"value": "cat has:media -grumpy", "tag": "happy cats with media"},     {"value": "meme", "tag": "funny things"},     {"value": "meme has:images"}   ] }'`
    

Similarly, to remove one or more rules from your stream, submit a delete JSON body with the array of that contains the id parameter including the rule IDs that you would like to delete.

For example, if you were trying to remove a set of rules from your stream, your cURL command might look like this:  

      `curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \   -H "Content-type: application/json" \   -H "Authorization: Bearer $ACCESS_TOKEN" -d \   '{     "delete": {       "ids": [         "1165037377523306498",         "1165037377523306499"       ]     }   }'`
    

We have sample code in different languages available via our [Github](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/master/Filtered-Stream).   
  

#### Rule examples

##### Tracking a natural disaster

The following rule matched on Tweets coming from weather agencies and gauges that discuss Hurricane Harvey, which hit Houston in 2017. Notice the use of the [matching rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets) tag, and the JSON format that you will need to use when submitting the rule to the [POST /2/tweets/search/stream/rules endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules).

      `{             "value": "-is:retweet has:geo (from:NWSNHC OR from:NHC_Atlantic OR from:NWSHouston OR from:NWSSanAntonio OR from:USGS_TexasRain OR from:USGS_TexasFlood OR from:JeffLindner1)",             "tag": "theme:info has:geo original from weather agencies and gauges"         }`
    

##### Reviewing the sentiment of a conversation

The next rule could be used to better understand the sentiment of the conversation developing around the hashtag, _#nowplaying_, but only from Tweets published within North America.

      `{             "value": "#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place_country:US OR place_country:MX OR place_country:CA) -horrible -worst -sucks -bad -disappointing",             "tag": "#nowplaying positive"         },         {             "value": "#nowplaying (horrible OR worst OR sucks OR bad OR disappointing) (place_country:US OR place_country:MX OR place_country:CA) -happy -exciting -excited -favorite -fav -amazing -lovely -incredible",             "tag": "#nowplaying negative"         }`
    

##### Find Tweets that relate to a specific Tweet annotation

This rule was built to search for original Tweets that included an image of a pet that is not a cat, where the language identified in the Tweet is Japanese. To do this, we used the context: operator to take advantage of the [Tweet annotation](https://developer.twitter.com/en/docs/twitter-api/annotations) functionality. We first used the [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup) endpoint and the tweet.fields=context\_annotations fields parameter to identify which domain.entity IDs we need to use in our query:

* Tweets that relate to cats return **domain** 66 (Interests and Hobbies category) with entity 852262932607926273 (Cats). 
* Tweets that relate to pets return **domain** 65 (Interests and Hobbies Vertical) with entity 852262932607926273 (Pets).   
     

Here is what the rule would look like:

      `        {             "value": "context:65.852262932607926273 -context:66.852262932607926273 -is:retweet has:images lang:ja",             "tag": "Japanese pets with images - no cats"         }`