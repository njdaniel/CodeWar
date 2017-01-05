def likes(names):
    """prints out names of people who liked"""
    likes = names
    if not likes:
         print('no one likes this')
    if len(likes) == 1:
        print('%s likes this' % likes[0])
    elif len(likes) == 2:
        print('%s and %s likes this' % likes[0], likes[1])
    elif len(likes) == 3:
        print('%s, %s and %s likes this' % likes[0], likes[1], likes[2])
    elif len(likes) == 4:
        print('%s, %s and %d likes this' % likes[0], likes[1], (len(likes)-2))

likes(['Peter', 'John', 'Hodor', 'Pico'])