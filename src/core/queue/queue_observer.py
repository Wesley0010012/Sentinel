from ..usecases.analyze_data import AnalyzeData
from ..dto.analyze_data_input import AnalyzeDataInput
from ..protocols.queue_protocol import QueueProtocol


class QueueObserver:
    def __init__(self, queue: QueueProtocol, use_case: AnalyzeData):
        self._queue = queue
        self._use_case = use_case

    def start(self) -> None:
        while True:
            message = self._queue.consume()

            if message is None:
                continue

            try:
                input_data = self._to_input(message)
                self._use_case.execute(input_data)
            except Exception as e:
                print(f"[QUEUE ERROR] {e}")

    def _to_input(self, message: dict) -> AnalyzeDataInput:
        signature = message.get("signature")
        data = message.get("data")

        if not signature or not data:
            raise ValueError("Mensagem inválida: signature ou data ausente")

        return AnalyzeDataInput(
            signature=signature,
            data_to_test=data
        )