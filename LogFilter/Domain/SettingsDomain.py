import json

#======================================================================================================================
# is_enabled - ��������� �������
# is_included - ����� ��������� ��� true � ���������� ��� false
# data - ������ ��� �������
#======================================================================================================================

class NodeSetting:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.include = json["include"]
        self.data = json["data"]

        
class EventFilter:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.operation_filter = NodeSetting(json["operationFilter"])
        

class Settings:
    def __init__(self, json: dict):
        self.event_filter = EventFilter(json["eventFilter"])
        self.log_path = json["logPath"]
        self.output_path = json["outputPath"]
        
    @staticmethod
    def fromFile(path: str): 
        file = open(path)
        settings = Settings(json.load(file))
        file.close()
        return settings
