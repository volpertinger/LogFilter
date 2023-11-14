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
        self.pid_filter = NodeSetting(json["pidFilter"])
        self.process_index_filter = NodeSetting(json["processIndexFilter"])
        self.process_name_filter = NodeSetting(json["processNameFilter"])
        
class ProcessFilter:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.command_line_filter = NodeSetting(json["commandLineFilter"])
        self.company_name_filter = NodeSetting(json["companyNameFilter"])
        self.is_virtualized_filter = NodeSetting(json["isVirtualizedFilter"])
        self.process_id_filter = NodeSetting(json["processIdFilter"])
        self.process_name_filter = NodeSetting(json["processNameFilter"])
        
        

class Settings:
    def __init__(self, json: dict):
        self.event_filter = EventFilter(json["eventFilter"])
        self.process_filter = ProcessFilter(json["processFilter"])
        self.log_path = json["logPath"]
        self.output_path = json["outputPath"]
        
    @staticmethod
    def fromFile(path: str): 
        file = open(path)
        settings = Settings(json.load(file))
        file.close()
        return settings
