platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained


### Client disconnects  

A client disconnect is essentially any disconnection that occurs which isn’t initiated by our servers. There are many causes for this. Sometimes this could be caused by the code or the architecture of your application, but this often occurs when something in the internet or network layer cuts off the connection. This section provides a list of the most common causes for a client disconnects.  
 

**Issues at the network layer**

Routing issues at the networking level can cause disconnects. For example, a Border Gateway Protocol (BGP) update can go awry, and clients can disconnect as routers fail to keep up with the sudden additional load put on them when a route fails. As network operators cooperate to reroute traffic, you may notice a pattern of disconnects for some time.  
 

**Firewall configuration**

Clients may have firewalls set up with session limits that cut off the connections after a certain amount of time, which they need to create exceptions for. From our side, our servers just see the connection close, so we don’t have a way to see whether it was closed by the proactive actions of your app, or just something related to the internet connection between your client and the Twitter servers.  
 

**Data burst and packet loss**

Clients should be designed to handle spikes in the volume of Tweets received. If a client is slow to consume a stream, it will receive a [full buffer disconnect](#full_buffer_disconnect). However, there are situations where the client is not able to handle a sudden surge in volume (for example, after significant rule activity) which will cause the client to drop packets. When this happens, you may notice the client resetting a TCP/IP connection. In certain cases, the connection is terminated correctly and cleanly; however, there may be situations where the underlying networking layer doesn't close the socket properly, or does so after a set delay. In your dashboard, this event will be reported as a client disconnect. In such cases, clients must be sized to handle multiple times the average Tweet volume. It can be beneficial to examine the network traffic to detect any pattern that leads the client to drop packets.  
 

**Failure to reconnect after a disconnection**

Occasionally, some customers have trouble reconnecting to their stream after they’ve terminated a connection. Assuming there are no operational issues posted on our [Status Page](https://api.twitterstat.us/), one reason might be that something within your code is keeping the connection alive. In these scenarios, we see something in the layer outside of your app persisting, because the connection wasn’t properly terminated. Generally we see similar behavior when the HTTP client portion of the code isn’t getting proactively closed. It might also be that there is simply some network latency or delay set at the configuration level preventing the request from going through.