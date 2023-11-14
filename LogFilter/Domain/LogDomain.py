from tkinter import SEL


class Event:
    def __init__(self, json: dict):
        self.detail = json["Detail"]
        self.opeartion = json["Operation"]
        self.pid = json["PID"]
        self.path = json["Path"]
        self.process_index = json["ProcessIndex"]
        self.process_name = json["Process_Name"]
        self.result = json["Result"]
        self.time_of_day = json["Time_of_Day"]

    def __dict__(self):
        return {
            "Detail": self.detail,
            "Operation": self.opeartion,
            "PID": self.pid,
            "Path": self.path,
            "ProcessIndex": self.process_index,
            "Process_Name": self.process_name,
            "Result": self.result,
            "Time_of_Day": self.time_of_day,
        }


class Process:
    def __init__(self, json: dict):
        self.authentication_id = json["AuthenticationId"]
        self.command_line = json["CommandLine"]
        self.company_name = json["CompanyName"]
        self.create_time = json["CreateTime"]
        self.description = json["Description"]
        self.finishtime = json["FinishTime"]
        self.image_path = json["ImagePath"]
        self.integrity = json["Integrity"]
        self.is64bit = json["Is64bit"]
        self.is_virtualized = json["IsVirtualized"]
        self.owner = json["Owner"]
        self.parent_process_id = json["ParentProcessId"]
        self.parent_process_index = json["ParentProcessIndex"]
        self.process_id = json["ProcessId"]
        self.process_index = json["ProcessIndex"]
        self.process_name = json["ProcessName"]
        self.version = json["Version"]
        self.modulelist = ModuleList(json["modulelist"])

    def __dict__(self):
        return {
            "AuthenticationId": self.authentication_id,
            "CommandLine": self.command_line,
            "CompanyName": self.company_name,
            "CreateTime": self.create_time,
            "Description": self.description,
            "FinishTime": self.finishtime,
            "ImagePath": self.image_path,
            "Integrity": self.integrity,
            "Is64bit": self.is64bit,
            "IsVirtualized": self.is_virtualized,
            "Owner": self.owner,
            "ParentProcessId": self.parent_process_id,
            "ParentProcessIndex": self.parent_process_index,
            "ProcessId": self.process_id,
            "ProcessIndex": self.process_index,
            "ProcessName": self.process_name,
            "Version": self.version,
            "modulelist": self.modulelist.__dict__(),
        }


class Module:
    def __init__(self, json: dict):
        self.base_address = json["BaseAddress"]
        self.company = json["Company"]
        self.description = json["Description"]
        self.path = json["Path"]
        self.size = json["Size"]
        self.timestamp = json["Timestamp"]
        self.version = json["Version"]

    def __dict__(self):
        return {
            "BaseAddress": self.base_address,
            "Company": self.company,
            "Description": self.description,
            "Path": self.path,
            "Size": self.size,
            "Timestamp": self.timestamp,
            "Version": self.version,
        }


class ModuleList:
    def __init__(self, json: dict):
        if json == None:
            self.module = list()
            return
        self.module = self.getListFromJson(json["module"])

    def __dict__(self):
        result = list()
        for module in self.module:
            result.append(module.__dict__())
        return {"module": result}

    def append(self, module: Module):
        self.module.append(module)

    @staticmethod
    def getListFromJson(json_list: list):
        result = list()
        for json in json_list:
            result.append(Module(json))
        return result


class ProcessList:
    def __init__(self, json: dict):
        if json == None:
            self.process = list()
            return
        self.process = self.getListFromJson(json["process"])

    def __dict__(self):
        result = list()
        for process in self.process:
            result.append(process.__dict__())
        return {"process": result}

    def append(self, process: Process):
        self.process.append(process)

    @staticmethod
    def getListFromJson(json_list: list):
        result = list()
        for json in json_list:
            result.append(Process(json))
        return result


class EventList:
    def __init__(self, json: dict):
        if json == None:
            self.event = list()
            return
        self.event = self.getListFromJson(json["event"])

    def __dict__(self):
        result = list()
        for event in self.event:
            result.append(event.__dict__())
        return {"event": result}

    def append(self, event: Event):
        self.event.append(event)

    @staticmethod
    def getListFromJson(json_list: list):
        result = list()
        for json in json_list:
            result.append(Event(json))
        return result


class Log:
    def __init__(self, json: dict = None):
        self.event_list = EventList(None)
        self.process_list = ProcessList(None)
        if json != None:
            self.event_list = EventList(json["procmon"]["eventlist"])
            self.process_list = ProcessList(json["procmon"]["processlist"])

    def __dict__(self):
        return {
            "procmon": {
                "eventlist": self.event_list.__dict__(),
                "processlist": self.process_list.__dict__(),
            }
        }

    def addEvent(self, event: Event):
        self.event_list.append(event)

    def getEvent(self, i: int):
        if i >= 0 and i < len(self.event_list.event):
            return self.event_list.event[i]
        return None

    def addProcess(self, process: Process):
        self.process_list.append(process)

    def getProcess(self, i: int):
        if i >= 0 and i < len(self.process_list.process):
            return self.process_list.process[i]
        return None
