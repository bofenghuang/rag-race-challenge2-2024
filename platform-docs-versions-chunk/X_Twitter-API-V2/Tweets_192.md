platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query


### Building a query

#### Query limitations

Your queries will be limited depending on which [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) you are using. 

If you have Pro access, your query can be 512 characters long.

If you have Enterprise access, please reach out to your account manager.   
  

#### Operator availability

While most operators are available to any developer, there are several that are reserved for those that have been approved for Enterprise access. We list which access level each operator is available to in the [list of operators](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#list) table using the following labels:

* Core operators: Available when using any [Project](https://developer.twitter.com/en/docs/projects).
* Advanced operators: Available when using a Project with Enterprise access   
     

#### Operator types: standalone and conjunction-required

**Standalone operators** can be used alone or together with any other operators (including those that require conjunction).

For example, the following query will work because it uses the #hashtag operator, which is standalone:

#twitterapiv2

**Conjunction-required** operators cannot be used by themselves in a query; they can only be used when at least one standalone operator is included in the query. This is because using these operators alone would be far too general, and would match on an extremely high volume of Tweets.  

For example, the following queries are not supported since they contain only conjunction-required operators:

has:media  
has:links OR is:retweet

If we add in a standalone operator, such as the phrase "twitter data", the query would then work properly. 

"twitter data" has:mentions (has:media OR has:links)

####   
Boolean operators and grouping

If you would like to string together multiple operators in a single query, you have the following tools at your disposal:

|     |     |
| --- | --- |
| **AND logic** | Successive operators with a space between them will result in boolean "AND" logic, meaning that Tweets will match only if both conditions are met. For example, snow day #NoSchool will match Tweets containing the terms snow and day and the hashtag #NoSchool. |
| **OR logic** | Successive operators with OR between them will result in OR logic, meaning that Tweets will match if either condition is met. For example, specifying grumpy OR cat OR #meme will match any Tweets containing at least the terms grumpy or cat, or the hashtag #meme. |
| **NOT logic, negation** | Prepend a dash (-) to a keyword (or any operator) to negate it (NOT). For example, cat #meme -grumpy will match Tweets containing the hashtag #meme and the term cat, but only if they do not contain the term grumpy. One common query clause is \-is:retweet, which will not match on Retweets, thus matching only on original Tweets, Quote Tweets, and replies. All operators can be negated, but negated operators cannot be used alone. |
| **Grouping** | You can use parentheses to group operators together. For example, (grumpy cat) OR (#meme has:images) will return either Tweets containing the terms grumpy and cat, or Tweets with images containing the hashtag #meme. Note that ANDs are applied first, then ORs are applied. |

**A note on negations**

The operators \-is:nullcast must always be negated.

Negated operators cannot be used alone.

Do not negate a set of operators grouped together in a set of parentheses. Instead, negate each individual operator. For example, instead of using skiing -(snow OR day OR noschool), we suggest that you use skiing -snow -day -noschool. 

####   
Order of operations

When combining AND and OR functionality, the following order of operations will dictate how your query is evaluated.

1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied  
      
    

For example:

* apple OR iphone ipad would be evaluated as apple OR (iphone ipad)
* ipad iphone OR android would be evaluated as (iphone ipad) OR android  
      
    

To eliminate uncertainty and ensure that your query is evaluated as intended, group terms together with parentheses where appropriate. 

For example:

* (apple OR iphone) ipad
* iphone (ipad OR android)  
     

#### Punctuation, diacritics, and case sensitivity

If you specify a keyword or hashtag query with character accents or diacritics, it will match Tweet text that contains both the term with the accents and diacritics, as well as those terms with normal characters. For example, queries with a keyword Diacrítica or hashtag #cumpleaños will match _Diacrítica_ or _#cumpleaños_, as well as with _Diacritica_ or _#cumpleanos_ without the tilde í or eñe.

Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a query with the keyword cumpleaños would only match activities containing the word _cumpleaños_ and would not match activities containing _cumplea_, _cumplean_, or _os_.

All operators are evaluated in a case-insensitive manner. For example, the query cat will match Tweets with all of the following: _cat_, _CAT_, _Cat_.

The [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream) matching behavior acts differently from Tweet counts. When [building a filtered stream rule](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule), know that keywords and hashtags that include accents and diacritics will only match on terms that also include the accent and diacritic, and will not match on terms that use normal characters instead. 

For example, filtered stream rules that include a keyword Diacrítica or hashtag #cumpleaños will only match the terms _Diacrítica_ and _#cumpleaños_, and will not match on _Diacritica_ or _#cumpleanos_ without the tilde í or eñe

#### Specificity and efficiency

When you start to build your query, it is important to keep a few things in mind.

* Using broad, standalone operators for your query such as a single keyword or #hashtag is generally not recommended since it will likely match on a massive volume of Tweets. Creating a more robust query will result in a more specific set of matching Tweets, and will hopefully increase the accuracy of your Tweet counts to help you find more valuable insights. 
    * For example, if your query was just the keyword happy you will likely get anywhere from 200,000 - 300,000 Tweets per day.
    * Adding more conditional operators narrows your results, for example (happy OR happiness) place\_country:GB -birthday -is:retweet
* Writing efficient queries is also beneficial for staying within the characters query length restriction. The character count includes the entire query string including spaces and operators.
    * For example, the following query is 59 characters long: (happy OR happiness) place\_country:GB -birthday -is:retweet  
        

####   
Quote Tweet matching behavior

When using the Tweet counts endpoints, operators will not match on the content from the original Tweet that was quoted, but will match on the content included in the Quote Tweet.

However, please note that [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream) will match on both the content from the original Tweet that was quoted and the Quote Tweet's content.  
 

#### Iteratively building a query

##### Test your query early and often

Getting a query to return the "right" results the first time is rare. There is so much on Twitter that may or may not be obvious at first and the query syntax described above may be hard to match to your desired query.

As you build a query, it is important for you to periodically test it out using one of the [Search Tweet](https://developer.twitter.com/en/docs/twitter-api/tweets/search) endpoints to ensure that the Tweets that are matching your query are relevant to your use case.

For this section, we are going to start with the following query and adjust it based on the results that we receive during our test: 

happy OR happiness

##### Use results to narrow the query

As you test the query with Search Tweets, you should scan the returned Tweets to see if they include the data that you are expecting and hoping to receive. Starting with a broad query and a superset of Tweet matches allows you to review the result and narrow the query to filter out undesired results.  

When we tested the example query, we noticed that we were getting Tweets in a variety of different languages. In this situation, we want to only receive Tweets that are in english, so we’re going to add the lang: operator:

(happy OR happiness) lang:en

The test delivered a number of Tweets wishing people a happy birthday, so we are going to add \-birthday as a negated keyword operator. We also want to only receive original Tweets, so we’ve added the negated \-is:retweet operator:

(happy OR happiness) lang:en -birthday -is:retweet

##### Adjust for inclusion where needed

If you notice that you are not receiving data via Search Tweets that you expect and know that there are existing Tweets that should return, you may need to broaden your query by removing operators that may be filtering out the desired data. 

For our example, we noticed that there were other Tweets in our personal timeline that expressed the emotion that we are looking for and weren’t included in the test results. To ensure we have greater coverage, we are going to add the keywords, excited and elated.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet

##### Adjust for popular trends/bursts over the time period

Trends come and go on Twitter quickly. Maintaining your query should be an active process. If you plan to use a query for a while, we suggest that you periodically check in on the data that you are receiving to see if you need to make any adjustments.

In our example, we notice that we started to receive some Tweets that are wishing people a “happy holidays”. Since we don’t want these Tweets included in our results, we are going to add a negated \-holidays keyword.

(happy OR happiness OR excited OR elated) lang:en -birthday -is:retweet -holidays 

Once you've properly tested and iterated upon your query, you can start sending it with the Tweet counts endpoints to start to receive just the volume of Tweets rather than the full Tweet payloads.