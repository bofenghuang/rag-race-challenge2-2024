platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/getting-started


### Indicator Types

| Match Text | Indicator Type |
| --- | --- |
| Raw Text | `TEXT_STRING` |
| Trend Queries (keywords+regex) | `TREND_QUERY` |

| Match URLs | Indicator Type |
| --- | --- |
| URLs | `URI` |
| Domains | `DOMAIN` |

| Match Photos | Indicator Type |
| --- | --- |
| PDQ Hashes [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fpdq&h=AT1YqmOq-JrbvK1odNN9TLqO87lqDxuCOr6Czgvb7bRhvs3O1iOZOd3a4MomJcy92GLv4mdktAeVgp133vKFiGW79MO2JG7_Uag7P3ooRXF7ytbq14g-HUxHN9SmavhgRbmZfnUzv-Zx2P-x) | `HASH_PDQ` |
| PDQ Hashes + [OCR](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOptical_character_recognition&h=AT2DHtEOgEYMtsThYuRzkxAjIY2rNh0FFJLfZTSh3A6UwjVpu0jinHvlMcBwefCo9VwuoxCf2uO76lp2uupgnEY3XtTmiK_48Zb-n2C0230vsQ1Z3OUeBMIKHWXc0OFz82InqqRhgTulc3Ys) Text | `HASH_PDQ_OCR` |

| Match Videos | Indicator Type |
| --- | --- |
| MD5 Hash [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMD5&h=AT0eVDo7_zH_RJXnL0zgO1gI5OE8wGnjTAXNRPVi91Hi8ATFF3CxajgQAL02G5UUnCCrXIYyFvE35l01LbtGJh5JgceyHF0gZcNAzyHv5PNQ16gsffXIP7t6fSPaSuR5G1MAR0HClXw5ZBpS) | `HASH_MD5` |
| TMK+PDQF Hash [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Ftmk&h=AT3w5Qd1CNXCL9Cnpb8c4esQZXByp8UWHsI9FX8ecBcZgEX4UFCufImo3L-2Vol5Wv8Qj0sy3TPUhhM8Vaww_IH48YSund-AZrhLkNkURCPsOep2ALfXuUUP2RvEFEyH2QbnfeBTtik6qrOW) | `HASH_TMK` |