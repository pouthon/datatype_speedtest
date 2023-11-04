import timeit

from dataclasses import dataclass, field
from collections import namedtuple

DrawDownStatsAsNamedTuple = namedtuple('DrawDownStatsAsNamedTupe',
                                       ['is_valid',
                                       'adjusted_for_negative_values',
                                       'avg_drawdown_pct',
                                       'max_drawdown_pct',
                                       'avg_drawdown_amnt',
                                       'max_drawdown_amnt'])


@dataclass
class DrawDownStatsAsDC:
  is_valid: bool = field(repr=True)
  adjusted_for_negative_values: bool = field(repr=True)
  avg_drawdown_pct: float = field(repr=True)
  max_drawdown_pct: float = field(repr=True)
  avg_drawdown_amnt: float = field(repr=True)
  max_drawdown_amnt: float = field(repr=True)

@dataclass(slots=True)
class DrawDownStatsAsDCSlotsTrue:
  is_valid: bool = field(repr=True)
  adjusted_for_negative_values: bool = field(repr=True)
  avg_drawdown_pct: float = field(repr=True)
  max_drawdown_pct: float = field(repr=True)
  avg_drawdown_amnt: float = field(repr=True)
  max_drawdown_amnt: float = field(repr=True)


DrawDownStatsAsDict = {
  'is_valid': True,
  'adjusted_for_negative_values': False,
  'avg_drawdown_pct': 3.14,
  'max_drawdown_pct': 3.14,
  'avg_drawdown_amnt': 3.14,
  'max_drawdown_amnt': 3.14
}


def create_named_tuple_version(
    is_valid: bool,
    adjusted_for_negative_values: bool,
    avg_drawdown_pct: float,
    max_drawdown_pct: float,
    avg_drawdown_amnt: float,
    max_drawdown_amnt: float,
):
  return DrawDownStatsAsNamedTuple(
    is_valid,
    adjusted_for_negative_values,
    avg_drawdown_pct,
    max_drawdown_pct,
    avg_drawdown_amnt,
    max_drawdown_amnt
  )


def create_dict_version(
    is_valid: bool,
    adjusted_for_negative_values: bool,
    avg_drawdown_pct: float,
    max_drawdown_pct: float,
    avg_drawdown_amnt: float,
    max_drawdown_amnt: float,
):
  return {
    'is_valid': is_valid,
    'adjusted_for_negative_values': adjusted_for_negative_values,
    'avg_drawdown_pct': avg_drawdown_pct,
    'max_drawdown_pct': max_drawdown_pct,
    'avg_drawdown_amnt': avg_drawdown_amnt,
    'max_drawdown_amnt': max_drawdown_amnt
  }


def create_many_as_dataclass(cnt: int) -> None:
  dd = []
  for i in range(cnt):
    d = DrawDownStatsAsDC(
      is_valid=True,
      adjusted_for_negative_values=True,
      avg_drawdown_pct=1.0,
      avg_drawdown_amnt=1.0,
      max_drawdown_pct=1.0,
      max_drawdown_amnt=1.0
    )
    dd.append(d)
  dd.clear()

def create_many_as_dataclass_slots_true(cnt: int) -> None:
  dd = []
  for i in range(cnt):
    d = DrawDownStatsAsDCSlotsTrue(
      is_valid=True,
      adjusted_for_negative_values=True,
      avg_drawdown_pct=1.0,
      avg_drawdown_amnt=1.0,
      max_drawdown_pct=1.0,
      max_drawdown_amnt=1.0,
    )
    dd.append(d)
  dd.clear()



def create_many_as_dict(cnt: int) -> None:
  dd = []
  for i in range(cnt):
    d = create_dict_version(
      is_valid=True,
      adjusted_for_negative_values=True,
      avg_drawdown_pct=1.0,
      avg_drawdown_amnt=1.0,
      max_drawdown_pct=1.0,
      max_drawdown_amnt=1.0
    )
    dd.append(d)
  dd.clear()

def create_many_as_namedtuple(cnt: int) -> None:
  dd = []
  for i in range(cnt):
    d = create_named_tuple_version(
      is_valid=True,
      adjusted_for_negative_values=True,
      avg_drawdown_pct=1.0,
      avg_drawdown_amnt=1.0,
      max_drawdown_pct=1.0,
      max_drawdown_amnt=1.0
    )
    dd.append(d)
  dd.clear()


if __name__ == '__main__':
  create_many_as_namedtuple(cnt=10_000_000)
  create_many_as_dataclass(cnt=10_000_000)
  create_many_as_dataclass_slots_true(cnt=10_000_000)
  create_many_as_dict(cnt=10_000_000)
