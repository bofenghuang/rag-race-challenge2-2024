platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/building-a-rule


## Getting started with enterprise rules and queries

Products utilizing enterprise operators deliver social data to you based on filtering rules you set up. Rules are made up of one or more ‘clauses’, where a clause is a keyword, exact phrase, or one of the many enterprise operators. Before beginning to build rules with enterprise operators, be sure to review the syntax described below, look through the list of available operators, and understand the restrictions around building rules. You should also be sure to understand the nuances of how rules are evaluated logically, in the "[Order of operations](#orderofoperations)" section.

Multiple clauses can be combined with both "and" and "or" logic.

**Please note:** "And" logic is specified with a space between clauses, while or logic is specified with an upper-case `OR`. 

Each rule can be up to 2,048 characters long with no limits on the number of positive clauses (things you want to match or filter on) and negative clauses (things you want to exclude and not match on).