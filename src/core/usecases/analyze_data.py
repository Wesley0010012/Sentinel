from ..protocols.anomaly_notifier import AnomalyNotifier
from ..dto.analyze_data_input import AnalyzeDataInput
from ..protocols.schemas_repository import SchemasRepository
from ..protocols.schema_tester_factory import SchemaTesterFactory

class AnalyzeData:
    def __init__(
        self,
        schemas_repository: SchemasRepository,
        schema_tester_factory: SchemaTesterFactory,
        anomaly_notifier: AnomalyNotifier,
    ):
        self._schemas_repository = schemas_repository
        self._schema_tester_factory = schema_tester_factory
        self._anomaly_notifier = anomaly_notifier

    def execute(self, input: AnalyzeDataInput):
        schema = self._schemas_repository.findLatestBySignature(input.signature)

        if schema is None:
            self._anomaly_notifier.notify_schema_not_found(input.signature)
            return

        schema_tester = self._schema_tester_factory.build(schema)

        schema.data_to_test = input.data_to_test

        if not schema_tester.test(schema):
            self._anomaly_notifier.notify_schema_anomaly(schema)
            return