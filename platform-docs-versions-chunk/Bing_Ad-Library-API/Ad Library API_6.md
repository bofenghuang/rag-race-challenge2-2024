platform: Bing
topic: Ad-Library-API
subtopic: Ad Library API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Bing_Ad-Library-API/Ad Library API.md
url: https://learn.microsoft.com/en-us/advertising/guides/ad-library-api?view=bingads-13


### Authenticating your credentials

Ad Library API uses the same authentication schemes as Bing Ads API. For details about authenticating Microsoft account credentials with OAuth, see [Authentication with the Microsoft identity platform](https://learn.microsoft.com/en-us/advertising/guides/authentication-oauth-identity-platform).

You can use the Bing Ads SDK for .NET, Java, or Python to authenticate Microsoft account credentials. For details about using the SDK to get the access token, see [C#](https://learn.microsoft.com/en-us/advertising/guides/get-started-csharp) | [Java](https://learn.microsoft.com/en-us/advertising/guides/get-started-java) | [Python](https://learn.microsoft.com/en-us/advertising/guides/get-started-python).

_Note_: The Bing Ads SDK doesn't provide interfaces for Ad Library API. You should only use the SDK to get the access token if you're using the SDK for Microsoft Advertising campaigns, too. Otherwise, it may not be worth the overhead of installing the SDK.

If you don't use the Bing Ads SDK for authentication, see Authenticating Microsoft Account Credentials in C# for an example that shows how to use OAuth to authenticate Microsoft account credentials.