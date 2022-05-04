TEMP_FILENAME_CHARSET = "0123456789abcdef"
ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
REAL_IP_HEADER = 'X-Real-IP'

BODY_TYPE_NORMAL = 1
BODY_TYPE_ESCAPED = 2
BODY_TYPE_TOO_LONG = 3

USER_TYPE_SUPER_ADMIN = 1
USER_TYPE_NORMAL = 2

RULE_TYPE_STATIC_FILE = 1
RULE_TYPE_DYNAMIC_TEMPLATE = 2
RULE_TYPES = {RULE_TYPE_STATIC_FILE, RULE_TYPE_DYNAMIC_TEMPLATE}

PUBLISH_MESSAGE_TYPE_NEW_HTTP_ACCESS_LOG = 1
PUBLISH_MESSAGE_TYPE_NEW_DNS_LOG = 2

WEBSOCKET_TIMEOUT = 20

LOG_TYPE_LOGIN = 1
LOG_TYPE_TEMPLATE_ERROR = 2
LOG_TYPE_MAIL_SEND_ERROR = 3
LOG_TYPE_SYSTEM_ERROR = 4

JWT_HEADER = "Authorization"
CONFIG_INIT_KEY = 'INITED'

DNS_LRU_CACHE = 1024
