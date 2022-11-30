# Instagram Auto Posting

### [Daily automatic instagram image post](https://www.instagram.com/___scrivener___/)

## Tech
Instagram autoposting uses [Instagram API](https://developers.facebook.com/docs/instagram-api/), part of Facebook's Meta Program and Access Token of a created App in Fackebook developers page which are temporary but Permanant access Token can be generated using Temporary Token, to know how [click here](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived).

### This Posting involves Two Steps
##### 1. Image Creation and Editing

A background Image is editied using python [PILLOW](https://pypi.org/project/Pillow/) module to add a random quote from [Quotes API](https://github.com/lukePeavey/quotable)
This created image is then uploaded to [Amazon S3](https://aws.amazon.com/s3/), a cloud object Storage service offered by AWS.

##### 2. Post publishing
For a post to publish involves two API calls - 
- First POST request with a payload of image url which is uploaded to Amazon S3 Bucket and caption(optional) responds with a Creation ID which represents that particular post.
- Second POST request with a payload of Creation ID actually publishes the post in [instagram account](https://www.instagram.com/___scrivener___/)

That Instagram Account => [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" width="50"/>](insta.png)

