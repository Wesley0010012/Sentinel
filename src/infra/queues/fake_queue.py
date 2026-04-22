from ...core.protocols.queue_protocol import QueueProtocol

class FakeQueue(QueueProtocol):
    def __init__(self):
        self._messages = [
            {
                "signature": "xml-signature",
                "data": "<note>Hello</note>"
            },
            {
                "signature": "json-signature",
                "data": '{"name": "John"}'
            }
        ]

    def consume(self):
        if not self._messages:
            return None

        return self._messages.pop(0)