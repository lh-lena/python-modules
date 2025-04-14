## Norm: pip install flake8

- print(globals()) -  повертає словник, який містить усі глобальні змінні та їх значення в поточному модулі
- print(locals()) - надає доступ до локальних змінних у поточному контексті програми


### documentations:
- print(dir(np.array))
- help(np)
- help(list)

### ABC (Abstract Base Class)
- implementation of abstract
- class through subclassing
import abc

class parent:
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print("child class")
# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))

## Debuging Python Code

python -m pdb python-script.py

not good practice: https://shitcode.net/latest/language/python
