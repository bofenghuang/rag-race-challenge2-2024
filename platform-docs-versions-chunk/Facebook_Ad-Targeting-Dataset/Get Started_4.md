platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Get Started
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Get Started.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/get-started

### Step 1: log in

While connected to our VPN, visit the Researcher Platform URL that was emailed to you and log into the site using your Facebook credentials. This will spin up a Jupyter Notebook server instance for your use.

You can access Researcher Platform user documentation [here](https://developers.facebook.com/docs/researcher-platform/).

### Step 2: Create a notebook

Click the **New** dropdown menu and select either **Python3** or **R**. This will create a new Jupyter Notebook in a new browser tab. Rename the Notebook if you wish.

### Step 3: Import the query module

Import our query module (`execute`) by clicking in an empty notebook cell and entering the following code:

RPython

    library(fbrir)

    from fbri.private.sql.query import execute

Run the code by clicking **\>**. You won't see anything happen, but a new notebook cell will appear when it finishes importing.