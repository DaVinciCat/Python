from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple
import json
import pickle

class ConfigHandler(ABC):
    
    def __init__(self) -> None:
        self.parameters: Dict[str, Any] = {}
    
    def add(self, name: str, value: Any) -> None:
        self.parameters[name] = value
        
    def try_add(self, name: str, value: Any) -> bool:
        if name in self.parameters:
            return False
        self.parameters[name] = value    
        return True
            
    def get(self, name: str) -> Any:
        return self.parameters[name]
    
    def try_get(self, name: str) -> Tuple[bool, Any]:
        result = self.parameters.get(name, None)
        return (result is not None, result)

    def delete(self, name: str) -> bool:
        result = self.parameters.pop(name, None)
        return result is not None
        
    def all(self) -> Dict[str, Any]:
        for key, value in self.parameters.items():
            yield key, value
            
    def clear(self) -> None:
        self.parameters.clear()    
    
    @abstractmethod    
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass
    
class JsonConfigHandler(ConfigHandler):
    
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
    
    def read(self) -> None:
        with open(self.filename, 'r', encoding='utf-8') as json_file:
            self.parameters = json.load(json_file)
    
    def write(self) -> None:
        with open(self.filename, 'w', encoding='utf-8') as json_file:
            json.dump(self.parameters, json_file, ensure_ascii=False, indent=4)
            
class PickleConfigHandler(ConfigHandler):
    
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
    
    def read(self) -> None:
        with open(self.filename, 'rb') as pickle_file:
            self.parameters = pickle.load(pickle_file)
    
    def write(self) -> None:
        with open(self.filename, 'wb') as pickle_file:
            pickle.dump(self.parameters, pickle_file)           
        
#test

def main() -> None:
    json_config_handler = JsonConfigHandler('config_test.json')
    pickle_config_handler = PickleConfigHandler('config_test.pickle')
    
    handle(json_config_handler)
    handle(pickle_config_handler)

def handle(config_handler: ConfigHandler):
    config_handler.add('one', 1)
    config_handler.add('two', 2)
    config_handler.add('cow', 'cow')
    config_handler.write()
    config_handler.clear()
    config_handler.read()
    print(list(config_handler.all()))

if __name__ == '__main__':
    main()

# ConfigHandler
# Реализовать простое средство для считывания и записи информации из конфигурационных файлов. 
# Количество форматов не ограничено.
# Необходимо описать базовый абстрактный класс ConfigHandler. 
# В интерфейсе класса должны присутствовать следующие методы:

#    add(name: str, value: Any) -> None - добавляет новый, или затирает существующий, параметр с именем name и указанным значением value
#    get(name: str) -> Any - возвращает значение параметра с указанным именем
#    all() -> dict[str, Any] - возвращает значения всех опций в виде словаря (можно генератора)
#    delete(name: str) -> None - удаляет значение опции с указанным именем
#    clear() -> None - удаляет значения всех опций (очистка)
#    read() -> None - абстрактный метод, выполняет чтение параметров из конфигурационного файла
#    write() -> None - абстрактный метод, записывает параметры в конфигурационный файл

# Необходимо описать дочерний класс JsonConfigHandler, который реализует операции чтения и записи в формате JSON.
# Необходимо описать дочерний класс PickleConfigHandler, который реализует операции чтения и записи в формате Pickle.
