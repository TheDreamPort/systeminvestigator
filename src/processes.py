import csv
import logging

import psutil

from intelligence import intelligence

class processlist( intelligence ):
    def __init__( self, output_type='csv' ):
        super(processlist, self).__init__( output_type='csv' )
        self.default_headers = None
        
    def run( self ):
        self.logger.info( 'running proc' )
        for proc in psutil.process_iter( ):
            r = proc.as_dict( )
            if not self.default_headers:
                self.logger.info( 'set CSV output headers' )
                self.default_headers = r.keys() 

            self.add_result( proc.as_dict() )