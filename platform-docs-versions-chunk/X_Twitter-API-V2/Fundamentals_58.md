platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/annotations/overview


### Context

_Last updated: June 2022_

Context annotations are delivered as a context\_annotations field in the payload. These annotations are inferred based on semantic analysis (keywords, hashtags, handles, etc) of the Tweet text and result in domain and/or entity labels. Context annotations can yield one or many domains. At present, we’re using a list of 80+ domains reflected in the table below.

|     |     |     |     |
| --- | --- | --- | --- |
| 3: TV Shows<br><br>4: TV Episodes<br><br>6: Sports Events<br><br>10: Person<br><br>11: Sport<br><br>12: Sports Team<br><br>13: Place<br><br>22: TV Genres<br><br>23: TV Channels<br><br>26: Sports League<br><br>27: American Football Game<br><br>28: NFL Football Game<br><br>29: Events<br><br>31: Community<br><br>35: Politicians<br><br>38: Political Race<br><br>39: Basketball Game<br><br>40: Sports Series<br><br>43: Soccer Match<br><br>44: Baseball Game<br><br>45: Brand Vertical | 46: Brand Category<br><br>47: Brand<br><br>48: Product<br><br>54: Musician<br><br>55: Music Genre<br><br>56: Actor<br><br>58: Entertainment Personality<br><br>60: Athlete<br><br>65: Interests and Hobbies Vertical<br><br>66: Interests and Hobbies Category<br><br>67: Interests and Hobbies<br><br>68: Hockey Game<br><br>71: Video Game<br><br>78: Video Game Publisher<br><br>79: Video Game Hardware<br><br>83: Cricket Match<br><br>84: Book<br><br>85: Book Genre<br><br>86: Movie<br><br>87: Movie Genre<br><br>88: Political Body | 89: Music Album<br><br>90: Radio Station<br><br>91: Podcast<br><br>92: Sports Personality<br><br>93: Coach<br><br>94: Journalist<br><br>95: TV Channel \[Entity Service\]<br><br>109: Reoccurring Trends<br><br>110: Viral Accounts<br><br>114: Concert<br><br>115: Video Game Conference<br><br>116: Video Game Tournament<br><br>117: Movie Festival<br><br>118: Award Show<br><br>119: Holiday<br><br>120: Digital Creator<br><br>122: Fictional Character<br><br>130: Multimedia Franchise<br><br>131: Unified Twitter Taxonomy<br><br>136: Video Game Personality | 137: eSports Team<br><br>138: eSports Player  <br><br>139: Fan Community<br><br>149: Esports League<br><br>152: Food<br><br>155: Weather<br><br>156: Cities<br><br>157: Colleges & Universities<br><br>158: Points of Interest<br><br>159: States<br><br>160: Countries<br><br>162: Exercise & fitness<br><br>163: Travel<br><br>164: Fields of study<br><br>165: Technology<br><br>166: Stocks<br><br>167: Animals<br><br>171: Local News<br><br>172: Global TV Show<br><br>173: Google Product Taxonomy<br><br>174: Digital Assets & Crypto<br><br>175: Emergency Events |

_Note:_ Domain 131 (Unified Twitter Taxonomy) refers to Twitter's User Facing Interest Taxonomy. This taxonomy helps to power features on the platform such as, [Topics](https://blog.twitter.com/en_us/topics/product/2020/topics-behind-the-tweets).