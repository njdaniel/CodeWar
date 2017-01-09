def likes(names):
    """prints out names of people who liked"""
    likes = names
    others = len(likes) - 2
    if not likes:
         print('no one likes this')
    if len(likes) == 1:
        print('%s likes this' % likes[0])
    elif len(likes) == 2:
        print('%s and %s likes this' % (likes[0], likes[1]))
    elif len(likes) == 3:
        print('%s, %s and %s likes this' % (likes[0], likes[1], likes[2]))
    elif len(likes) == 4:
        print('%s, %s and %d likes this' % (likes[0], likes[1], others))

def likes_solution(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

likes(['Peter', 'John', 'bob'])