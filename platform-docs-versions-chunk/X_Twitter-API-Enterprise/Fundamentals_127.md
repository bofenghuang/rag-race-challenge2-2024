platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators


## Enterprise operators

Below are the operators available with PowerTrack and Historical PowerTrack. A subset of these are available with the 30-Day and Full-Archive search APIs. See [this table](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product) for a product-by-product list of available operators. 

**Operator**  

Descriptionkeyword  

Matches a keyword within the text body or URL of a Tweet. Keywords must start with either a digit (0-9) or any non-puncutation character.  Keyword matching is a tokenized match, meaning that your keyword will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol, and separator Unicode basic plane characters.  To match strings containing punctuation (for example, coca-cola), symbol, or separator characters, you must use a quoted "exact phrase match".  
  
Example:  
(social OR pizza OR wildfire) -planet  
  
**Note:** With the Search API, accented and special characters are normalized to standard latin characters, which can change meanings in foreign languages or return unexpected results:  
For example, "músic" will match “music” and vice versa.   
For example, common phrases like "Feliz Año Nuevo!" in Spanish, would be indexed as "Feliz Ano Nuevo", which changes the meaning of the phrase.

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.  

emoji  
Matches an emoji within the body of a Tweet. Emojis are a tokenized match, meaning that your emoji will be matched against the tokenized text of the Tweet body – tokenization is based on punctuation, symbol/emoji, and separator Unicode basic plane characters. For example, a Tweet with the text “I like 🍕” would be split into the following tokens: I, like, 🍕. These tokens would then be compared to the emoji used in your rule. Note that if an emoji has a variant, you must use “quotations” to add to a rule.  
  
Example:  
(🍕 OR 💜 OR 🐢) -🤖  
"exact phrase match"  

Matches an exact phrase within the body of a Tweet.

Example:  
("social media" OR "developer.twitter.com" OR "wildfire911" OR "coca-cola") -"planet earth"

**Note:** In 30 Day Search and Full Archive Search, punctuation is not tokenized and is instead treated as whitespace.   
For example, quoted “#hashtag” will match “hashtag” but not #hashtag (use the hashtag # operator without quotes to match on actual hashtags)  
For example, quoted “$cashtag” will match “cashtag” but not $cashtag (use the cashtag $ operator without quotes to match on actual cashtags)

**Note:** This operator will match on both URLs and unwound URLs within a Tweet.