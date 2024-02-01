platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/compliance-data-objects


## Payload examples

See the payload examples below for each compliance event described in the table above.

#### Tweet delete

      `{ 	"data": { 		"delete": { 			"tweet": { 				"id": "601430178305220608", 				"author_id": "3198576760" 			}, 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	}  }`
    

When a deleted Tweet has been Quote Tweeted, there will be an additional Tweet 'delete' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### Tweet edit

      `{ 	"data": { 		"tweet_edit": { 			"tweet": { 				"id": "1567233994734948354" 			}, 			"initial_tweet_id": "1567233844205453313", 			"edit_tweet_ids": [ 				"1567233844205453313", 				"1567233994734948354" 			], 			"event_at": "2022-09-06T19:31:16.801Z" 		} 	} }`
    

#### Tweet withheld  

      `{ 	"data": { 		"withheld": { 			"tweet": { 				"id": "601430178305220608", 				"author_id": "3198576760" 			}, 			"withheld_in_countries": [ 				"XY" 			], 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	} }`
    

When a withheld Tweet has been Quote Tweeted, there will be an additional Tweet 'withheld' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### Tweet Drop

      `{ 	"data": { 		"drop": { 			"tweet": { 				"id": "601430178305220600", 				"author_id": "3198576760" 			}, 			"event_at": "2022-12-23T12:34:56.789Z" 		} 	} }`
    

#### Tweet Undrop

      `{   "data":       {        "undrop": {           "tweet": {              "id": "601430178305220600",              "author_id": "3198576760"            },          "event_at": "2022-12-23T12:34:56.789Z"         }      } }`
    

#### User scrub geo

      `{    "data":      {       "scrub_geo": {         "user": {           "id": "1375036644"         },       "up_to_tweet_id": "411552403083628544",       "event_at": "2022-06-27T23:49:41.839+00:00"       }     } }`
    

#### User delete

      `{ 	"data": { 		"user_delete": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User undelete

      `{ 	"data": { 		"user_undelete": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User withheld

      `{ 	"data": { 		"user_withheld": { 			"user": { 				"id": "1375036644" 			}, 			"withheld_in_countries": [ 				"XY" 			], 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User protect

      `{ 	"data": { 		"user_protect": { 			"user": { 				"id": "3182003550" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User unprotect

      `{ 	"data": { 		"user_unprotect": { 			"user": { 				"id": "3182003550" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User suspend

      `{ 	"data": { 		"user_suspend": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

#### User unsuspend

      `{ 	"data": { 		"user_unsuspend": { 			"user": { 				"id": "1375036644" 			}, 			"event_at": "2022-06-27T23:49:41.839+00:00" 		} 	} }`
    

**User profile modification**

      `{   "data": {     "user_profile_modification": {       "user": {         "id": "906948460078698496"       },       "event_at": "2022-07-12T19:47:59.442Z",       "profile_field": "profile.description",       "new_value": "Home of the @SnowbotDev chatbot."     }   } }`
    

The "profile\_field" attribute indicates what in the User profile changed, and can contain the following values: 

* "profile.name"  
    
* "profile.location"
* "profile.description"
* "profile.url"
* "profile.profileBanner"
* "profile.profileBanner.url"
* "profile.profileImage"
* "profile.profileImage.url"