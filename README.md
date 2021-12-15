# RemoveBG_API
small app for removing the background from you pictures using the API from https://www.remove.bg/

# How to use it:

- change the dummy path within the folder_path.txt file;
- execute the run.py file;

# How it works:

- reads the folder path from the txt file;
- creates a new folder - 'no_bg_pics' if not existing;
- extracts a list of each file within the folder;
- using the remove.bg API, sends each pic as request to the api;
- if the response is OK, then writes the no background file in the proper folder;

# Errors:

- 429 - rate limit - remove.bg API offers a rate up to 500pic/minute;
- 402 - insuficient credits - for free acount the API offers 50pic/month;
- for the free account the images should be < 12 MB;