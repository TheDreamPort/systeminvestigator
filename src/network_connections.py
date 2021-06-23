import csv
import logging

import psutil

from intelligence import intelligence

class network_connections( intelligence ):
    def __init__( self, output_type='csv' ):
        super(network_connections, self).__init__( output_type='csv' )
        
    def run( self ):
        self.logger.info( 'running network connections' )
