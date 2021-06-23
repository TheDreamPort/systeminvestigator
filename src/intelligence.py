import csv
import io   
import logging


class intelligence:
    def __init__( self, output_type='csv' ):
        self.logger = logging.getLogger( __name__ )
        self.output_type = output_type
        self.results = []
        self.default_headers = []

    def add_result( self, result_object ):
        self.results.append( result_object )

    def run( self ):
        raise NotImplementedError("This is the base-class behavior for RUN(), please call a child class!")

    def to_csv( self ):
        self.logger.info( 'convert to CSV' )
        output = io.StringIO()
        writer = csv.DictWriter( output, fieldnames=self.default_headers ) 
        writer.writeheader()
        for r in self.results:
            writer.writerow( r )
        return output.getvalue( )