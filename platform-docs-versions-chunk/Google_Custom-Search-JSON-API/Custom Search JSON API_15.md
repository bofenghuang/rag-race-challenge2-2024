platform: Google
topic: Custom-Search-JSON-API
subtopic: Custom Search JSON API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Google_Custom-Search-JSON-API/Custom Search JSON API.md
url: https://developers.google.com/custom-search/v1/using_rest


## REST from JavaScript

You can invoke the Custom Search JSON API using REST from JavaScript, using the `callback` query parameter and a callback function. This allows you to write rich applications that display Programmable Search Engine data without writing any server side code.

The following example uses this approach to display the first page of search results for the query **cars**:

    <html>
      <head>
        <title>Custom Search JSON API Example</title>
      </head>
      <body>
        <div id="content"></div>
        <script>
          function hndlr(response) {
          for (var i = 0; i < response.items.length; i++) {
            var item = response.items[i];
            // Make sure HTML in item.htmlTitle is escaped.
            document.getElementById("content").append(
              document.createElement("br"),
              document.createTextNode(item.htmlTitle)
            );
          }
        }
        </script>
        <script src="https://www.googleapis.com/customsearch/v1?key=YOUR-KEY&cx=017576662512468239146:omuauf_lfve&q=cars&callback=hndlr">
        </script>
      </body>
    </html>