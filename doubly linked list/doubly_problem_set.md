### Question_1: Delete the 3rd Element from the End of a Doubly Linked List
Consider a **Doubly Linked List (dll)**. Write a Python function that deletes the **3rd element from the end** of the list.  
You may assume that `dll` contains **more than 5 elements**.

**For example :**
if the given **dll** is: **3 ↔ 4 ↔ 6 ↔ 32 ↔ 6 ↔ 9 ↔ 6**. 

after calling the function the **dll** should be like this : **3 ↔ 4 ↔ 6 ↔ 32 ↔ 9 ↔ 6**.

### Question_2: Check if a Doubly Linked List is Symmetric

Consider a **Doubly Linked List (DLL)** implemented in a `DLL` class. Write a method named `isSymmetric(self)` that determines whether the items in the linked list are arranged symmetrically.

For example:  
- Given the **DLL**:  **head → 1 ↔ 2 ↔ 3 ↔ 2 ↔ 1 ← tail** is symmetric, therefore, the function should return True.
- But if the **DLL** is: **head → 1 ↔ 2 ↔ 3 ↔ 1 ← tail** is not symmetric, therefore the function should return False.

### Question_3: Insert a Node After a Given Value

Assume, HEAD is the head-node of a doubly linked list (dll). Write a utility function addNodeAfterValue(self, givenValue, newValue) to insert a new value in this dll just after a given value.
-  a. If the given value is found in the dll, insert the new value just after the given value.
-  b. If the given value is not found, don’t add the node. Just print “Not found”

### Question_4 : Insert a Node in a Sorted Doubly Linked List
Given a sorted doubly linked list and a value to insert, write a function to insert the value in sorted way (and in efficient way). 
-  Initial doubly linked list : **head → 4 ↔ 7 ↔ 12 ↔ 21 ↔ 28 ← tail**
-  After calling **insertSorted(9)** the list will be as follows: **head → 4 ↔ 7 ↔ 9↔ 12 ↔ 21 ↔ 28 ← tail**


