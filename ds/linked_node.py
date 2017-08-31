class linked_node:
    def get_data():
        return self.data

    def __init__(self, data):
        print "init called"
        self.data = data

if __name__ == '__main__':
	n = linked_node(1)
