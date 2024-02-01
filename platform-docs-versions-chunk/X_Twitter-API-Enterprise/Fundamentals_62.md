platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities


## Introduction

If a Tweet contains native media (shared with the Tweet user-interface as opposed via a link to elsewhere), there will also be a extended\_entities section. When it comes to any native media (photo, video, or GIF), the extended\_entities is the preferred metadata source for several reasons. Currently, up to four photos can be attached to a Tweet. The entities metadata will only contain the first photo (until 2014, only one photo could be included), while the extended\_entities section will include all attached photos. With native media, another deficiency of the entities.media metadata is that the media type will always indicate ‘photo’, even in cases where the attached media is a video or animated GIF. The actual type of media is specified in the extended\_entities.media\[\].type attribute and is set to either _photo_, _video_, or _animated\_gif_. For these reasons, if you are working with native media, the extended\_entities metadata is the way to go.

All Tweets with attached photos, videos and animated GIFs will include an `extended_entities` JSON object. The `extended_entities` object contains a single `media` array of `media` objects (see the `entities` section for its data dictionary). No other entity types, such as hashtags and links, are included in the `extended_entities` section. The `media` object in the `extended_entities` section is identical in structure to the one included in the `entities` section.  

Tweets can only have one type of media attached to it. For photos, up to four photos can be attached. For videos and GIFs, one can be attached. Since the media `type` metadata in the `extended_entities` section correctly indicates the media type (‘photo’, ‘video’ or ‘animated\_gif’), and supports up to 4 photos, it is the preferred metadata source for native media.

    {
      "extended_entities": {
        "media": [
          
        ]
      }
    }