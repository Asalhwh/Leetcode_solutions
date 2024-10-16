class MyStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):#This method pushes elements onoto top of stack
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)!=0:
            self.stack.append(x)
        else:
            return -1

    def pop(self):#This method shows the top element and also delete it.
        """
        :rtype: int
        """
        if len(self.stack)>0:
            self.stack.pop()
        else:
            return -1

    def top(self):#This will just shows the top as well as peek
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return -1
        else:
            return self.stack[len(self.stack)-1]

    def empty(self):#It checks whether the stack is empty or not
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        else:
            return False
             
