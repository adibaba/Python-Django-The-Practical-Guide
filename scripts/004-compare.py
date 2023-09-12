# e.g. https://github.com/adibaba/django-practical-guide-course-code/compare/e4956b0..1ef4b0b
url_prefix = 'https://github.com/adibaba/django-practical-guide-course-code/compare/'
url_prefix_branch = 'https://github.com/adibaba/django-practical-guide-course-code/tree/'
prefixlen = len('remotes/origin/')
last_commit = ''
is_remote = False
is_commit = False
for line in open('003-hashes.txt', 'r').readlines():
    line = line.strip()
    if len(line) < 1:
        continue
    if line.startswith('002-branches.txt'):
        continue
    if line.startswith('remotes/origin/HEAD'):
        continue
        
    is_remote = True
        
    if is_commit:
        is_remote = False
        is_commit = False
        commit = line[0:7]
        
        #print(commit, remote)
        
        # compare urls
        #print(url_prefix + last_commit + '..' + commit)
        
        # compare links
        print('- [Changes]' + '(' + url_prefix + last_commit + '..' + commit + ') and')
        print('  [Code]' + '(' + url_prefix_branch + remote + ')')
        print('  for ' + remote + ')')
        
        last_commit = commit
        commit = ''
        remote = ''
    
    if is_remote:
        is_remote = False
        is_commit = True
        remote = line[prefixlen:]