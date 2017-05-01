import time

def name(x):
    def helper(*arg):
        print "%s%s" % (x.func_name, arg)
        return x(*arg)
    return helper

def runtime(x):
    def helper(*arg):
        start  = time.time()
        var = x(*arg)
        end = time.time()
        print "runtime: [%s]" % (str(end - start))
        return var
    return helper

@name
@runtime
def addition (a,b):
    return a + b

print addition (5,7)
print addition ("hello", "potato")
print addition ("hello", "7")
