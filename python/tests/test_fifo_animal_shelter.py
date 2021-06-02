import pytest
from fifo_animal_shelter.fifo_animal_shelter import Node, Queue, AnimalShelter


def test_import():
  assert Node and Queue and AnimalShelter
  
def test_instance():
  shelter = AnimalShelter(Queue(), Queue())
  assert shelter
  
def test_enqueue():
  shelter = AnimalShelter(Queue(), Queue())
  shelter.enqueue('cat')
  assert shelter.cats.front.value in shelter.cat_names
  
def test_dequeue():
  shelter = AnimalShelter(Queue(), Queue())
  shelter.enqueue('cat')
  shelter.enqueue('cat')
  shelter.enqueue('dog')
  shelter.enqueue('dog')
  assert shelter.dequeue('dog') in shelter.dog_names
  
def test_dequeue_2():
  shelter = AnimalShelter(Queue(), Queue())
  shelter.enqueue('cat')
  shelter.enqueue('cat')
  shelter.enqueue('dog')
  shelter.enqueue('dog')
  shelter.dequeue('cat')
  shelter.dequeue('cat')
  assert shelter.cats.front == None
  
def test_no_animal_type_specified_for_dequeue():
  shelter = AnimalShelter(Queue(), Queue())
  shelter.enqueue('cat')
  shelter.enqueue('cat')
  shelter.enqueue('dog')
  shelter.enqueue('dog')
  assert shelter.dequeue() == None
  
  