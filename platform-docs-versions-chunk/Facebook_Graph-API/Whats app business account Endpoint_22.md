platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_template_previews/

### Sample Response

{
  "data": \[
    {
      "body": "\*{{1}}\* is your verification code. For your security, do not share this code.",
      "buttons": \[
        {
          "autofill\_text": "Autofill",
          "text": "Copy code"
        }
      \],
      "footer": "This code expires in 10 minutes.",
      "language": "en\_US"
    },
    {
      "body": "Tu código de verificación es \*{{1}}\*. Por tu seguridad, no lo compartas.",
      "buttons": \[
        {
          "autofill\_text": "Autocompletar",
          "text": "Copiar código"
        }
      \],
      "footer": "Este código caduca en 10 minutos.",
      "language": "es\_ES"
    }
  \]
}