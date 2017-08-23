list = []
def add(contact):
    list.append(contact)

def find(contact):
    count = 0
    for c in list:
        if contact in c:
            count += 1
    print count

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == "add":
        add(contact)
    elif op == "find":
        find(contact)
