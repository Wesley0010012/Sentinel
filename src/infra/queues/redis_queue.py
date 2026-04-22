import json
import redis
from typing import Optional
from ...core.protocols.queue_protocol import QueueProtocol


class RedisQueue(QueueProtocol):
    def __init__(self, config: dict):
        """
        Exemplo de config:
        {
            "host": "localhost",
            "port": 6379,
            "db": 0,
            "password": None,
            "queue_name": "sentinel:schemas:queue",
            "timeout": 5
        }
        """
        self._queue_name = config.get("queue_name", "schemas")
        self._timeout = config.get("timeout", 5)

        self._client = redis.Redis(
            host=config.get("host", "localhost"),
            port=config.get("port", 6379),
            db=config.get("db", 0),
            password=config.get("password"),
            decode_responses=True
        )

    def publish(self, message: dict) -> None:
        self._client.lpush(self._queue_name, json.dumps(message))

    def consume(self) -> Optional[dict]:
        result = self._client.brpop(self._queue_name, timeout=self._timeout)

        if not result:
            return None

        _, data = result
        return json.loads(data)