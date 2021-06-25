from hash_table.hash_table import HashTable, alphabet

def test_imports():
  assert HashTable
  
def test_table_has_add():
  ht = HashTable()
  assert ht.add
  
def test_table_has_get():
  ht = HashTable()
  assert ht.get
  
def test_table_has_contains():
  ht = HashTable()
  assert ht.contains
  
def test_table_has_hash():
  ht = HashTable()
  assert ht.hash
  
def test_add_actually_adds():
  ht = HashTable()
  ht.add('babies', 25)
  assert ht.contains('babies')
  
def test_get_value_works():
  ht = HashTable()
  ht.add('babies', 25)
  assert ht.get('babies') == 25
  
def test_hash_is_in_range():
  ht = HashTable()
  index = ht.hash('babies')
  assert 0 <= index <= 1024
  
def test_multiple_insertions():
  ht = HashTable()
  ht.add('babies', 25)
  ht.add('goats', 99)
  assert ht.get('babies') == 25
  
def test_multiple_insertions_get():
  ht = HashTable()
  ht.add('babies', 25)
  ht.add('goats', 99)
  assert ht.get('goats') == 99
  
def test_random_collision():
  ht = HashTable()
  collision_key = ht.find_collision_key('babies')
  assert (collision_key != 'babies') and (ht.hash('babies') == ht.hash(collision_key))
  
def test_can_retrieve_proper_info_with_collisions():
  ht = HashTable()
  collision_key = ht.find_collision_key('babies')
  ht.add('babies', 55)
  ht.add(collision_key, 10000000)
  assert ht.get('babies') == 55
  
def test_can_retrieve_proper_info_with_collisions2():
  ht = HashTable()
  collision_key = ht.find_collision_key('babies')
  ht.add('babies', 55)
  ht.add(collision_key, 10000000)
  collision_key2 = ht.find_collision_key('goats')
  ht.add('goats', 99)
  ht.add(collision_key2, 9887766554433231)
  assert (ht.get('babies') == 55) and (ht.get('goats') == 99) and (ht.get(collision_key) == 10000000)
  