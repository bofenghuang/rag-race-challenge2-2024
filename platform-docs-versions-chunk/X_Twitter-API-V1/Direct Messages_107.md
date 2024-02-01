platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/overview


## Product & development guidance

Collecting structured feedback about customer interactions is a useful part of the customer service experience, providing quantitative measures of service quality and effectiveness that benefits both people and businesses. By asking for feedback in context and shortly after the interaction is complete, people are more likely to provide a response and more likely to provide feedback that reflects their interaction. This feature supports the programmatic creation and delivery of feedback prompts that allow someone to submit responses to feedback surveys after a conversation in Direct Messages.

* Feedback should ideally be built into your product so it can be kicked off automatically, not manually. The goal is to remove potential bias in results and to give a sense of trust to the user (for more honest feedback) that the agent who handled the interaction is not reading the results.
* Feedback results should be delivered to the business via your product. We've built our APIs with an assumption that you could create a dashboard or file download to provide reports to managers. Twitter is not planning to provide an interface for businesses to retrieve results directly from Twitter.
* Feedback results should ideally not be surfaced directly to an agent, and instead, be surfaced in supervisor reports or in an asynchronous way such that an agent doesn’t see the feedback and change their interaction demeanor or behavior.  
    
* Initially, Feedback can only be requested along with a Direct Message. Make sure to check the user object can\_dm to see if you have the ability to send Feedback before hitting the POST endpoint. (Particularly relevant if sending a Feedback prompt after a public interaction.)  
    
* A Direct Message must be sent before prompting a user for Feedback. When brands are considering the Direct Message text preceding the Feedback prompt, make sure it makes sense in the case that the Feedback experience does not render (web client, old clients, 3rd party clients, etc).
* Scores and text can be submitted independently and will likely have different timestamps. A score may be submitted without a text comment ever being completed. Both scores and text are immutable once submitted.
* Code should be tolerant of n ­number of updates per Feedback object. It should not assume a max of three possible updates. You should always rely on the most recent “updated\_at” timestamp.
* An empty next\_cursor value indicates you have reached the end of the result set. You should make no assumption about empty/partial page returned in "events" array as a signal that there is no more data to be fetched.

* * *