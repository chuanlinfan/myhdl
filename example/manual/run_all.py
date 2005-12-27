modules = ('hello1',
           'hello2',
           'greetings',
           'bin2gray',
           'hec',
           'rs232',
           'mux',
           'mux2',
           'inc',
           'fsm',
           'fsm2',
           'queue',
           'sparseMemory',
           'fifo',
           'rom',
           'ram',
          )

for n in modules:
    m = __import__(n)
    info = "* %s.py *" % m.__name__
    print
    print '*' * len(info)
    print "* %s.py *" % m.__name__
    print '*' * len(info)
    m.main()
