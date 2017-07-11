#!/usr/bin/env python

import os
import radical.utils as ru

dburl = 'mongodb://144.76.72.175/am'
pwd   = os.path.dirname(__file__)

if __name__ == '__main__':

    mongo, db, _, _, _ = ru.mongodb_connect(str(dburl))

    sid   = ru.generate_id('rp.session',  mode=ru.ID_PRIVATE)
    coll  = db[sid]
    json  = ru.read_json('%s/01_publish_resources.json' % pwd)

    print 'create session %s' % sid

    for doc in json:
        if doc['type'] == 'session':
            doc['uid'] = sid
            doc['_id'] = sid
        coll.insert(doc)
        print 'insert %s %s' % (doc['type'], doc['uid'])
    print 'inserted session %s' % sid


