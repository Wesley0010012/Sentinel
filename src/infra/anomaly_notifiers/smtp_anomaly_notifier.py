import smtplib
from email.message import EmailMessage
from typing import List
from ...core.protocols.anomaly_notifier import AnomalyNotifier
from ...core.entities.schema import Schema


class SMTPAnomalyNotifier(AnomalyNotifier):
    def __init__(self, config: dict):
        self._host = config.get("host")
        self._port = config.get("port", 587)
        self._username = config.get("username")
        self._password = config.get("password")
        self._from_email = config.get("from_email")
        self._to_emails: List[str] = config.get("to_emails", [])
        self._use_tls = config.get("use_tls", True)

    def notify_schema_not_found(self, schema_signature: str) -> None:
        subject = "[SENTINEL] Schema não encontrado"
        body = f"Schema não encontrado para signature: {schema_signature}"

        self._send_email(subject, body)

    def notify_schema_anomaly(self, schema: Schema) -> None:
        version_number = getattr(schema.version, "number", None)
        created_at = getattr(schema.version, "created_at", None)

        subject = "[SENTINEL] Anomalia detectada em Schema"
        body = (
            f"Anomalia detectada:\n\n"
            f"ID: {schema.id}\n"
            f"Signature: {schema.signature}\n"
            f"Type: {schema.type.value}\n"
            f"Payload: {schema.data_to_test}\n" 
            f"Version: {version_number}\n"
            f"Created At: {created_at}\n"
        )

        self._send_email(subject, body)

    def _send_email(self, subject: str, body: str) -> None:
        print('enviando e-mail')
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self._from_email
        msg["To"] = ", ".join(self._to_emails)
        msg.set_content(body)

        with smtplib.SMTP(self._host, self._port) as server:
            if self._use_tls:
                server.starttls()

            if self._username and self._password:
                server.login(self._username, self._password)

            server.send_message(msg)