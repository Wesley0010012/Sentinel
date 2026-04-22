import json
import redis


def seed():
    client = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True
    )

    queue_name = "sentinel:schemas"

    messages = [
        {
            "signature": "xml-signature",
            "data": "<note>Hello</note>"
        },
        {
            "signature": "xml-signature",
            "data": "<note><title>Hi</title><body>World</body></note>"
        },
        {
            "signature": "json-signature",
            "data": '{"name": "John"}'
        },
        {
            "signature": "json-signature",
            "data": '{"name": "John", "age": 30}'
        }
    ]

    for msg in messages:
        client.lpush(queue_name, json.dumps(msg))

    print(f"Seeded {len(messages)} messages into {queue_name}")


if __name__ == "__main__":
    seed()