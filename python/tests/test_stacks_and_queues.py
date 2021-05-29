import pytest
from stacks_and_queues.stacks_and_queues import Node, Stack, Queue

def test_stack_import():
  assert Stack
  
def test_node_import():
  assert Node
  
def test_stack_push():
  s = Stack()
  s.push('hello world')
  assert s.top.value == 'hello world'
  
def test_stack_push_many():
  s = Stack()
  s.push('hello world')
  s.push('multiple values woah')
  assert s.top.value == 'multiple values woah'
  
def test_stack_pop():
  s = Stack()
  s.push('hello world')
  s.push('multiple values woah')
  s.pop()
  assert s.top.value == 'hello world'
  
def test_empty_after_multiple_pops():
  s = Stack()
  s.push('hello world')
  s.push('multiple values woah')
  s.pop()
  s.pop()
  assert s.top == None
  
def test_stack_peek():
  s = Stack()
  s.push('hello world')
  s.push('quit peeking')
  assert s.peek() == 'quit peeking'
  
def test_instantiate_empty_stack():
  s = Stack()
  assert s.top == None
  
def test_empty_stack_pop():
  s = Stack()
  assert s.pop() == 'this stack is empty buddy'
  
def test_empty_stack_peek():
  s = Stack()
  assert s.peek() == 'this stack is empty buddy'
  
# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception

def test_queue():
  assert Queue
  
def test_enqueue():
  q = Queue()
  q.enqueue('first value')
  assert q.front.value == 'first value'
  
def test_enqueue_multiple():
  q = Queue()
  q.enqueue('first value')
  q.enqueue('second value')
  assert q.front.value == 'first value'
  
def test_dequeue():
  q = Queue()
  q.enqueue('first value')
  q.enqueue('second value')
  assert q.dequeue() == 'first value'
  
def test_queue_peek():
  q = Queue()
  q.enqueue('first value')
  q.enqueue('second value')
  assert q.peek() == 'first value'
  
def test_multiple_dequeue():
  q = Queue()
  q.enqueue('first value')
  q.enqueue('second value')
  q.dequeue()
  q.dequeue()
  assert q.front == None
  
def test_instantiate_empty_queue():
  q = Queue()
  assert q.front == None
  
def test_peek_empty_queue():
  q = Queue()
  assert q.peek() == 'this queue is empty buddy'
  
def test_dequeue_empty_queue():
  q = Queue()
  assert q.dequeue() == 'this queue is empty buddy'