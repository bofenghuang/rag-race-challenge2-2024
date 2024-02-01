platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media


### Reel Specifications

The following are the specifications for Reels:

* Container: MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
    
* Audio codec: AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
    
* Video codec: HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
    
* Frame rate: 23-60 FPS.
    
* Picture size:
    
    * Maximum columns (horizontal pixels): 1920
        
    * Required aspect ratio is between 0.01:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space.
        
    
* Video bitrate: VBR, 25Mbps maximum
    
* Audio bitrate: 128kbps
    
* Duration: 15 mins maximum, 3 seconds minimum
    
* File size: 1GB maximum
    

The following are the specifications for a Reels cover photo:

* Format: JPEG
    
* File size: 8MB maximum
    
* Color Space: sRGB. Images that use other color spaces will be converted to sRGB.
    
* Aspect ratio: We recommend 9:16 to avoid cropping or blank space. If the aspect ratio of the original image is not 9:16, we crop the image and use the middle most 9:16 rectangle as the cover photo for the reel. If you share a reel to your feed, we crop the image and use the middle most 1:1 square as the cover photo for your feed post.