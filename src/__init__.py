import logging
from processes import *

logger = logging.getLogger( )

def collect( intelligence_type ):
    collectors = []
    logger.info( 'creating a collector' )
    if intelligence_type.lower() == 'process':
        collectors.append( processlist() )

    return collectors
    