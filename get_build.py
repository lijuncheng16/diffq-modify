from pathlib import Path
import requests
import zipfile

root = Path('dist')
root.mkdir(exist_ok=True, parents=True)

token = open('misc/token.txt').read().strip()
headers = {'Authorization': 'token ' + token}
query_url = "https://api.github.com/repos/facebookresearch/diffq/actions/artifacts"

res = requests.get(query_url, headers=headers).json()['artifacts'][0]
url = res['archive_download_url']
print(res['created_at'], url)
r = requests.get(url, headers=headers, stream=True)
with open(root / 'build.zip', 'wb') as f:
    while True:
        d = r.raw.read(2 ** 16)
        if not d:
            break
        f.write(d)

