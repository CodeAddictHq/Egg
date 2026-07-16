from collections import deque
from ..Errors.runtime import (
  TypeNotAllowed,
  RuntimeError,
  NotFoundError,
  ArgsNotAllowed,
)


class Fun:
  def show(self, val):
    try:
      for i in val:
        print(i)
    except Exception as e:
      raise RuntimeError(str(e))

  def fineshow(self, val):
    try:
      fine_str = ""
      for i in val:
        fine_str += str(i)
      print(fine_str)
    except Exception as e:
      raise RuntimeError(str(e))

  def type(self, val):
    try:
      if len(val) > 1:
        raise ArgsNotAllowed("Only one argument is allowed.")
      return self.get_types(val[0])
    except Exception:
      raise

  def get_types(self, val):
    try:
      if isinstance(val, list):
        return "ARRAY"
      elif isinstance(val, int):
        return "INTEGER"
      elif isinstance(val, dict):
        return "HASHMAP"
      elif isinstance(val, float):
        return "FLOATING"
      elif isinstance(val, str):
        return "STRING"
      elif isinstance(val, type({}.keys())):
        return "HASH_KEYS"
      elif isinstance(val, type({}.values())):
        return "HASH_VALUES"
      elif isinstance(val, deque):
        return "QUEUE"
      else:
        return "UNKNOWN"
    except Exception as e:
      raise RuntimeError(str(e))

  def keys(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed("keys() expects exactly one argument.")
      if not isinstance(val[0], dict):
        raise TypeNotAllowed("keys() can only be used on a HASHMAP.")
      return val[0].keys()
    except Exception:
      raise

  def len(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed("len() expects exactly one argument.")
      return len(val[0])
    except TypeError:
      raise TypeNotAllowed(
        f"Type '{self.get_types(val[0])}' has no length."
      )
    except Exception:
      raise

  def values(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed("values() expects exactly one argument.")
      if not isinstance(val[0], dict):
        raise TypeNotAllowed("values() can only be used on a HASHMAP.")
      return val[0].values()
    except Exception:
      raise

  def check(self, val):
    try:
      if len(val) > 1:
        raise ArgsNotAllowed("Only one argument is allowed.")
    except Exception:
      raise

  def string(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed("string() expects exactly one argument.")
      return str(val[0])
    except Exception:
      raise

  def number(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed("number() expects exactly one argument.")
      try:
        return int(val[0])
      except ValueError:
        return float(val[0])
    except (ValueError, TypeError):
      raise TypeNotAllowed(
        f"Cannot convert {val[0]!r} to a number."
      )
    except Exception:
      raise

  def ask(self, val):
    try:
      if val and val[0]:
        self.check(val)
        return input(val[0])
      return input()
    except Exception:
      raise
  
  # List methods

  def method_push(self, val):
    try:
      if len(val) != 2:
        raise ArgsNotAllowed(
          "push() expects two arguments: value and array."
        )
      val[1].append(val[0])
    except AttributeError:
      raise TypeNotAllowed(
        f"push() is not supported for type '{self.get_types(val[1])}'."
      )
    except Exception:
      raise

  def method_pop(self, val):
    try:
      if len(val) != 1:
        raise ArgsNotAllowed(
          "pop() expects 1 arguments."
        )
      return val[0].pop()
    except AttributeError:
      raise TypeNotAllowed(
        f"pop() is not supported for type '{self.get_types(val[0])}'."
      )
    except IndexError:
      raise RuntimeError("Cannot pop from an empty array.")
    except Exception:
      raise