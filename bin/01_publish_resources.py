#!/usr/bin/env python

import os
import radical.utils as ru

dburl = 'mongodb://144.76.72.175/am'
pwd   = os.path.dirname(__file__)

if __name__ == '__main__':

    mongo, db, _, _, _ = ru.mongodb_connect(str(dburl))

    coll  = db['rp.session.thinkie.merzky.017354.0030']
    coll.insert(ru.read_json('%s/01_publish_resources.json' % pwd))


