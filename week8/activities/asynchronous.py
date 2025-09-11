import aiohttp

async def fetch_metadata(doc_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://jsonplaceholder.typicode.com/posts/{doc_id}"
        async with session.get(url) as resp:
            data = await resp.json()
            return data