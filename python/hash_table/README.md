# Hashtables
Hashtables take a key and assign a value to it. the key is hashed to a unique value, and that value is used as an index in an array to achieve O(1) lookup times. to handle collisions, buckets are used to store multiple keys and values.

## Challenge
create a hashtable class that has the methods add, get, hash, and contains

## Approach & Efficiency
i used an array of arrays for storage. arrays are quick to look up and slow to delete something, but i thought there wouldnt be a lot of deleting as usually hashtables are used for adding stuff and referring to to see whether youve seen something or not, not deleting data frequently.

## API
the hash method hashes the key to a unique number somewhere in range of the size of the array. 
the add method uses the hash function to find an index for the key, and then stores the tuple of (key, value) in the array position. it checks to see if theres already something there in the hash index, and if there is, it makes another slot for itself.
the contains method hashes the key and goes to see if the key is in the hash index. it returns a boolean whos value depends on if the key is in the hash table or not.
the get method hashes the key, goes to the hash index, and finds the correct key position by looping through the contents of the bucket. it returns the value.
the find collision key method finds a key that will hash to the same index as a given key, and then returns that collision key string.