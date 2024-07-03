from sync import client

if __name__ == "__main__":
    pubsub = client.pubsub()
    pubsub.subscribe("channel")
    for msg in pubsub.listen():
        print(msg)
