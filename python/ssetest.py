from sseclient import SSEClient

rets =[]
for i in range(5):
    messages = SSEClient('http://121.42.12.11:81/subscribe')
    rets.append(messages)

while True:
    for item in rets:
        for msg in messages:
            print msg
            break
