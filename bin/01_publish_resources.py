#!/usr/bin/env

# This demonstrator connects to a MongoDB, creates a collection 'panda.nge',
# and publishes information about RP pilot instances, in the following form:
#
# {
#   'session' : rp.session.nge,001122', 
#   'pmgr'    : [
#     {  
#       'uid'    : 'pmgr.0000',
#       'pilots' : [
#         { 
#           'uid'       : 'pilot.0000', 
#           'cores'     : 128,
#           'submitted' : 12312768,        # seconds since epoch
#           'started'   : null,            # not yet started
#           'runtime'   : 60,              # minutes
#           'state'     : 'rp.LAUNCHING',  # rp level state string
#           'control'   : 'panda_pending'  # pickup to be confirmed
#         }, 
#         ...
#       ]
#     }
#   ]
# }
#      
#
#
# The 'control' entry in the pilot dict are used to coordinate ownership of the
# respective entries.
#
