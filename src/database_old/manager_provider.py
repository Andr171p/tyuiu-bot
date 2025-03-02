from typing import Optional

from src.database_old.manager import DatabaseManager


class DatabaseManagerSingleton:
    _instance: Optional[DatabaseManager] = None
    
    def __new__(cls) -> DatabaseManager:
        if cls._instance is None:
            cls._instance  = DatabaseManager()
            cls._instance.init()
        return cls._instance
    
    
def get_database_manager() -> DatabaseManager:
    manager = DatabaseManagerSingleton()
    return manager
