# e.g. https://github.com/adibaba/django-practical-guide-course-code/compare/e4956b0..1ef4b0b
url_prefix = 'https://github.com/adibaba/django-practical-guide-course-code/compare/'
url_prefix_branch = 'https://github.com/adibaba/django-practical-guide-course-code/tree/'
prefixlen = len('remotes/origin/')
last_commit = ''
last_block = False
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

    if '-00-' in line:
        last_block = True
        print('\n---\n')
    elif '-01-' in line and not last_block:
        last_block = False
        print('\n---\n')
    elif '-0' in line:
        last_block = False

    if 'setup-zz-extra-files' in line \
    or 'urls-views-zz-extra-files' in line \
    or 'prj-urls-views-templates-zz-extra-files' in line:
        print('\n---\n')
        
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
        print('  for ' + remote)
        
        last_commit = commit
        commit = ''
        remote = ''
    
    if is_remote:
        is_remote = False
        is_commit = True
        remote = line[prefixlen:]