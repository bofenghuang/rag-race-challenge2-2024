platform: Wikipedia
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Wikipedia_API/API.md
url: https://www.mediawiki.org/wiki/API:Main_page


## Main module

* Source: MediaWiki
* License: [GPL-2.0-or-later](https://www.mediawiki.org/wiki/Special:Version/License/MediaWiki "Special:Version/License/MediaWiki")

* [Documentation](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Main_page "Special:MyLanguage/API:Main page")
* [Etiquette & usage guidelines](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Etiquette "Special:MyLanguage/API:Etiquette")
* [FAQ](https://www.mediawiki.org/wiki/Special:MyLanguage/API:FAQ "Special:MyLanguage/API:FAQ")
* [Mailing list](https://lists.wikimedia.org/postorius/lists/mediawiki-api.lists.wikimedia.org/)
* [API Announcements](https://lists.wikimedia.org/postorius/lists/mediawiki-api-announce.lists.wikimedia.org/)
* [Bugs & requests](https://phabricator.wikimedia.org/maniphest/query/GebfyV4uCaLd/#R)

**Status:** The MediaWiki API is a mature and stable interface that is actively supported and improved. While we try to avoid it, we may occasionally need to make breaking changes; subscribe to [the mediawiki-api-announce mailing list](https://lists.wikimedia.org/hyperkitty/list/mediawiki-api-announce@lists.wikimedia.org/) for notice of updates.

**Erroneous requests:** When erroneous requests are sent to the API, an HTTP header will be sent with the key "MediaWiki-API-Error" and then both the value of the header and the error code sent back will be set to the same value. For more information see [API: Errors and warnings](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Errors_and_warnings "Special:MyLanguage/API:Errors and warnings").

**Testing:** For ease of testing API requests, see [Special:ApiSandbox](https://www.mediawiki.org/wiki/Special:ApiSandbox "Special:ApiSandbox").

Specific parameters:

action

Which action to perform.

[abusefiltercheckmatch](https://www.mediawiki.org/w/api.php?action=help&modules=abusefiltercheckmatch)

Check to see if an AbuseFilter matches a set of variables, an edit, or a logged AbuseFilter event.

[abusefilterchecksyntax](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterchecksyntax)

Check syntax of an AbuseFilter filter.

[abusefilterevalexpression](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterevalexpression)

Evaluates an AbuseFilter expression.

[abusefilterunblockautopromote](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterunblockautopromote)

Unblocks a user from receiving autopromotions due to an abusefilter consequence.

[abuselogprivatedetails](https://www.mediawiki.org/w/api.php?action=help&modules=abuselogprivatedetails)

View private details of an AbuseLog entry.

[acquiretempusername](https://www.mediawiki.org/w/api.php?action=help&modules=acquiretempusername)

Acquire a temporary user username and stash it in the current session, if temp account creation is enabled and the current user is logged out. If a name has already been stashed, returns the same name.

[aggregategroups](https://www.mediawiki.org/w/api.php?action=help&modules=aggregategroups)

Manage aggregate message groups.

[antispoof](https://www.mediawiki.org/w/api.php?action=help&modules=antispoof)

Check a username against AntiSpoof's normalisation checks.

[block](https://www.mediawiki.org/w/api.php?action=help&modules=block)

Block a user.

[centralauthtoken](https://www.mediawiki.org/w/api.php?action=help&modules=centralauthtoken)

Fetch a centralauthtoken for making an authenticated request to an attached wiki.

[centralnoticecdncacheupdatebanner](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticecdncacheupdatebanner)

Request the purge of banner content stored in the CDN (front-end) cache for anonymous users, for the requested banner and language

[centralnoticechoicedata](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticechoicedata)

Get data needed to choose a banner for a given project and language

[centralnoticequerycampaign](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticequerycampaign)

Get all configuration settings for a campaign.

[changeauthenticationdata](https://www.mediawiki.org/w/api.php?action=help&modules=changeauthenticationdata)

Change authentication data for the current user.

[changecontentmodel](https://www.mediawiki.org/w/api.php?action=help&modules=changecontentmodel)

Change the content model of a page

[checktoken](https://www.mediawiki.org/w/api.php?action=help&modules=checktoken)

Check the validity of a token from [action=query&meta=tokens](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Btokens).

[cirrus-config-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-config-dump)

Dump of CirrusSearch configuration.

[cirrus-mapping-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-mapping-dump)

Dump of CirrusSearch mapping for this wiki.

[cirrus-profiles-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-profiles-dump)

Dump of CirrusSearch profiles for this wiki.

[cirrus-settings-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-settings-dump)

Dump of CirrusSearch settings for this wiki.

[clearhasmsg](https://www.mediawiki.org/w/api.php?action=help&modules=clearhasmsg)

Clears the `hasmsg` flag for the current user.

[clientlogin](https://www.mediawiki.org/w/api.php?action=help&modules=clientlogin)

Log in to the wiki using the interactive flow.

[compare](https://www.mediawiki.org/w/api.php?action=help&modules=compare)

Get the difference between two pages.

[createaccount](https://www.mediawiki.org/w/api.php?action=help&modules=createaccount)

Create a new user account.

[createlocalaccount](https://www.mediawiki.org/w/api.php?action=help&modules=createlocalaccount)

Forcibly create a local account. The central account must exist.

[delete](https://www.mediawiki.org/w/api.php?action=help&modules=delete)

Delete a page.

[deleteglobalaccount](https://www.mediawiki.org/w/api.php?action=help&modules=deleteglobalaccount)

Delete a global user.

[discussiontoolsedit](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsedit)

Post a message on a discussion page.

[discussiontoolsfindcomment](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsfindcomment)

Find a comment by its ID or name.

[discussiontoolsgetsubscriptions](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsgetsubscriptions)

Get the subscription statuses of given topics.

[discussiontoolssubscribe](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolssubscribe)

Subscribe (or unsubscribe) to receive notifications about a topic.

[echomarkread](https://www.mediawiki.org/w/api.php?action=help&modules=echomarkread)

Mark notifications as read for the current user.

[echomarkseen](https://www.mediawiki.org/w/api.php?action=help&modules=echomarkseen)

Mark notifications as seen for the current user.

[echomute](https://www.mediawiki.org/w/api.php?action=help&modules=echomute)

Mute or unmute notifications from certain users or pages.

[edit](https://www.mediawiki.org/w/api.php?action=help&modules=edit)

Create and edit pages.

[editmassmessagelist](https://www.mediawiki.org/w/api.php?action=help&modules=editmassmessagelist)

Edit a mass message delivery list.

[emailuser](https://www.mediawiki.org/w/api.php?action=help&modules=emailuser)

Email a user.

[expandtemplates](https://www.mediawiki.org/w/api.php?action=help&modules=expandtemplates)

Expands all templates within wikitext.

[featuredfeed](https://www.mediawiki.org/w/api.php?action=help&modules=featuredfeed)

Returns a featured content feed.

[feedcontributions](https://www.mediawiki.org/w/api.php?action=help&modules=feedcontributions)

Returns a user's contributions feed.

[feedrecentchanges](https://www.mediawiki.org/w/api.php?action=help&modules=feedrecentchanges)

Returns a recent changes feed.

[feedthreads](https://www.mediawiki.org/w/api.php?action=help&modules=feedthreads)

Return a feed of discussion threads.

[feedwatchlist](https://www.mediawiki.org/w/api.php?action=help&modules=feedwatchlist)

Returns a watchlist feed.

[filerevert](https://www.mediawiki.org/w/api.php?action=help&modules=filerevert)

Revert a file to an old version.

[flow](https://www.mediawiki.org/w/api.php?action=help&modules=flow)

Allows actions to be taken on Structured Discussions pages.

[flow-parsoid-utils](https://www.mediawiki.org/w/api.php?action=help&modules=flow-parsoid-utils)

Convert text between wikitext and HTML.

[flowthank](https://www.mediawiki.org/w/api.php?action=help&modules=flowthank)

Send a public thank-you notification for a Flow comment.

[globalblock](https://www.mediawiki.org/w/api.php?action=help&modules=globalblock)

Globally block or unblock a user.

[globalpreferenceoverrides](https://www.mediawiki.org/w/api.php?action=help&modules=globalpreferenceoverrides)

Change local overrides for global preferences for the current user.

[globalpreferences](https://www.mediawiki.org/w/api.php?action=help&modules=globalpreferences)

Change global preferences of the current user.

[globaluserrights](https://www.mediawiki.org/w/api.php?action=help&modules=globaluserrights)

Add/remove a user to/from global groups.

[groupreview](https://www.mediawiki.org/w/api.php?action=help&modules=groupreview)

Set message group workflow states.

[help](https://www.mediawiki.org/w/api.php?action=help&modules=help)

Display help for the specified modules.

[imagerotate](https://www.mediawiki.org/w/api.php?action=help&modules=imagerotate)

This module has been disabled.

[import](https://www.mediawiki.org/w/api.php?action=help&modules=import)

Import a page from another wiki, or from an XML file.

[jsonconfig](https://www.mediawiki.org/w/api.php?action=help&modules=jsonconfig)

Allows direct access to JsonConfig subsystem.

[languagesearch](https://www.mediawiki.org/w/api.php?action=help&modules=languagesearch)

Search for language names in any script.

[linkaccount](https://www.mediawiki.org/w/api.php?action=help&modules=linkaccount)

Link an account from a third-party provider to the current user.

[login](https://www.mediawiki.org/w/api.php?action=help&modules=login)

Log in and get authentication cookies.

[logout](https://www.mediawiki.org/w/api.php?action=help&modules=logout)

Log out and clear session data.

[managetags](https://www.mediawiki.org/w/api.php?action=help&modules=managetags)

Perform management tasks relating to change tags.

[massmessage](https://www.mediawiki.org/w/api.php?action=help&modules=massmessage)

Send a message to a list of pages.

[mergehistory](https://www.mediawiki.org/w/api.php?action=help&modules=mergehistory)

Merge page histories.

[move](https://www.mediawiki.org/w/api.php?action=help&modules=move)

Move a page.

[newslettersubscribe](https://www.mediawiki.org/w/api.php?action=help&modules=newslettersubscribe)

Subscribe to or unsubscribe from a newsletter.

[opensearch](https://www.mediawiki.org/w/api.php?action=help&modules=opensearch)

Search the wiki using the OpenSearch protocol.

[options](https://www.mediawiki.org/w/api.php?action=help&modules=options)

Change preferences of the current user.

[paraminfo](https://www.mediawiki.org/w/api.php?action=help&modules=paraminfo)

Obtain information about API modules.

[parse](https://www.mediawiki.org/w/api.php?action=help&modules=parse)

Parses content and returns parser output.

[patrol](https://www.mediawiki.org/w/api.php?action=help&modules=patrol)

Patrol a page or revision.

[protect](https://www.mediawiki.org/w/api.php?action=help&modules=protect)

Change the protection level of a page.

[purge](https://www.mediawiki.org/w/api.php?action=help&modules=purge)

Purge the cache for the given titles.

[query](https://www.mediawiki.org/w/api.php?action=help&modules=query)

Fetch data from and about MediaWiki.

[removeauthenticationdata](https://www.mediawiki.org/w/api.php?action=help&modules=removeauthenticationdata)

Remove authentication data for the current user.

[resetpassword](https://www.mediawiki.org/w/api.php?action=help&modules=resetpassword)

Send a password reset email to a user.

[revisiondelete](https://www.mediawiki.org/w/api.php?action=help&modules=revisiondelete)

Delete and undelete revisions.

[rollback](https://www.mediawiki.org/w/api.php?action=help&modules=rollback)

Undo the last edit to the page.

[rsd](https://www.mediawiki.org/w/api.php?action=help&modules=rsd)

Export an RSD (Really Simple Discovery) schema.

[searchtranslations](https://www.mediawiki.org/w/api.php?action=help&modules=searchtranslations)

Search translations.

[setglobalaccountstatus](https://www.mediawiki.org/w/api.php?action=help&modules=setglobalaccountstatus)

Hide or lock (or unhide or unlock) a global user account.

[setnotificationtimestamp](https://www.mediawiki.org/w/api.php?action=help&modules=setnotificationtimestamp)

Update the notification timestamp for watched pages.

[setpagelanguage](https://www.mediawiki.org/w/api.php?action=help&modules=setpagelanguage)

Change the language of a page.

[shortenurl](https://www.mediawiki.org/w/api.php?action=help&modules=shortenurl)

Shorten a long URL into a shorter one.

[sitematrix](https://www.mediawiki.org/w/api.php?action=help&modules=sitematrix)

Get Wikimedia sites list.

[spamblacklist](https://www.mediawiki.org/w/api.php?action=help&modules=spamblacklist)

Validate one or more URLs against the spam block list.

[streamconfigs](https://www.mediawiki.org/w/api.php?action=help&modules=streamconfigs)

Exposes event stream config. Returns only format=json with formatversion=2.

[strikevote](https://www.mediawiki.org/w/api.php?action=help&modules=strikevote)

Allows admins to strike or unstrike a vote.

[tag](https://www.mediawiki.org/w/api.php?action=help&modules=tag)

Add or remove change tags from individual revisions or log entries.

[templatedata](https://www.mediawiki.org/w/api.php?action=help&modules=templatedata)

Fetch data stored by the TemplateData extension.

[thank](https://www.mediawiki.org/w/api.php?action=help&modules=thank)

Send a thank-you notification to an editor.

[threadaction](https://www.mediawiki.org/w/api.php?action=help&modules=threadaction)

Allows actions to be taken on threads and posts in threaded discussions.

[titleblacklist](https://www.mediawiki.org/w/api.php?action=help&modules=titleblacklist)

Validate a page title, filename, or username against the TitleBlacklist.

[torblock](https://www.mediawiki.org/w/api.php?action=help&modules=torblock)

Check if an IP address is blocked as a Tor exit node.

[transcodereset](https://www.mediawiki.org/w/api.php?action=help&modules=transcodereset)

Users with the 'transcode-reset' right can reset and re-run a transcode job.

[translationaids](https://www.mediawiki.org/w/api.php?action=help&modules=translationaids)

Query all translations aids.

[translationreview](https://www.mediawiki.org/w/api.php?action=help&modules=translationreview)

Mark translations reviewed.

[translationstats](https://www.mediawiki.org/w/api.php?action=help&modules=translationstats)

Fetch translation statistics

[ttmserver](https://www.mediawiki.org/w/api.php?action=help&modules=ttmserver)

Query suggestions from translation memories.

[unblock](https://www.mediawiki.org/w/api.php?action=help&modules=unblock)

Unblock a user.

[undelete](https://www.mediawiki.org/w/api.php?action=help&modules=undelete)

Undelete revisions of a deleted page.

[unlinkaccount](https://www.mediawiki.org/w/api.php?action=help&modules=unlinkaccount)

Remove a linked third-party account from the current user.

[upload](https://www.mediawiki.org/w/api.php?action=help&modules=upload)

Upload a file, or get the status of pending uploads.

[userrights](https://www.mediawiki.org/w/api.php?action=help&modules=userrights)

Change a user's group membership.

[validatepassword](https://www.mediawiki.org/w/api.php?action=help&modules=validatepassword)

Validate a password against the wiki's password policies.

[watch](https://www.mediawiki.org/w/api.php?action=help&modules=watch)

Add or remove pages from the current user's watchlist.

[webapp-manifest](https://www.mediawiki.org/w/api.php?action=help&modules=webapp-manifest)

Returns a webapp manifest.

[webauthn](https://www.mediawiki.org/w/api.php?action=help&modules=webauthn)

API Module to communicate between server and client during registration/authentication process.

[wikilove](https://www.mediawiki.org/w/api.php?action=help&modules=wikilove)

Give WikiLove to another user.

[bouncehandler](https://www.mediawiki.org/w/api.php?action=help&modules=bouncehandler)

Internal. Receive a bounce email and process it to handle the failing recipient.

[categorytree](https://www.mediawiki.org/w/api.php?action=help&modules=categorytree)

Internal. Internal module for the CategoryTree extension.

[collection](https://www.mediawiki.org/w/api.php?action=help&modules=collection)

Internal. API module for performing various operations on a wiki user's collection.

[cspreport](https://www.mediawiki.org/w/api.php?action=help&modules=cspreport)

Internal. Used by browsers to report violations of the Content Security Policy. This module should never be used, except when used automatically by a CSP compliant web browser.

[discussiontoolscompare](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolscompare)

Internal. Get information about comment changes between two page revisions.

[discussiontoolspageinfo](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolspageinfo)

Internal. Returns metadata required to initialize the discussion tools.

[discussiontoolspreview](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolspreview)

Internal. Preview a message on a discussion page.

[fancycaptchareload](https://www.mediawiki.org/w/api.php?action=help&modules=fancycaptchareload)

Internal. Get a new FancyCaptcha.

[jsondata](https://www.mediawiki.org/w/api.php?action=help&modules=jsondata)

Internal. Retrieve localized JSON data.

[managegroupsynchronizationcache](https://www.mediawiki.org/w/api.php?action=help&modules=managegroupsynchronizationcache)

Internal. Manage group synchronization cache.

[managemessagegroups](https://www.mediawiki.org/w/api.php?action=help&modules=managemessagegroups)

Internal. Add a message as a rename of an existing message or a new message in the group during imports

[oathvalidate](https://www.mediawiki.org/w/api.php?action=help&modules=oathvalidate)

Internal. Validate a two-factor authentication (OATH) token.

[parser-migration](https://www.mediawiki.org/w/api.php?action=help&modules=parser-migration)

Internal. Parse a page with two different parser configurations.

[readinglists](https://www.mediawiki.org/w/api.php?action=help&modules=readinglists)

Internal. Reading list write operations.

[sanitize-mapdata](https://www.mediawiki.org/w/api.php?action=help&modules=sanitize-mapdata)

Internal. Performs data validation for Kartographer extension

[scribunto-console](https://www.mediawiki.org/w/api.php?action=help&modules=scribunto-console)

Internal. Internal module for servicing XHR requests from the Scribunto console.

[securepollauth](https://www.mediawiki.org/w/api.php?action=help&modules=securepollauth)

Internal. Allows a remote wiki to authenticate users before granting access to vote in the election.

[stashedit](https://www.mediawiki.org/w/api.php?action=help&modules=stashedit)

Internal. Prepare an edit in shared cache.

[timedtext](https://www.mediawiki.org/w/api.php?action=help&modules=timedtext)

Internal. Provides timed text content for usage by <track> elements

[translationcheck](https://www.mediawiki.org/w/api.php?action=help&modules=translationcheck)

Internal. Validate translations.

[translationentitysearch](https://www.mediawiki.org/w/api.php?action=help&modules=translationentitysearch)

Internal. Search for message groups and messages

[ulslocalization](https://www.mediawiki.org/w/api.php?action=help&modules=ulslocalization)

Internal. Get the localization of ULS in the given language.

[ulssetlang](https://www.mediawiki.org/w/api.php?action=help&modules=ulssetlang)

Internal. Update user's preferred interface language.

[visualeditor](https://www.mediawiki.org/w/api.php?action=help&modules=visualeditor)

Internal. Returns HTML5 for a page from the Parsoid service.

[visualeditoredit](https://www.mediawiki.org/w/api.php?action=help&modules=visualeditoredit)

Internal. Save an HTML5 page to MediaWiki (converted to wikitext via the Parsoid service).

[wikimediaeventsblockededit](https://www.mediawiki.org/w/api.php?action=help&modules=wikimediaeventsblockededit)

Internal. Log information about blocked edit attempts

One of the following values: [abusefiltercheckmatch](https://www.mediawiki.org/w/api.php?action=help&modules=abusefiltercheckmatch), [abusefilterchecksyntax](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterchecksyntax), [abusefilterevalexpression](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterevalexpression), [abusefilterunblockautopromote](https://www.mediawiki.org/w/api.php?action=help&modules=abusefilterunblockautopromote), [abuselogprivatedetails](https://www.mediawiki.org/w/api.php?action=help&modules=abuselogprivatedetails), [acquiretempusername](https://www.mediawiki.org/w/api.php?action=help&modules=acquiretempusername), [aggregategroups](https://www.mediawiki.org/w/api.php?action=help&modules=aggregategroups), [antispoof](https://www.mediawiki.org/w/api.php?action=help&modules=antispoof), [block](https://www.mediawiki.org/w/api.php?action=help&modules=block), [centralauthtoken](https://www.mediawiki.org/w/api.php?action=help&modules=centralauthtoken), [centralnoticecdncacheupdatebanner](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticecdncacheupdatebanner), [centralnoticechoicedata](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticechoicedata), [centralnoticequerycampaign](https://www.mediawiki.org/w/api.php?action=help&modules=centralnoticequerycampaign), [changeauthenticationdata](https://www.mediawiki.org/w/api.php?action=help&modules=changeauthenticationdata), [changecontentmodel](https://www.mediawiki.org/w/api.php?action=help&modules=changecontentmodel), [checktoken](https://www.mediawiki.org/w/api.php?action=help&modules=checktoken), [cirrus-config-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-config-dump), [cirrus-mapping-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-mapping-dump), [cirrus-profiles-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-profiles-dump), [cirrus-settings-dump](https://www.mediawiki.org/w/api.php?action=help&modules=cirrus-settings-dump), [clearhasmsg](https://www.mediawiki.org/w/api.php?action=help&modules=clearhasmsg), [clientlogin](https://www.mediawiki.org/w/api.php?action=help&modules=clientlogin), [compare](https://www.mediawiki.org/w/api.php?action=help&modules=compare), [createaccount](https://www.mediawiki.org/w/api.php?action=help&modules=createaccount), [createlocalaccount](https://www.mediawiki.org/w/api.php?action=help&modules=createlocalaccount), [delete](https://www.mediawiki.org/w/api.php?action=help&modules=delete), [deleteglobalaccount](https://www.mediawiki.org/w/api.php?action=help&modules=deleteglobalaccount), [discussiontoolsedit](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsedit), [discussiontoolsfindcomment](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsfindcomment), [discussiontoolsgetsubscriptions](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolsgetsubscriptions), [discussiontoolssubscribe](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolssubscribe), [echomarkread](https://www.mediawiki.org/w/api.php?action=help&modules=echomarkread), [echomarkseen](https://www.mediawiki.org/w/api.php?action=help&modules=echomarkseen), [echomute](https://www.mediawiki.org/w/api.php?action=help&modules=echomute), [edit](https://www.mediawiki.org/w/api.php?action=help&modules=edit), [editmassmessagelist](https://www.mediawiki.org/w/api.php?action=help&modules=editmassmessagelist), [emailuser](https://www.mediawiki.org/w/api.php?action=help&modules=emailuser), [expandtemplates](https://www.mediawiki.org/w/api.php?action=help&modules=expandtemplates), [featuredfeed](https://www.mediawiki.org/w/api.php?action=help&modules=featuredfeed), [feedcontributions](https://www.mediawiki.org/w/api.php?action=help&modules=feedcontributions), [feedrecentchanges](https://www.mediawiki.org/w/api.php?action=help&modules=feedrecentchanges), [feedthreads](https://www.mediawiki.org/w/api.php?action=help&modules=feedthreads), [feedwatchlist](https://www.mediawiki.org/w/api.php?action=help&modules=feedwatchlist), [filerevert](https://www.mediawiki.org/w/api.php?action=help&modules=filerevert), [flow-parsoid-utils](https://www.mediawiki.org/w/api.php?action=help&modules=flow-parsoid-utils), [flow](https://www.mediawiki.org/w/api.php?action=help&modules=flow), [flowthank](https://www.mediawiki.org/w/api.php?action=help&modules=flowthank), [globalblock](https://www.mediawiki.org/w/api.php?action=help&modules=globalblock), [globalpreferenceoverrides](https://www.mediawiki.org/w/api.php?action=help&modules=globalpreferenceoverrides), [globalpreferences](https://www.mediawiki.org/w/api.php?action=help&modules=globalpreferences), [globaluserrights](https://www.mediawiki.org/w/api.php?action=help&modules=globaluserrights), [groupreview](https://www.mediawiki.org/w/api.php?action=help&modules=groupreview), [help](https://www.mediawiki.org/w/api.php?action=help&modules=help), [imagerotate](https://www.mediawiki.org/w/api.php?action=help&modules=imagerotate), [import](https://www.mediawiki.org/w/api.php?action=help&modules=import), [jsonconfig](https://www.mediawiki.org/w/api.php?action=help&modules=jsonconfig), [languagesearch](https://www.mediawiki.org/w/api.php?action=help&modules=languagesearch), [linkaccount](https://www.mediawiki.org/w/api.php?action=help&modules=linkaccount), [login](https://www.mediawiki.org/w/api.php?action=help&modules=login), [logout](https://www.mediawiki.org/w/api.php?action=help&modules=logout), [managetags](https://www.mediawiki.org/w/api.php?action=help&modules=managetags), [massmessage](https://www.mediawiki.org/w/api.php?action=help&modules=massmessage), [mergehistory](https://www.mediawiki.org/w/api.php?action=help&modules=mergehistory), [move](https://www.mediawiki.org/w/api.php?action=help&modules=move), [newslettersubscribe](https://www.mediawiki.org/w/api.php?action=help&modules=newslettersubscribe), [opensearch](https://www.mediawiki.org/w/api.php?action=help&modules=opensearch), [options](https://www.mediawiki.org/w/api.php?action=help&modules=options), [paraminfo](https://www.mediawiki.org/w/api.php?action=help&modules=paraminfo), [parse](https://www.mediawiki.org/w/api.php?action=help&modules=parse), [patrol](https://www.mediawiki.org/w/api.php?action=help&modules=patrol), [protect](https://www.mediawiki.org/w/api.php?action=help&modules=protect), [purge](https://www.mediawiki.org/w/api.php?action=help&modules=purge), [query](https://www.mediawiki.org/w/api.php?action=help&modules=query), [removeauthenticationdata](https://www.mediawiki.org/w/api.php?action=help&modules=removeauthenticationdata), [resetpassword](https://www.mediawiki.org/w/api.php?action=help&modules=resetpassword), [revisiondelete](https://www.mediawiki.org/w/api.php?action=help&modules=revisiondelete), [rollback](https://www.mediawiki.org/w/api.php?action=help&modules=rollback), [rsd](https://www.mediawiki.org/w/api.php?action=help&modules=rsd), [searchtranslations](https://www.mediawiki.org/w/api.php?action=help&modules=searchtranslations), [setglobalaccountstatus](https://www.mediawiki.org/w/api.php?action=help&modules=setglobalaccountstatus), [setnotificationtimestamp](https://www.mediawiki.org/w/api.php?action=help&modules=setnotificationtimestamp), [setpagelanguage](https://www.mediawiki.org/w/api.php?action=help&modules=setpagelanguage), [shortenurl](https://www.mediawiki.org/w/api.php?action=help&modules=shortenurl), [sitematrix](https://www.mediawiki.org/w/api.php?action=help&modules=sitematrix), [spamblacklist](https://www.mediawiki.org/w/api.php?action=help&modules=spamblacklist), [streamconfigs](https://www.mediawiki.org/w/api.php?action=help&modules=streamconfigs), [strikevote](https://www.mediawiki.org/w/api.php?action=help&modules=strikevote), [tag](https://www.mediawiki.org/w/api.php?action=help&modules=tag), [templatedata](https://www.mediawiki.org/w/api.php?action=help&modules=templatedata), [thank](https://www.mediawiki.org/w/api.php?action=help&modules=thank), [threadaction](https://www.mediawiki.org/w/api.php?action=help&modules=threadaction), [titleblacklist](https://www.mediawiki.org/w/api.php?action=help&modules=titleblacklist), [torblock](https://www.mediawiki.org/w/api.php?action=help&modules=torblock), [transcodereset](https://www.mediawiki.org/w/api.php?action=help&modules=transcodereset), [translationaids](https://www.mediawiki.org/w/api.php?action=help&modules=translationaids), [translationreview](https://www.mediawiki.org/w/api.php?action=help&modules=translationreview), [translationstats](https://www.mediawiki.org/w/api.php?action=help&modules=translationstats), [ttmserver](https://www.mediawiki.org/w/api.php?action=help&modules=ttmserver), [unblock](https://www.mediawiki.org/w/api.php?action=help&modules=unblock), [undelete](https://www.mediawiki.org/w/api.php?action=help&modules=undelete), [unlinkaccount](https://www.mediawiki.org/w/api.php?action=help&modules=unlinkaccount), [upload](https://www.mediawiki.org/w/api.php?action=help&modules=upload), [userrights](https://www.mediawiki.org/w/api.php?action=help&modules=userrights), [validatepassword](https://www.mediawiki.org/w/api.php?action=help&modules=validatepassword), [watch](https://www.mediawiki.org/w/api.php?action=help&modules=watch), [webapp-manifest](https://www.mediawiki.org/w/api.php?action=help&modules=webapp-manifest), [webauthn](https://www.mediawiki.org/w/api.php?action=help&modules=webauthn), [wikilove](https://www.mediawiki.org/w/api.php?action=help&modules=wikilove), [bouncehandler](https://www.mediawiki.org/w/api.php?action=help&modules=bouncehandler), [categorytree](https://www.mediawiki.org/w/api.php?action=help&modules=categorytree), [collection](https://www.mediawiki.org/w/api.php?action=help&modules=collection), [cspreport](https://www.mediawiki.org/w/api.php?action=help&modules=cspreport), [discussiontoolscompare](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolscompare), [discussiontoolspageinfo](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolspageinfo), [discussiontoolspreview](https://www.mediawiki.org/w/api.php?action=help&modules=discussiontoolspreview), [fancycaptchareload](https://www.mediawiki.org/w/api.php?action=help&modules=fancycaptchareload), [jsondata](https://www.mediawiki.org/w/api.php?action=help&modules=jsondata), [managegroupsynchronizationcache](https://www.mediawiki.org/w/api.php?action=help&modules=managegroupsynchronizationcache), [managemessagegroups](https://www.mediawiki.org/w/api.php?action=help&modules=managemessagegroups), [oathvalidate](https://www.mediawiki.org/w/api.php?action=help&modules=oathvalidate), [parser-migration](https://www.mediawiki.org/w/api.php?action=help&modules=parser-migration), [readinglists](https://www.mediawiki.org/w/api.php?action=help&modules=readinglists), [sanitize-mapdata](https://www.mediawiki.org/w/api.php?action=help&modules=sanitize-mapdata), [scribunto-console](https://www.mediawiki.org/w/api.php?action=help&modules=scribunto-console), [securepollauth](https://www.mediawiki.org/w/api.php?action=help&modules=securepollauth), [stashedit](https://www.mediawiki.org/w/api.php?action=help&modules=stashedit), [timedtext](https://www.mediawiki.org/w/api.php?action=help&modules=timedtext), [translationcheck](https://www.mediawiki.org/w/api.php?action=help&modules=translationcheck), [translationentitysearch](https://www.mediawiki.org/w/api.php?action=help&modules=translationentitysearch), [ulslocalization](https://www.mediawiki.org/w/api.php?action=help&modules=ulslocalization), [ulssetlang](https://www.mediawiki.org/w/api.php?action=help&modules=ulssetlang), [visualeditor](https://www.mediawiki.org/w/api.php?action=help&modules=visualeditor), [visualeditoredit](https://www.mediawiki.org/w/api.php?action=help&modules=visualeditoredit), [wikimediaeventsblockededit](https://www.mediawiki.org/w/api.php?action=help&modules=wikimediaeventsblockededit)

Default: help

format

The format of the output.

[json](https://www.mediawiki.org/w/api.php?action=help&modules=json)

Output data in JSON format.

[jsonfm](https://www.mediawiki.org/w/api.php?action=help&modules=jsonfm)

Output data in JSON format (pretty-print in HTML).

[none](https://www.mediawiki.org/w/api.php?action=help&modules=none)

Output nothing.

[php](https://www.mediawiki.org/w/api.php?action=help&modules=php)

Output data in serialized PHP format.

[phpfm](https://www.mediawiki.org/w/api.php?action=help&modules=phpfm)

Output data in serialized PHP format (pretty-print in HTML).

[rawfm](https://www.mediawiki.org/w/api.php?action=help&modules=rawfm)

Output data, including debugging elements, in JSON format (pretty-print in HTML).

[xml](https://www.mediawiki.org/w/api.php?action=help&modules=xml)

Output data in XML format.

[xmlfm](https://www.mediawiki.org/w/api.php?action=help&modules=xmlfm)

Output data in XML format (pretty-print in HTML).

One of the following values: [json](https://www.mediawiki.org/w/api.php?action=help&modules=json), [jsonfm](https://www.mediawiki.org/w/api.php?action=help&modules=jsonfm), [none](https://www.mediawiki.org/w/api.php?action=help&modules=none), [php](https://www.mediawiki.org/w/api.php?action=help&modules=php), [phpfm](https://www.mediawiki.org/w/api.php?action=help&modules=phpfm), [rawfm](https://www.mediawiki.org/w/api.php?action=help&modules=rawfm), [xml](https://www.mediawiki.org/w/api.php?action=help&modules=xml), [xmlfm](https://www.mediawiki.org/w/api.php?action=help&modules=xmlfm)

Default: jsonfm

maxlag

Maximum lag can be used when MediaWiki is installed on a database replicated cluster. To save actions causing any more site replication lag, this parameter can make the client wait until the replication lag is less than the specified value. In case of excessive lag, error code maxlag is returned with a message like Waiting for $host: $lag seconds lagged.  
See [Manual: Maxlag parameter](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Maxlag_parameter "Special:MyLanguage/Manual:Maxlag parameter") for more information.

Type: integer

smaxage

Set the `s-maxage` HTTP cache control header to this many seconds. Errors are never cached.

Type: integer

The value must be no less than 0.

Default: 0

maxage

Set the `max-age` HTTP cache control header to this many seconds. Errors are never cached.

Type: integer

The value must be no less than 0.

Default: 0

assert

Verify that the user is logged in (including possibly as a temporary user) if set to user, _not_ logged in if set to anon, or has the bot user right if bot.

One of the following values: anon, bot, user

assertuser

Verify the current user is the named user.

Type: user, by any of username and Temporary user

requestid

Any value given here will be included in the response. May be used to distinguish requests.

servedby

Include the hostname that served the request in the results.

Type: boolean ([details](#main/datatype/boolean))

curtimestamp

Include the current timestamp in the result.

Type: boolean ([details](#main/datatype/boolean))

responselanginfo

Include the languages used for uselang and errorlang in the result.

Type: boolean ([details](#main/datatype/boolean))

origin

When accessing the API using a cross-domain AJAX request (CORS), set this to the originating domain. This must be included in any pre-flight request, and therefore must be part of the request URI (not the POST body).

For authenticated requests, this must match one of the origins in the `Origin` header exactly, so it has to be set to something like [https://en.wikipedia.org](https://en.wikipedia.org/) or [https://meta.wikimedia.org](https://meta.wikimedia.org/). If this parameter does not match the `Origin` header, a 403 response will be returned. If this parameter matches the `Origin` header and the origin is allowed, the `Access-Control-Allow-Origin` and `Access-Control-Allow-Credentials` headers will be set.

For non-authenticated requests, specify the value \*. This will cause the `Access-Control-Allow-Origin` header to be set, but `Access-Control-Allow-Credentials` will be `false` and all user-specific data will be restricted.

uselang

Language to use for message translations. [action=query&meta=siteinfo](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bsiteinfo) with siprop=languages returns a list of language codes, or specify user to use the current user's language preference, or specify content to use this wiki's content language.

Default: user

variant

Variant of the language. Only works if the base language supports variant conversion.

errorformat

Format to use for warning and error text output

plaintext

Wikitext with HTML tags removed and entities replaced.

wikitext

Unparsed wikitext.

html

HTML

raw

Message key and parameters.

none

No text output, only the error codes.

bc

Format used prior to MediaWiki 1.29. errorlang and errorsuselocal are ignored.

One of the following values: bc, html, none, plaintext, raw, wikitext

Default: bc

errorlang

Language to use for warnings and errors. [action=query&meta=siteinfo](https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bsiteinfo) with siprop=languages returns a list of language codes, or specify content to use this wiki's content language, or specify uselang to use the same value as the uselang parameter.

Default: uselang

errorsuselocal

If given, error texts will use locally-customized messages from the MediaWiki namespace.

Type: boolean ([details](#main/datatype/boolean))

centralauthtoken

When accessing the API using a cross-domain AJAX request (CORS), use this to authenticate as the current SUL user. Use [action=centralauthtoken](https://www.mediawiki.org/w/api.php?action=help&modules=centralauthtoken) on this wiki to retrieve the token, before making the CORS request. Each token may only be used once, and expires after 10 seconds. This should be included in any pre-flight request, and therefore should be included in the request URI (not the POST body).

Examples:

Help for the main module.

[api.php?action=help](https://www.mediawiki.org/w/api.php?action=help) [\[open in sandbox\]](https://www.mediawiki.org/wiki/Special:ApiSandbox#action=help)

All help in one page.

[api.php?action=help&recursivesubmodules=1](https://www.mediawiki.org/w/api.php?action=help&recursivesubmodules=1) [\[open in sandbox\]](https://www.mediawiki.org/wiki/Special:ApiSandbox#action=help&recursivesubmodules=1)

Permissions:

writeapi

Use of the write API

Granted to: all, user and bot

apihighlimits

Use higher limits in API queries (slow queries: 500; fast queries: 5000). The limits for slow queries also apply to multivalue parameters.

Granted to: bot and sysop