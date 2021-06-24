import logging
from processes import *
from network_connections import *

logger = logging.getLogger( )

def collect( intelligence_type ):
    collectors = []
    logger.info( 'creating a collector' )
    if intelligence_type.lower() == 'process':
        collectors.append( processlist() )
    elif intelligence_type.lower() == 'network':
        collectors.append( network_connections() )

    return collectors
    