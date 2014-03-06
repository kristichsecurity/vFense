import logging

from time import mktime
from datetime import datetime
from vFense.agent import *
from vFense.db.client import r , db_connect

import os
import settings

logging.config.fileConfig(os.path.join(ROOT_ETC, 'logging.config'))
logger = logging.getLogger('agentstatus')

def all_agent_status():
    seconds = mktime(datetime.now().timetuple()) - 600
    try:
        conn = db_connect()
        (
            r
            .table(AgentsCollection)
            .filter(
                lambda x:
                x[AgentKey.LastAgentUpdate].to_epoch_time() < seconds
            )
            .update({AgentKey.AgentStatus: 'down'})
            .run(conn)
        )
        conn.close()

    except Exception as e:
        logger.exception(e)
