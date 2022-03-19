from __future__ import annotations

import vapoursynth as vs
from typing import Any, cast, Iterator, List, Mapping, Type, TypeVar, OrderedDict, TYPE_CHECKING, Generic

from PyQt5.QtCore import Qt, QModelIndex, QAbstractListModel

from ..core import main_window, QYAMLObject, VideoOutput, AudioOutput


T = TypeVar('T', VideoOutput, AudioOutput)


class Outputs(Generic[T], QAbstractListModel, QYAMLObject):
    out_type: Type[T]

    __slots__ = ('items')

    def __init__(self, local_storage: Mapping[str, T] | None = None) -> None:
        super().__init__()
        self.items: List[T] = []

        local_storage = local_storage if local_storage is not None else {}

        outputs = OrderedDict(sorted(vs.get_outputs().items()))

        main_window().reload_signal.connect(self.clear_outputs)

        for i, vs_output in outputs.items():
            if not isinstance(vs_output, self.vs_type):
                continue
            try:
                output = local_storage[str(i)]
                output.__init__(vs_output, i)  # type: ignore
            except KeyError:
                output = self.out_type(vs_output, i)

            self.items.append(output)

    def clear_outputs(self) -> None:
        for o in self.items:
            o.clear()

    def __getitem__(self, i: int) -> T:
        return self.items[i]

    def __len__(self) -> int:
        return len(self.items)

    def index_of(self, item: T) -> int:
        return self.items.index(item)

    def __getiter__(self) -> Iterator[T]:
        return iter(self.items)

    def append(self, item: T) -> int:
        index = len(self.items)
        self.beginInsertRows(QModelIndex(), index, index)
        self.items.append(item)
        self.endInsertRows()

        return len(self.items) - 1

    def clear(self) -> None:
        self.beginRemoveRows(QModelIndex(), 0, len(self.items))
        self.items.clear()
        self.endRemoveRows()

    def data(self, index: QModelIndex, role: int = Qt.UserRole) -> Any:
        if not index.isValid():
            return None
        if index.row() >= len(self.items):
            return None

        if role == Qt.DisplayRole:
            return self.items[index.row()].name
        if role == Qt.EditRole:
            return self.items[index.row()].name
        if role == Qt.UserRole:
            return self.items[index.row()]
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.items)

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if not index.isValid():
            return cast(Qt.ItemFlags, Qt.ItemIsEnabled)

        return super().flags(index) | Qt.ItemIsEditable  # type: ignore

    def setData(self, index: QModelIndex, value: Any, role: int = Qt.EditRole) -> bool:
        if not index.isValid():
            return False
        if not role == Qt.EditRole:
            return False
        if not isinstance(value, str):
            return False

        self.items[index.row()].name = value
        self.dataChanged.emit(index, index, [role])

        return True

    def __getstate__(self) -> Mapping[str, Any]:
        return dict(zip([str(x.index) for x in self.items], self.items), type=self.out_type)

    def __setstate__(self, state: Mapping[str, T | str]) -> None:
        try:
            type_string = state['type']
            if not isinstance(type_string, str):
                raise TypeError('Storage loading: Outputs: value of key "type" is not a string')

        except KeyError:
            raise KeyError('Storage loading: Outputs: key "type" is missing') from KeyError

        for key, value in state.items():
            if key == 'type':
                continue
            if not isinstance(key, str):
                raise TypeError(f'Storage loading: Outputs: key {key} is not a string')
            if not isinstance(value, self.out_type):
                raise TypeError(f'Storage loading: Outputs: value of key {key} is not {self.out_type.__name__}')

        self.__init__(state)  # type: ignore

    if TYPE_CHECKING:
        # https://github.com/python/mypy/issues/2220
        def __iter__(self) -> Iterator[T]: ...


class VideoOutputs(Outputs[VideoOutput]):
    yaml_tag = '!VideoOutputs'
    out_type = VideoOutput
    vs_type = vs.VideoOutputTuple


class AudioOutputs(Outputs[AudioOutput]):
    yaml_tag = '!AudioOutputs'
    out_type = AudioOutput
    vs_type = vs.AudioNode
