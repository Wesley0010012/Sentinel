import logging
from ...core.protocols.anomaly_notifier import AnomalyNotifier
from ...core.entities.schema import Schema

logger = logging.getLogger(__name__)


class LoggingAnomalyNotifier(AnomalyNotifier):

    def notify_schema_not_found(self, schema_signature: str) -> None:
        logger.warning(
            f"[SCHEMA NOT FOUND] signature={schema_signature}"
        )

    def notify_schema_anomaly(self, schema: Schema) -> None:
        version_number = getattr(schema.version, "signature", None)
        created_at = getattr(schema.version, "created_at", None)

        logger.error(
            "[SCHEMA ANOMALY] "
            f"id={schema.id} "
            f"signature={schema.signature} "
            f"type={schema.type} "
            f"payload={schema.data_to_test}"
            f"version={version_number} "
            f"created_at={created_at}"
        )