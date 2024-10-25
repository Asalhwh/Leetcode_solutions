class MyQueue(object):

    def __init__(self):
        self.Q=[]
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.Q)==0:
            return"Queue is empty"
        else:
            return self.Q.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if len(self.Q)==0:
            return -1
        else:
            for i in self.Q:

                return self.Q[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.Q)==0:
            return True
        else:
            return False