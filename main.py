#!/usr/bin/env python3

import sys

from uczacz.app import Uczacz

sys.path.append('..')

app = Uczacz()

if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print('\n(E) %s' % e, end='\n\n')
    finally:
        print('\nBye..')
