# Its useful when we have to acquire and release resources

# Examples:

# Option 1
# context manager make sure to close 'notes.txt'
# with open('notes.txt') as file:
#     file.write('some todo')

# Option2
# anternaty way
# file = open('notes.txt', 'w')
# try:
#     file.write('some todo ...')
# finally:
#     file.close

# Option 1 and 2 are the same

# Another example for context manager is when using locks

# You can create your own context manager object
# You mainly need to override the functions __enter__ and __exit__
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename
    
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('note.txt') as file:
    file.write('some todo from kent')
