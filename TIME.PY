from datetime import datetime
import pytz
b=pytz.timezone("Asia/kathmandu")
res=datetime.now(b)
print(res)