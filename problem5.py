# Competive Programming
# Problem 5
'''
Name : Mithun. T
Programme : B.Tech(CSE)
Section : 'D'
Year : 1st year
Register No. : RA2411003020254
'''

glassStack = list() 
def isEmpty(glassStack):
     if len(glassStack) == 0:
          return True
     else:
          return False
     
def opPush(glassStack, element):
     glassStack.append(element)

def size(glassStack):
     return len(glassStack)

def peek(glassStack):
     if isEmpty(glassStack):
          print("Stack is Empty")
          return None
     else:
          x = len(glassStack)
          element = glassStack[x-1]
          return element

def opPop(glassStack):
     if isEmpty(glassStack):
          print("Underflow")
          return None
     else:
          return (glassStack.pop())

def display(glassStack):
     x = len(glassStack)
     print("Current elements in the stacks are: ")
     for i in range(x-1, -1, -1):
          print(glassStack[i])

glassStack = list() 

while True:
     print('''
1. Push element to the stack
2. Pop an element from the stack
3. Display the Peek(top) element added to the stack
4. Exit
''')
     ch = int(input("Enter the choice number : "))
     if ch == 1:
          element = input("Enter the element to add : ")
          print("Pushing elment: ", element)
          opPush(glassStack, element)
     elif ch == 2:
          element = opPop(glassStack)
          print("Popped element is", element)
     elif ch == 3:
          print("Top element --> ", peek(glassStack))
     elif ch == 4:
          print("Program Closed...!")
          break
     else:
         print("Invalid Choice!!!")
         continue
