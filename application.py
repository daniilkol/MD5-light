import sys
from settings import*

id = sys.argv [1]
url = sys.argv [2]
create_json (id = id, status = "running", url = url)

if len (sys.argv) == 3:
    try:
        hash_sum = md5_hash_sum (url)
        create_json (id = id, status = "done", url = url,  md5 = hash_sum)
    except:
        create_json (id = id, status = "failed", url = url)
        sys.exit ()
elif len (sys.argv) == 4:
    try:
        email = sys.argv [3]
        hash_sum = md5_hash_sum (url)
        send_email(email, url + "\n" + hash_sum)
        create_json (id = id, status = "done", url = url, md5 = hash_sum, email = email)
    except:
        create_json (id = id, status = "failed", url = url)
        sys.exit ()