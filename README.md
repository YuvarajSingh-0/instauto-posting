# Instagram Auto Posting

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png" width="40"/>

## Daily automatic Instagram image post
Check out the daily automatic Instagram image posts on [___scrivener___](https://www.instagram.com/___scrivener___/)!

## Tech Stack
The Instagram Auto Posting project utilizes the following technologies:

- **Instagram API**: Part of Facebook's Meta Program, it allows access to Instagram functionalities.
- **Access Token**: Generate a temporary or permanent access token using the Facebook Developers page.
- **Python**: Used for image creation and editing using the Pillow module.
- **Quotes API**: Fetches random quotes to add to the background image.
- **Amazon S3**: Cloud object storage service provided by AWS for storing the created images.
- **API Calls**: Involved in the post publishing process using the Creation ID and image URL.

## Posting Process Overview
This Instagram Auto Posting project follows a two-step process:

1. **Image Creation and Editing**: 
   - A background image is created using Python's Pillow module.
   - A random quote is fetched from the Quotes API and added to the image.
   - The edited image is uploaded to Amazon S3 for storage.

2. **Post Publishing**:
   - First POST request: Sends the image URL (uploaded to Amazon S3) and an optional caption. It returns a Creation ID, representing the post.
   - Second POST request: Uses the Creation ID to publish the post on the Instagram account.

## Usage
To use this project:
1. Obtain the necessary access token from the Facebook Developers page.
2. Configure the Python script with the access token and desired settings.
3. Run the script to automatically create and publish Instagram posts.

Feel free to explore the [___scrivener___](https://www.instagram.com/___scrivener___/) Instagram account for the latest posts!

## Deployment
The Instagram Auto Posting code is deployed on [PythonAnywhere](https://www.pythonanywhere.com/), a platform that allows hosting and running Python applications in the cloud.

## Status
- Current State: :red_circle: **Offline**
- Reason: API calls became costly in the AWS S3 bucket.

## Contributing
Contributions are welcome! If you want to contribute to the Instagram Auto Posting project, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3. Make your modifications and commit them with descriptive messages: `git commit -m "Add your commit message here"`.
4. Push your changes to the new branch on your forked repository: `git push origin feature/your-feature-name`.

Let's collaborate and improve this project together!
