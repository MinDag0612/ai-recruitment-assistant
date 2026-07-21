from enum import Enum

class JobDescripStatus(str, Enum): #extending str to make it compatible with FastAPI and Pydantic
    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"