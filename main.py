import os
from dotenv import load_dotenv
from src.core.usecases.analyze_data import AnalyzeData
from src.core.queue.queue_observer import QueueObserver
from src.infra.schemas_repository.in_memory_schemas_repository import InMemorySchemasRepository
from src.infra.schemas_repository.sqlite_schemas_repository import SqliteSchemasRepository
from src.infra.schemas_repository.mysql_schemas_repository import MySQLSchemasRepository
from src.infra.anomaly_notifiers.logging_anomaly_notifier import LoggingAnomalyNotifier
from src.infra.anomaly_notifiers.smtp_anomaly_notifier import SMTPAnomalyNotifier
from src.infra.testers.default_schema_tester_factory import DefaultSchemaTesterFactory
from src.infra.queues.fake_queue import FakeQueue
from src.infra.queues.redis_queue import RedisQueue

load_dotenv()

REPOSITORY_TYPE = os.getenv("REPOSITORY_TYPE", "memory")  
QUEUE_TYPE = os.getenv("QUEUE_TYPE", "fake")              
NOTIFIER_TYPE = os.getenv("NOTIFIER_TYPE", "log")         

if REPOSITORY_TYPE == "sqlite":
    repository = SqliteSchemasRepository(
        db_path=os.getenv("SQLITE_PATH", "schemas.db")
    )

elif REPOSITORY_TYPE == "mysql":
    repository = MySQLSchemasRepository({
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT", 3306)),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "database": os.getenv("MYSQL_DATABASE"),
    })

else:
    repository = InMemorySchemasRepository()

if NOTIFIER_TYPE == "smtp":
    anomaly_notifier = SMTPAnomalyNotifier({
        "host": os.getenv("SMTP_HOST"),
        "port": int(os.getenv("SMTP_PORT", 587)),
        "username": os.getenv("SMTP_USER"),
        "password": os.getenv("SMTP_PASSWORD"),
        "from_email": os.getenv("SMTP_FROM"),
        "to_emails": os.getenv("SMTP_TO", "").split(","),
        "use_tls": os.getenv("SMTP_TLS", "true").lower() == "true",
    })
else:
    anomaly_notifier = LoggingAnomalyNotifier()

schema_tester_factory = DefaultSchemaTesterFactory()

use_case = AnalyzeData(
    repository,
    schema_tester_factory,
    anomaly_notifier,
)

if QUEUE_TYPE == "redis":
    queue = RedisQueue({
        "host": os.getenv("REDIS_HOST", "localhost"),
        "port": int(os.getenv("REDIS_PORT", 6379)),
        "db": int(os.getenv("REDIS_DB", 0)),
        "password": os.getenv("REDIS_PASSWORD"),
        "queue_name": os.getenv("REDIS_QUEUE", "sentinel:queue"),
        "timeout": int(os.getenv("REDIS_TIMEOUT", 5)),
    })
else:
    queue = FakeQueue()

observer = QueueObserver(queue, use_case)
observer.start()