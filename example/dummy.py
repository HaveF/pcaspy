#!/usr/bin/env python

from pcas import Driver, SimpleServer
import time

if __name__ == '__main__':
    prefix = 'MTEST:'
    pvdb = {
        'RAND' : {
            'prec' : 3,
        },
    }

    server = SimpleServer()
    server.createPVs(prefix, pvdb)
    server.createDriver(Driver)

    while True:
        # process CA transactions
        server.process(0.01)
        # give other thread a chance
        time.sleep(0.01)
