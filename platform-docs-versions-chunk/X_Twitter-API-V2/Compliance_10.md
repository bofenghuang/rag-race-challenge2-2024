platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/integrate


### Install the dependencies

Before proceeding, you should have a Node.js environment installed; you can obtain Node.js from its website. Once installed, Node.js will contain a utility called npm; make sure both Node and npm are installed by calling the following command, and ensure it doesn’t result in an error.

      `$ npm -v 6.4.1`
    

A version number similar to this signifies your environment is ready (note that your version number may differ). We will use npm to install the upload library. Run this command:

      `$ npm install -g needle`
    

You’re all set; there is no additional configuration required.

#### Request a resumable destination

When creating a new job, set the resumable parameter to true so you can get a destination that supports a resumable upload. In the response payload, you will receive an upload\_url value.

      `"upload_url":\ "https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"`
    

#### Prepare the code to upload a file

By default, the library will create a new upload destination by accepting an upload location (called bucket) and the name of the file you wish to upload. Because the batch compliance endpoints create their own destination, we will need to tell the library we already have a location ready to accept our upload. 

  
We will need to pass this value to the upload library, along with the name of the file containing the data to upload. Create a file, and name it _**twitter-upload.js**_. Add the following code:

      ``const needle = require('needle'); const fs = require('fs'); const path = require('path');  const [, scriptName, filename, uploadURL] = process.argv; if (!filename || !uploadURL) {   console.error(`Usage: node ${path.basename(scriptName)} filename upload_url`);   process.exit(-1); }  async function uploadFile(file, url) {   // rangeEnd is the index of the last byte in the file, i.e. number of bytes in file   const rangeEnd = (await fs.promises.stat(file)).size;      let options = {     headers: {       'Content-Range': `bytes */${rangeEnd}`,     },   };      const response = await needle('put', url, null, options);    switch (response.statusCode) {     case 200:     case 201:       console.log('Upload complete');       return;     case 308:       return resumeUpload(response, file, url);     default:        console.log('Got unexpected response code: ', response.statusCode);       return;   } }  async function resumeUpload(response, file, url) {   console.log('Upload not completed, resuming');   if (response.headers.range) {           let resumeOffset = Number(response.headers.range.split('-')[1]) + 1;          let options = {       headers: {         'Content-Range': `bytes ${resumeOffset}-${rangeEnd-1}/${rangeEnd}`,         'Content-Length': `${rangeEnd-resumeOffset}`,       },     };          let readStream = fs.createReadStream(file, {start: resumeOffset});     return needle('put', url, readStream, options);   } else {     console.log('Initiating upload');     let options = {       headers: {         'Content-Type': 'text/plain'       }     };          let readStream = fs.createReadStream(file);     return needle('put', url, readStream, options);   } }  // Request resumable session URL async function requestResumableSession(url) {   const options = {     headers: {       'Content-Type': 'text/plain',       'Content-Length': '0',       'x-goog-resumable': 'start',     },   };    const res = await needle('post', url, null, options);   if (res.statusCode === 201) {     const resumableSessionURL = res.headers['location'];     console.log('Starting upload to: ', resumableSessionURL);          await uploadFile(filename, resumableSessionURL);   } else {     console.log('Failed to create resumable session URI');   }    }  requestResumableSession(uploadURL).then(result => console.log('Upload complete'));``
    

Save the file wherever it makes the most sense. Next, in your command line, invoke the script and pass two parameters:

1. The first will be the location of the file (with the Tweet or User IDs) that you wish to upload.
2. The second will be the upload URL we received from the compliance endpoint response.

Ensure the URL is surrounded in double-quotes, and do the same for your file name if it contains spaces or other characters:  

      `node twitter-upload.js compliance_upload.txt\ "https://storage.googleapis.com/compliance_tweet_ids/customer_test_object_12950882_GlYjiE?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=193969463581-compute%40developer.gserviceaccount.com%2F20200618%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20200618T184154Z&X-Goog-Expires=900&X-Goog-SignedHeaders=content-type%3Bhost&X-Goog-Signature=b7bdcf32479b08715be91ed47b06471b8acdcdb319f8e4f423bf3a3056dfa03ed83e47446f33338e292967a15c08fa5ba34395edaf057a2ac975b88e710ca994adb023a9e1673a7c58ce2fa0d73537f72812af78e92b708dfe6b907a7d75bd0f6cfa61fec867e80ac83ced0725d1ee59787c9dbca50d41f7b0f513dad63a7564136b1a70042a2ec6ba6b697cbe480a4405362f7a08255a5e8205aa7baa562f99e6a092f0420f33d67ffaeb132f877fbaf16c969630b5f173e8a3f31c473707241fa4e28f4bed13fb2ea01d3af1c449321a2e6ee9ec1e331b447cabcfc6f9d1f99f564d180f0cc1d28ea54972c996102c67c6501c6c16a00c13d17756f960e0e1"`
    

You will see output similar to this:

      `Starting upload to:  https://storage.googleapis.com/twttr-tweet-compliance/<redacted> Upload not completed, resuming Initiating upload`
    

You can pause the upload at any time by pressing Ctrl + C or closing your command line. You will be able to resume the upload from where you left off when you invoke the same command at a later stage. Once the file has been completely uploaded, you will see the following message:

      `Upload complete`
    

At this point, you will be able to use the [compliance status endpoint](https://developer-staging.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id) to check on the status of your compliance job, and you will be able to download the compliance result when complete.