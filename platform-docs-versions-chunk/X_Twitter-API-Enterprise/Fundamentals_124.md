platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule


### Building rules and queries 

**Keyword match**

Keyword matches are similar to queries in a search interface. For example, the following enterprise operator rule would match activities with the term "social" in the text body.

`social`

**ANDing terms with white space**

Adding another keyword is the same as adding another requirement for finding matches. For example, this rule would only match activities where both "social" and "media" were present in the text, in either order – _having a space between terms operates as boolean AND logic_. If you include an explicit AND in your rule, it will rejected by the rules endpoint.

`social media`

**ORing terms with upper-case OR**

Many situations actually call for boolean OR logic, however. This is easily accomplished as well. _Note that the OR operator must be upper-case and a lower-case ‘or’ will be treated as a regular keyword._

`social OR data`

**Negating terms**

Still other scenarios might call for excluding results with certain keywords (a boolean NOT logic). For instance, activities with ‘happy’, but excluding any with ‘birthday’ in the text.

`social -personality`

**Grouping with parentheses**

These types of logic can be combined using grouping with parentheses, and expanded to much more complex queries.

`(social OR data) (academic OR research) -personality -information -university`

This is just the beginning though – while the above examples rely simply on tokenized matching for keywords, enterprise products also offer operators to perform different types of matching on the text.

**Exact match**

`"social media research"`

**Substring match**

`contains:info`

**Proximity match**

`"social media research"~3`

  
Further, other operators allow you to filter on unique aspects of social data, besides just the text. 

**The user who is posting a Tweet**

`from:twitterdev`

**Geo-tagged Tweets within 10 miles of Pearl St. in Boulder, CO, United States**

`point_radius:[-105.27346517 40.01924738 10.0mi]`

**Putting it all together**

These can be combined with text filters using the same types of logic described above.

`(social OR data) (academic OR research OR "social media research") point_radius:[-105.27346517 40.01924738 10.0mi] lang:en -personality -information -university`