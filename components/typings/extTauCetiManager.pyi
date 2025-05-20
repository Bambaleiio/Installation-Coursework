"""Info Header Start
Name : extTauCetiManager
Author : Wieland@AMB-ZEPH15
Saveorigin : TauCetiV4.toe
Saveversion : 2023.11880
Info Header End"""
TDFunctions = op.TDModules.mod.TDFunctions
import uuid
from extParStack import InvalidOperator
from typing import Literal, Union

def snakeCaseToCamelcase(classObject):
    pass

class PresetDoesNotExist(Exception):
    pass

class extTauCetiManager:

    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self.stack = self.ownerComp.op('stack')
        self.tweener = self.ownerComp.op('remote_dependency').GetGlobalComponent()
        self.modeler = self.ownerComp.op('modeler')
        self.preview = self.ownerComp.op('previews')
        self.logger = self.ownerComp.op('logger')
        self.prefab = self.ownerComp.op('presetPrefab')
        self.Record_Preset = self.Store_Preset
        self.PresetDoesNotExist = PresetDoesNotExist
        pass

    @property
    def preset_folder(self):
        pass

    def Find_Presets(self, name='', tag=''):
        pass

    def Export_Presets(self, path):
        pass

    def Import_Presets(self, path):
        pass

    def store_prev(self, prefab):
        pass

    def Get_Preset_Comp(self, id):
        pass

    def Get_Preset_Name(self, id):
        pass

    def Get_Preview(self, id):
        pass

    def Store_Preset(self, name, tag='', id=''):
        pass

    def Remove_Preset(self, id):
        pass

    def Remove_All_Presets(self):
        pass

    def Preset_To_Stack(self, id):
        pass

    def Recall_Preset(self, id, time, curve='s', load_stack=False):
        pass

    def Rename(self, id, new_name):
        pass

    def Push_Stack_To_Presets(self, mode: Literal['keep', 'overwrite']='keep', _stackelements: Union[str, list, tuple]='*', _presets: Union[str, list, tuple]='*'):
        pass
    '\n\t\tUtility Functions and not part of the logic. Should maybe live outside.\n\t'

    def Import_V3_Presets(self, path=''):
        pass

    @property
    def PresetParMenuObject(self):
        pass