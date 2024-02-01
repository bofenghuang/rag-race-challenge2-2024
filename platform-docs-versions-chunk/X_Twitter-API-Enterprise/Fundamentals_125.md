platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule


###   
Boolean Syntax

The examples in the previous section, utilized various types of boolean logic and grouping. See the table below for additional detail regarding the syntax and requirements for each.

|     |     |     |
| --- | --- | --- |
| **Logic type** | **Operator syntax** | Description |
| AND | social data | Whitespace between two operators results in AND logic between them  <br>  <br>Matches activities containing both keywords ("social", "data").  <br>  <br>**Do not use AND explicitly in your rule. Only use whitespace. An explicit AND will be treated like a regular keyword.** |
| OR  | social OR data | To OR together two operators, insert an all-caps OR, enclosed in whitespace between them  <br>  <br>Matches activities with EITHER keyword ("social" OR "data")  <br>  <br>Note that if you combine OR and AND functionality in a single rule, you should understand the order of operations described in our "[Order of operations](#OrderOfOperations)" section, and consider grouping non-negated operators together using parentheses as described below to ensure your rule behaves as expected.  <br>  <br>You must use upper-case "OR" in your rule. Lower-case 'or' will be treated as a regular keyword. |
| NOT | social data  <br>\-apple -android -phone | Insert a `-` character immediately in front of the operator or group of operators.  <br>  <br>The example rule shown matches activities containing keyword "social", but excludes those which contain the keyword "data."  <br>  <br>Negated ORs are not allowed where the rule would request "everything in the firehose except the negation." For example, `apple OR -ipad` is invalid because it would match all activities except those mentioning "ipad". |
| Grouping | (social OR data) -twitterdev -twitterapi | Parentheses around multiple operators create a functional "group".<br><br>Groups can be connected to clauses in the same manner as an individual clause via whitespace (AND) or ORs. However, note that it is a best practice to not group together negations by applying the negating \- to the entire group. Instead, you should negate each individual operator, stringing them together via whitespace (AND). <br><br>For example, instead of using \-(iphone OR imac OR macbook), use the following: \-iphone -imac -macbook  <br>  <br>Grouping is especially important where a single rule combines AND and OR functionality, due to the order of operations used to evaluate the rule. See below for more details. |

**Please note:** that operators may be either positive or negative.

**Positive Operators** define what you want to **include** in the results. E.g. the `has:hashtags` operator says “I want activities containing hashtags.”

**Negative Operators** define what you want to **exclude** from the results, and are created by using the Boolean NOT logic described above. For example, `-has:hashtags` says “Exclude any activities containing hashtagss, even if they otherwise match my rule.”

Premum operator products have no restriction on the number of positive and negative clauses, subject to a maximum length of 2,048 characters.  
 

#### Order of Operations

When combining AND and OR functionality in a single rule, the following order of operations will dictate how your rule is evaluated.

1. Operators connected by AND logic are combined first
2. Then, operators connected with OR logic are applied

**Example:**

* `apple OR iphone ipad` would be evaluated as `apple OR (iphone ipad)`
* `ipad iphone OR android` would be evaluated as `(iphone ipad) OR android`

To eliminate uncertainty and ensure that your rules are evaluated as intended, group terms together with parentheses where appropriate. For example:

* `(apple OR iphone) ipad`
* `iphone (ipad OR android)`

####   
Punctuation, Diacritics, and Case Sensitivity

If you specify a keyword or hashtag rule with character accents or diacritics for enterprise operators, it will match Tweet text honoring the diacritics (hashtags or keywords). Rule with a keyword `Diacr**í**tica` or hashtag `#cumplea**ñ**os` will match "Diacr**í**tica" or "#cumplea**ñ**os" but not "Diacritica" or "#cumpleanos" without the tilde **í** or **eñe**.

Characters with accents or diacritics are treated the same as normal characters and are not treated as word boundaries. For example, a rule of cumplea**ñ**os would only match activities containing the word cumpleaños and would not match activities containing cumplea, cumplean, or os.

All operators are evaluated in a case-insensitive manner. For example, the rule `Cat` will match all of the following: "cat", "CAT", "Cat".

####   
PowerTrack rule tags

As described on our "[Matching rules](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules)" page, each rule may be created with a tag. These tags have no effect on filtering, but can be used to create logical groupings of rules within your app. Each rule may have only one tag, with a maximum of 255 characters. Tags are included with the JSON formatted rule at the time of creation via the API, as described on our "Matching rules" page.

####   
Putting Rules in JSON Format

In order to add or delete a rule from a stream via the API, the rules must utilize JSON format. Essentially, this requires putting each rule into the following structure:

`{"value":"insert_rule_here"}`

**Rules with double-quotes**

If the rule contains double-quote characters (`“`) associated with exact-match or other operators, they must be escaped using a backslash to distinguish them from the structure of the JSON format.

`"social data" @twitterdev`

The JSON formatted rule would be:

`{"value":"\"social data\" @twitterdev"}`

**Rules with double-quote string literals**

To include a double-quote character as a string literal within an exact-match, it must be double-escaped. For example, for a rule matching on the exact phrase "Toys “R” Us", including the double-quotes around "R", the plain-text representation of this would look like the following:

`"Toys \"R\" Us"`

Translating this to JSON format, you should use the following structure:

`{"value":"\"Toys \\\"R\\\" Us\""}`

**Rules with Tags**

To include an optional tag with your rule, as described above, simply include an additional `tag` field with the rule value.

`{"value":"\"social data\" @twitterdev","tag":"RULE-TAG-01"}`

**Formatting for API Requests**

When adding or deleting rules from the stream via the API, multiple JSON formatted rules should be comma delimited, and wrapped in a JSON “rules” array, as shown below:

`{"rules":[{"value":"from:twitterdev"},{"value":"\social data\" @twitterdev","tag":"RULE-TAG-01"}]}`

####   
Operators that match Quote Tweets

When using the [PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api) and [Historical PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/historical-powertrack-api), the operators below will match on content from both the original Tweet that was quoted and the new Quote Tweet.

However, if you are using the [Search API](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api), these operators will only match the contents of the Quote Tweet, and will not match on any content from the original Tweet that was quoted.

* `Keywords`
* `Phrases`
* `Proximity`
* `#hashtags`
* `@mentions`
* `$cashtags`
* `url:`
* `url_contains:`
* `has:links`
* `has:mentions`
* `has:hashtags`
* `has:media`
* `has:symbols`
* `is:quote`
* `is:reply`