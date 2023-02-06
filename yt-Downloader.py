import requests
import re

__author__ = "Kartik Aggarwal"


def download_video(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Extract the video URL from the response
            video_url = re.search(r'(?<=<source src=")(.*?)(?=")', response.text)

            # Check if the video URL was successfully extracted
            if video_url:
                video_url = video_url.group()
                # Save the video to a file
                with open('video.mp4', 'wb') as f:
                    video = requests.get(video_url)
                    f.write(video.content)

                print("Video downloaded successfully!")
            else:
                raise Exception("Unable to extract video URL.")
                
                return
        else:
            raise Exception("Request to URL failed with status code {}.".format(response.status_code))
    except Exception as e:
        print("An error occurred: {}".format(e))


url = input("Enter the URL of the YouTube video: ")
download_video(url)
input()
