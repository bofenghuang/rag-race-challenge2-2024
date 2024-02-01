platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/event/photos

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `source` | The photo, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT39v8aoonxHWXVtajg_3Anlc2X_Ti0iWzZ6ln8pknZ46iAXVT_8RYSwPbCNUAdc4Dm8-EO_pQzyii4dXJghCKqzIhdCBkfTRvHzK1rIlQr_aNWS51fYv5jqoFvqSN5yTw3czsSFPMmD271h). Either this or `url` field is required, but both should not be used together. | [`multipart/form-data`](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT1QWEY_GpyYtBvx2-rijZ_FRlrXW-5SsJeMtzwDEWS-q8v1Eoml9AGA5CQ-2HnfCRZ_kyntXz_Zt_elsE8I3-qEhBZ86bI8KSyFmupQydzw3fSDoWrsTwzG-0TXmpBsFR71s16SGsnvd4B4) |
| `url` | The URL of a photo that is already uploaded to the internet. Either this or `source` is required, but both should not be used together. | `string` |
| `message` | The description of the photo, used as the accompanying status message in any feed story. | `string` |