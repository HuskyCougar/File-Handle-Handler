#!/usr/bin/python3

# https://github.com/HuskyCougar/File-Handle-Handler
# https://github.com/HuskyCougar/File-Handle-Handler/blob/master/file_handle_handler.py
# file_handle_handler.py

########################################################################
##                        File Handle Handler                         ##
########################################################################

#region    ## File Handle Handler ######################################

from pathlib import Path
import gzip
import os

fhh_file_handles = {}

def fhh_write_str_to_file( fhh_path , fhh_str ) :

    '''File Handle Handler. This function, along with the global fhh_file_handles
    dictionary and the fhh_close_filehandles provides a mechanism for efficiently 
    writing strings to various files, handling compressed formats, and managing 
    file handles for proper closing. This is very handy when you are reading 
    data that needs to be written to an unknown number of different files.'''

    try :

        ## If a file handle is already open this will work
        fhh_file_handles[ fhh_path ].write( "%s\n" % fhh_str )
        fhh_file_handles[ fhh_path ].flush()

    except KeyError :

        ## If there is no handle for this file, try this
        try :

            ## Open a file handle
            if   ( fhh_path.endswith( ".gz" ) ) : fh = gzip.open( fhh_path , 'wt' , compresslevel=6 , encoding="utf-8" )
            else                                : fh =      open( fhh_path , 'w'                    , encoding="utf-8" )

            print( f'# Opening new file handle : {fhh_path}' )

            ## A handle is open now. Write to it
            fh.write( "%s\n" % fhh_str )
            fh.flush()

            ## Add our filehandle to a dictionary with the path string as a key
            fhh_file_handles[ fhh_path ] = fh

        except FileNotFoundError :

            ## if the folder does not exist, create it
            fhh_path_path , fhh_path_file = os.path.split( fhh_path )
            Path( fhh_path_path ).mkdir( parents = True , exist_ok = True )
            print( f'# Creating new folder : {fhh_path_path}' )

            ## you know whats going by now.

            if   ( fhh_path.endswith( ".gz" ) ) : fh = gzip.open( fhh_path , 'wt' , compresslevel=6 , encoding="utf-8" )
            else                                : fh =      open( fhh_path , 'w'                    , encoding="utf-8" )

            print( f'# Opening new file handle : {fhh_path}' )

            fh.write( "%s\n" % fhh_str )
            fh.flush()

            fhh_file_handles[ fhh_path ] = fh


def fhh_close_filehandles() :

    for fhh_path in fhh_file_handles :
        print( f'# Closing file handle : {fhh_path}' )
        fhh_file_handles[ fhh_path ].close()

    fhh_file_handles.clear()

#endregion ## File Handle Handler ######################################
