import copy

from dollar.dollarexception import DollarException
from dollar.dollarobject import DollarObject
from dollar.helper.validationhelper import ValidationHelper
import dollar.dollarerrorconstants as DollarErrorMessages


class DollarObjectIdMapDiff:
    def __init__(self, added, changed, removed):
        self.added = added
        self.changed = changed
        self.removed = removed

    def is_changed(self) -> bool:
        return len(self.added) + len(self.changed) + len(self.removed) != 0


class DollarObjectIdMap:
    def __init__(self):
        self.id_map = {}

    def get(self, dollar_object_id: str) -> DollarObject:
        if not ValidationHelper.valid_str(dollar_object_id):
            raise DollarException(DollarErrorMessages.INVALID_ID_STRING)
        if dollar_object_id not in self.id_map:
            raise DollarException(
                DollarErrorMessages.DOLLAR_OBJECT_ID_DOES_NOT_EXIST.format(
                    id=dollar_object_id
                )
            )

        return self.id_map[dollar_object_id]

    def has_id(self, dollar_object_id: str) -> bool:
        return dollar_object_id in self.id_map

    def remove__with_path(self, path: str):
        keys_to_remove = []
        for key in self.id_map:
            if self.id_map[key].get_path() == path:
                keys_to_remove.append(key)
        for key in keys_to_remove:
            del self.id_map[key]

    def get_map(self):
        return self.id_map

    def add(self, dollar_object: DollarObject):
        if not ValidationHelper.valid_obj(dollar_object, DollarObject):
            raise DollarException(DollarErrorMessages.INVALID_DOLLAR_OBJECT)
        dollar_object_id = dollar_object.get_id()
        if not ValidationHelper.valid_str(dollar_object_id):
            raise DollarException(DollarErrorMessages.INVALID_ID_STRING)
        if dollar_object_id in self.id_map:
            raise DollarException(
                DollarErrorMessages.DOLLAR_OBJECT_ID_EXISTS.format(dollar_object_id)
            )
        self.id_map[dollar_object_id] = dollar_object

    def add__force(self, dollar_object: DollarObject):
        if not ValidationHelper.valid_obj(dollar_object, DollarObject):
            raise DollarException(DollarErrorMessages.INVALID_DOLLAR_OBJECT)
        dollar_object_id = dollar_object.get_id()
        if not ValidationHelper.valid_str(dollar_object_id):
            raise DollarException(DollarErrorMessages.INVALID_STRING)
        self.id_map[dollar_object_id] = dollar_object

    def diff(self, dollar_object_id_map) -> DollarObjectIdMapDiff:
        added = []
        changed = []
        removed = []
        checked_keys = []
        for key in self.id_map:
            checked_keys.append(key)
            if key not in dollar_object_id_map.id_map:
                removed.append(self.id_map[key])
            elif self.id_map[key] != dollar_object_id_map.id_map[key]:
                changed.append(dollar_object_id_map.id_map[key])
        for key in dollar_object_id_map.id_map:
            if key in checked_keys:
                continue
            added.append(dollar_object_id_map.id_map[key])
        return DollarObjectIdMapDiff(added, changed, removed)

    def copy(self):
        new_map = DollarObjectIdMap()
        new_map.id_map = copy.deepcopy(self.id_map)
        return new_map
