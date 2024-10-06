from src.core.config import settings
from src.core.loggers import core as logger

logger.debug(f'''Database settings:
host={settings.db_host}
port={settings.db_port}
name={settings.db_name}
username={settings.db_user}
password={settings.db_pass}
url={settings.db_url}''')
