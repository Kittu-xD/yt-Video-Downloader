YT-Video-Downloader
---

> YouTube Video Downloader without using pytube library.

1) The code is a basic implementation of a YouTube video downloader using the requests library in Python.

2) It makes a `request` to the given URL and extracts the video URL from the response.

3) If the video URL is successfully extracted, it is saved to a file named `video.mp4` .

4) If there is an error, an exception is raised and the error message is printed.

5) We use `stream=True` when making a request for the video. This allows us to download the video in chunks, instead of all at once, which can save memory and make the code more efficient.

6) This code uses the `requests` library to make a request to the URL, and the `re` library to extract the video URL from the response. The video is then saved to a file on the local file system. Exception handling is added to catch any errors that may occur during the process.

7) In the code, the regular expression <b>`r'(?<=<source src=")(.*?)(?=")'`</b> is used to extract the video URL from the response. If no match is found, the search method returns None. The `.group()` method is then called on the result of the search. <br>
---

>> However, please note that downloading videos from YouTube is against their terms of service and could result in legal consequences.
---


