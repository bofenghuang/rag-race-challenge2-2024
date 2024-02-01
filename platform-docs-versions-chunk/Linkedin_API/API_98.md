platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients


## Example

To illustrate the benefits of using these API clients, consider [searching for ad accounts](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts#search-for-accounts) using our Advertising API. For a NodeJS application using an HTTP client library like [axios](https://axios-http.com/), there are quite a few details to get right to perform a working request, as shown in the following sample code: base URL, resource prefix, auth and custom headers, and correct encoding of complex query parameters. The result can be difficult to write and maintain and doesn’t account for edge cases requiring query tunneling.

    const axios = require('axios');
    
    const ACCESS_TOKEN = "AQX5…";
    const API_VERSION = '202302';
    
    // Define a generic function to search ad accounts by references
    function searchForAdAccountsByReferences(
     references,
     count = 10,
     sortField = 'ID',
     sortOrder = 'ASCENDING'
    ) {
     return axios.request({
       baseURL: 'https://api.linkedin.com',
       url: '/rest/adAccounts',
       method: 'get',
       headers: {
         'Authorization': `Bearer ${ACCESS_TOKEN}`,
         'X-RestLi-Method': 'finder',
         'X-RestLi-Protocol-Version': '2.0.0',
         'Connection': 'Keep-Alive',
         'LinkedIn-Version': API_VERSION
       },
       params: {
         q: 'search',
         search: `(reference:(values:List(${references.map(encodeURIComponent).join(',')})))`,
         count,
         sort: `(field:${sortField},order:${sortOrder})`
       },
       paramsSerializer: {
         // Can't use default encoding
         encode: (val) => val
       }
     }).then(response => response.data.elements);
    }
    
    // Search for ad accounts by a list of organizations, with up to 20 results
    const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
    searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
     console.log(adAccounts);
    });
    

Compare that to this code utilizing the LinkedIn API client. The client abstracts much of the complexities of constructing the request. It allows passing in objects, arrays, and strings with special characters as is, making the code easy to write and maintain. Furthermore, it handles edge cases where query tunneling may be required.

    const { RestliClient } = require('linkedin-api-client');
    
    const restliClient = new RestliClient();
    const ACCESS_TOKEN = "AQX5...";
    const API_VERSION = '202302';
    
    // Define a generic function to search ad accounts by references
    function searchForAdAccountsByReferences(
      references,
      count = 10,
      sortField = 'ID',
      sortOrder = 'ASCENDING'
    ) {
      return restliClient.finder({
        resourcePath: '/adAccounts',
        finderName: 'search',
        queryParams: {
          search: {
            reference: {
              values: references
            },
          },
          count,
          sort: {
            field: sortField,
            order: sortOrder
          }
        },
        versionString: API_VERSION,
        accessToken: ACCESS_TOKEN
      }).then(response => response.data.elements);
    }
    
    // Search for ad accounts by a list of organizations, with up to 20 results
    const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
    searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
      console.log(adAccounts);
    });
    

In summary, using these API clients can speed up and simplify the development process and make your application code maintainable and robust. If any issues arise, the corresponding Github repository is available for bug reports and enhancement suggestions.