import time
from PIL import ImageDraw, ImageFont, Image
import textwrap
import boto3
import os
from dotenv import load_dotenv
import urllib.request
import json
import uuid
load_dotenv()

uid = str(uuid.uuid4())
SECRET_KEY = os.getenv("AWS_SECRET_KEY")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
BUCKET = os.getenv("S3_BUCKET")
FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")


def generate_image():
    # urllib.request.urlretrieve(
    # "https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg.png", "gfg.jpg")
    response = urllib.request.urlopen("https://api.quotable.io/random")
    global response_text
    response_text = json.loads(response.read().decode("utf-8"))
    # print(response_text)
    value = """{}""".format(response_text["content"])
    wrapper = textwrap.TextWrapper(width=30)
    word_list = wrapper.wrap(text=value)

    im = Image.open("bg.jpg")
    I1 = ImageDraw.Draw(im)
    myFont = ImageFont.truetype('./Fuzzy_Bubbles/FuzzyBubbles-Bold.ttf', 65)
    y = 360
    for element in word_list:
        I1.text((200, y), element,
                font=myFont, fill=(0, 0, 0))
        y += 70
    myFont = ImageFont.truetype('./Fuzzy_Bubbles/FuzzyBubbles-Bold.ttf', 25)
    I1.text((900, 700), "- {}".format(response_text["author"]),
            font=myFont, fill=(0, 0, 0))
    # im.show()
    im.save("output.jpg")


def upload_image():
    client_s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY)
    client_s3.upload_file('output.jpg'.format(uid), BUCKET, 'output-{}.jpg'.format(uid), ExtraArgs={
        'ContentType': 'image/jpeg'})


def publish_image():
    image_url = "https://{}.s3.ap-south-1.amazonaws.com/output-{}.jpg".format(
        BUCKET, uid)
    caption = "%23quotes"
    for tag in response_text["tags"]:
        if tag == "famous-quotes":
            caption = "%23famousquotes"
            continue
        caption = "%23" + tag + "%20" + caption
    # print(caption)
    response = urllib.request.Request(
        "https://graph.facebook.com/v15.0/17841448545960382/media?image_url={}&caption={}&access_token={}".format(image_url, caption, FB_ACCESS_TOKEN), method="POST")
    # print(response.__dict__)
    r = urllib.request.urlopen(response)
    creation_id = json.loads(r.read().decode("utf-8")).get("id")
    # print(creation_id)
    r = urllib.request.Request(
        "https://graph.facebook.com/v15.0/17841448545960382/media_publish?creation_id={}&access_token={}".format(creation_id, FB_ACCESS_TOKEN), method="POST")
    urllib.request.urlopen(r)
    # print(r.read().decode("utf-8"))


if __name__ == "__main__":
    generate_image()
    upload_image()
    publish_image()
    # time.sleep(200)
