platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

Ad Repository API January 2024 3

Get a list of app and developer names



GET https://adrepository.apple.com/api/v1/ad-repository-entities

Use this endpoint to return list of app and developer names based on custom query

parameter input. A developer name refers to the developer as identified on the App

Store, which is the entity on whose behalf the subject advertising was presented. Only

apps that have been advertised in countries or regions in the European Union in which

Apple-delivered advertising is available on the App Store are searchable.



Request example



GET ~/api/v1/ad-repository-entities?name={URL encoded search input text}

\&types==APP

\&offset=0

\&limit=10



Request parameters



Parameter Type Required Description



name string yes Custom query for app and developer names with a

minimum of 2 characters required.



types string no



Values are:



APP

DEVELOPER

APP,DEVELOPER (T he default value or blank which

returns all types.)