import json

# ======================================================================================================================
# is_enabled - активация фильтра
# is_included - филтр включения при true и исключения при false
# data - строки для фильтра
# ======================================================================================================================


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
        self.path_filter = NodeSetting(json["pathFilter"])
        self.result_filter = NodeSetting(json["resultFilter"])


class ProcessFilter:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.with_modules = json["withModules"]
        self.command_line_filter = NodeSetting(json["commandLineFilter"])
        self.company_name_filter = NodeSetting(json["companyNameFilter"])
        self.is_virtualized_filter = NodeSetting(json["isVirtualizedFilter"])
        self.process_id_filter = NodeSetting(json["processIdFilter"])
        self.process_name_filter = NodeSetting(json["processNameFilter"])
        self.parent_process_id_filter = NodeSetting(json["parentProcessIdFilter"])


class ActionBaseSetting:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.output_path = json["outputPath"]


class CollectUniaueEventFields(ActionBaseSetting):
    def __init__(self, json: dict):
        super(CollectUniaueEventFields, self).__init__(json)
        self.fields = json["fields"]


class WriteOptions:
    def __init__(self, json: dict):
        self.console = json["console"]
        self.file = json["file"]


class MalwareDetectionOptions:
    def __init__(self, json: dict):
        self.enabled = json["enabled"]
        self.programm_path = json["programPath"]


class Settings:
    def __init__(self, json: dict):
        self.event_filter = EventFilter(json["eventFilter"])
        self.process_filter = ProcessFilter(json["processFilter"])
        self.input_path = json["inputPath"]
        self.write_filtered_result = ActionBaseSetting(
            json["actions"]["writeFilteredResult"]
        )
        self.collect_unique_event_fields = CollectUniaueEventFields(
            json["actions"]["collectUniqueEventFields"]
        )
        self.collect_unique_process_fields = CollectUniaueEventFields(
            json["actions"]["collectUniqueProcessFields"]
        )
        self.write_options = WriteOptions(json["writeOptions"])
        self.malware_detection = MalwareDetectionOptions(
            json["actions"]["malwareDetection"]
        )

    @staticmethod
    def fromFile(path: str):
        file = open(path)
        settings = Settings(json.load(file))
        file.close()
        return settings
