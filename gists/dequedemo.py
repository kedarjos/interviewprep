from collections import deque

if __name__ == "__main__":
    d = deque('abcd')
    
    print(d)
    # deque(['a', 'b', 'c', 'd'])

    print(d[0])
    # a

    print(d[-1])
    # d

    d.appendleft('z')
    # deque(['a', 'b', 'c', 'd', 'z'])

    # insert at right end
    d.extend('s')
    # deque(['z', 'a', 'b', 'c', 'd', 's'])

    d.remove('c')
    # deque(['z', 'a', 'b', 'd', 's'])

    d.rotate(1)
    # deque(['s', 'z', 'a', 'b', 'd'])
    # If the rotate index is negative, rotation is done from other side.

    d.pop()
    # deque(['s', 'z', 'a', 'b']

    d.popleft()
    # deque(['z', 'a', 'b'])

    # append and extend methods will add elements to right end
    # appendleft and extendleft methods will add elements to left end
    # extend methods take iterable objects as input and append methods take a single
    # value as inputs.
    # So for using append only: append and appendleft
    # for using extend only: extend and extendleft
    """
    # Add to the right
    d = collections.deque()
    d.extend('abcdefg')
    print 'extend    :', d
    d.append('h')
    print 'append    :', d

    # Add to the left
    d = collections.deque()
    d.extendleft('abcdefg')
    print 'extendleft:', d
    d.appendleft('h')
    print 'appendleft:', d 
    """