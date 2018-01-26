#!/usr/bin/env python

import sys

def main():
    """
    This about for sys module usage test
    include:
            1: sys.argv
            2: sys.path
            3: sys.platform
            4: sys.builtin_module_names
            5: sys.exit
    """

    print ("This program name is %s" % sys.argv[0])

    if len(sys.argv) < 2:
        print ("args too few")

        # when sys.exit(1) not 0, will pust abnormal 'SystemExit', can catch this abnormal.
        """
            try:
                sys.exit(1)
            except SystemExit:
                print ('sys.exit is 1')
        """
        sys.exit(0)
    else:
        print ("argv[%d] = %s  argv[%d] = %s" % (0, sys.argv[0], 1, sys.argv[1]))

    
    # check run proform is Windows or Linux
    print ('This run proform is %s' % sys.platform)

    # include sys.path.insert(0, 'test') and sys.path.append('test')
    print ('the third module:')
    print (sys.path)

    # return list, this list include builtin module names.
    print ('buildin module name:')
    print (sys.builtin_module_names)
    if 'os' in sys.builtin_module_names:
        print ('os => __builtin__')
    else:
        print ('os => __inport__(module).__file__')

    
    


if __name__ == '__main__':
    main()
