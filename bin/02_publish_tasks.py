#!/usr/bin/env python

import os
import sys
import radical.utils as ru

dburl = 'mongodb://144.76.72.175/am'
pwd   = os.path.dirname(__file__)
N     = 42

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise RuntimeError('expect sesson ID as argument')
    sid = sys.argv[1]

    tasks = list()
    for i in range(N):

        tasks.append({'executable' : '/bin/date',
                      'arguments'  : ['-R', '-u'],
                      'environment': {'TIMEZONE' : 'utc'},
                      'cores'      : 1,
                      'uid'        : ru.generate_id('unit'),
                      'pilot'      : None
                      })

    mongo, db, _, _, _ = ru.mongodb_connect(str(dburl))

    coll  = db[sid]

    for task in tasks:
        task['type'] = 'unit'
        task['_id']  = task['uid']
        coll.insert(task)
    print 'inserted %s tasks in %s' % (len(tasks), sid)
