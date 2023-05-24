
import aiohttp

# In this example aiohttp is used.
# This needs to be used in an async function.
# This is simply for demonstrative purposes, you can use
# any library for this.

# The only supported headers are User-Agent and Authorization
# Please change the user-agent as it's useful for identification purposes.
# This endpoint does not require a token but some others do.


headers = {'Accept-Version':'v5', 'User-Agent': f'aiohttp/{aiohttp.__version__}; YourAppName'}

# Here let's say you want to exclude some images, disable gifs and request only safe pictures
# The url is written in multiple lines for readability purposes, but it is equal to:
# https://api.waifu.im/search/?excluded_files=3867126be8e260b5&excluded_files=3133&gif=false&excluded_tags=maid&excluded_tags=oppai&is_nsfw=false
# You can also provide params as a dict or a list of tuple with the 'params' kwarg
url = "https://api.waifu.im/search/?excluded_files=4401" \
      "&excluded_files=3133" \
      "&gif=false" \
      "&excluded_tags=maid" \
      "&excluded_tags=oppai" \
      "&is_nsfw=false"


# Usually you would create a session and access it when needed.
session = aiohttp.ClientSession()

async with session.get(url, headers=headers) as resp:
    api = await resp.json()
    if resp.status in {200, 201}:
        url = api['images'][0]['url']
    # Do whatever you want with the image url.
    else:
        error = api['detail']
    # Do whatever you want with the error description.
                    