# Przykłady
Ten plik zawiera opis jak konkretne struktury w javie są tłumaczone na pythona.
## Nagłówki
### import
```java
import abc.name
```
zostanie zamienione na
```python
import abc.name
```

### package
Jako, że w pytonie nie ma czegoś takiego zostanie to zakomentowane np.
```python
# package abc.name
```

## Struktury

### Interfejs
Użyta zostanie tu biblioteka abc implementująca abstrakcyjne klasy i metody w pythonie
```java
public interface Animal {
    void makeSound();
    void move();
}
```
zostanie zamienione na
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

### Enum
Zostanie użyta tu biblioteka pythona enum.

```java
public enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
```
zostanie zamienione na
```python
from enum import Enum

class Day(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
```

## Klasy

### Klasy abstract
Będzie to wyglądać identycznie jak w przypadku interfejsów.


### Dziedziczenie i interfejsy
```java 
public class Dog extends Animal{
    // ...
}
```
jak i
```java 
public class Dog implements Animal{
    // ...
}
```
zostanie przetłumaczone na
```python
class Dog(Animal):
    # ...
```

### Atrybuty
```java 
public class Test{
    public int number;
    protected double quantity = 0;
    private string name;
}
```
zostanie przetłumaczone na
```python
    class Test:
        def __init__(self):
            self.number = None          
            self._quantity = 0.0        
            self.__name = None
```

### Atrybuty static
```java 
public class Test {
    public static int instances = 0;
}
```
przetłumaczone zostanie na
```python
class Test:
    instances = 0
```

## Metody
```java
public int add(int a, int b) {
    return a + b;
}
```
```python
def add(a, b):
    return a + b
```

### Metody abstrakcyjne
```java 
public abstract class Animal {
    abstract void makeSound();
    abstract void move();
}
```
zostanie przetłumaczony na
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def move(self):
        pass
```

## Pętle

### For

```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```
zosatnie przetłumaczone na
```python
for i in range(0, 10, 1):
    print(i)
```

### While
```java
int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}
```
zostanie przetłumaczone na
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### Do while
```java
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 10);
```
zostanie przetłumaczone na
```python
i = 0
while True:
    print(i)
    i += 1
    if i >= 10:
        break
```

## Warunki

### If
```java
int a = 5;
if (a > 0) {
    System.out.println("a is positive");
} else if (a < 0) {
    System.out.println("a is negative");
} else {
    System.out.println("a is zero");
}
```
zostanie przetłumaczone na
```python
a = 5
if a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is zero")
```

### Switch
```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    case 4:
        System.out.println("Thursday");
        break;
    case 5:
        System.out.println("Friday");
        break;
    case 6:
        System.out.println("Saturday");
        break;
    case 7:
        System.out.println("Sunday");
        break;
    default:
        System.out.println("Invalid day");
}
```
zostanie przetłumaczone na
```python
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")
```

## Wyjątki

```java
try {
    throw new Exception();
} catch (Exception e) {
    System.out.println("Exception caught");
} finally {
    System.out.println("Finally block");
}
```
zostanie przetłumaczone na
```python
try:
    raise Exception()
except Exception:
    print("Exception caught")
finally:
    print("Finally block")
```

## Wyrażenia

### Wyrażenie logiczne
```java
boolean a = true;
boolean b = false;
boolean c = a && b;
```
zostanie przetłumaczone na
```python
a = True
b = False
c = a and b
```
### Wyrażenie arytmetyczne
```java
int a = 5;
int b = 3;
int c = a + b;
```
zostanie przetłumaczone na
```python
a = 5
b = 3
c = a + b
```

