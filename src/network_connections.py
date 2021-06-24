import csv
import logging

import psutil

from intelligence import intelligence

class network_connections( intelligence ):
    def __init__( self, output_type='csv' ):
        super(network_connections, self).__init__( output_type='csv' )
        
    def run( self ):
        self.logger.info( 'running network connections' )
        open_network_connections = psutil.net_connections()
        self.default_headers = [ 'fd', 'family', 'type', 'status', 'pid', 'laddr', 'lport', 'raddr', 'rport' ]
        for nc in open_network_connections:
            r = {
                    'fd': nc.fd,
                    'family': nc.family,
                    'type': nc.type,
                    'status': nc.status,
                    'pid': nc.pid
                }

            if len( nc.laddr ) > 0:
                r['laddr'] = nc.laddr[0]
                r['lport'] = nc.laddr[1]
                
            if len( nc.raddr ) > 0:
                r['raddr'] = nc.raddr[0]
                r['rport'] = nc.raddr[1]

            self.add_result( r )
