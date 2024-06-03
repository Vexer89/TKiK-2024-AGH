# Manual
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
### Klasy final
```java 
public final class Animal {
    // ...
}
```
zostanie zamienione poprzez użycie konstrukcji w konstruktorze uniemożliwiającej dziedziczenie.
```python
class Animal:
    def __init__(self):
        if type(self) is not Animal:
            raise TypeError('Subclassing not allowed')
```

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
