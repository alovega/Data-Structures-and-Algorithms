# S.O.L.I.D Principles of Software Engineering
This is a set of design principles created for software
developers using object oriented languages. This principles
are intended to foster a simpler, more robust and 
updatable code from software developers:<br>
When Implemented properly it makes the code extendable
,logical and easier to read

### 1. Single Responsibility principle
><b>This Principle requires that a class should only have one job. So if a class has more than one responsibility,
> it becomes coupled. A change in one responsibility result to modification of the other responsibility</b>
>
### 2. Open Close Principle
><b> Software entities (classes, modules, function) should be open for extension but not modifiction</b>

let us imagine we have a store, and we give a discount of 20% to our favorite customers: When we decide to offer an
 additional discount of 20% percent to our V.I.P customer We may modify the class for giving discount to be like -:
 ```
class Discount:

  def __init__(self, customer, price):
      self.customer = customer
      self.price = price

  def give_discount(self):
      if self.customer == 'fav':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4
```
This goes against the O.C.P principle, O.C.P forbids it. If we need to add a discount to a different type of customer,
new logic will be added to the class. To make this follow O.C.P principle we will add a new class that extends Discount
 class in
 this class  we would implement this behaviour
 ```
class Discount:

    def __init__(self, customer, price):
      self.customer = customer
      self.price = price

    def get_discount(self):
      return self.price * 0.2

class VIPDiscount(Discount):

    def get_discount(self):
      return super().get_discount() * 2
```

### 3. Liskov substitution Principle
><b>The main idea behind this is that, for any class a client should be able to use any of its subtypes
> indistinguishably without even noticing, and therefore without compromising the behaviour at run time. Simply means
> that clients are completely isolated and  unaware of changes in the class  hierarchy </b>

### 4. Interface Segregation Principle
><b> Make fine grained interface that are client specific Client should not be forced to depend upon interfaces that
>they do not use. Below is a classic example </b>
```
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass
```
><b>Another nice trick is that in our business logic, a single class can implement several interfaces if needed. So we
> can provide a single implementation for all the common methods between the interfaces. </b>
 

### 5. Dependency Inversion Principle
><b>Dependency should be on abstractions not concretions. High level modules should not depend upon low level modules
>, both high and low level modules should depend on the same abstractions.

<br>
<br>

# Data Structures

### Linked List
```
In arrays  data is stored in contigous memory location data is stored in contigous memory location for instance if
 the first item is stored at index 10 and is of size 15 bytes the next item will be stored at location 10 + 15 + 1

But for linked list data is not stored at contigous memory location for each item in memory location linked list
 stores the value of the item and the reference or pointer to the next item which constitutes of a node
```
##### Advantages of using a lined list
```
1. A linked list is a dynamic datastructure which means memory reserved for it can be reduced or increased at run time.

2. Since Arrays require contigous memory location it is very difficult to insert or delete an item  because the
 memory location of large items have to updated. Whereas in a linked list items are not stored in contigous memory
 location therefore you can easily update or delete an item

3. Owing to its flexibility, a linked list is more suitable for implementing data structures like stacks, queues, and lists.
```
