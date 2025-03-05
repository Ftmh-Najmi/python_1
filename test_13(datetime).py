from datetime import datetime, timedelta

start = datetime.now()
end = start+timedelta(days=30)

print(end - start)

