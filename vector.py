class Vector2d(complex):

  def __new__(cls, *args, **kwargs):
    return complex.__new__(cls, *args, **kwargs)

  def __init__(self, *args, **kwargs) -> None:
      super().__init__()
      self.x = self.__getattribute__("real")
      self.y = self.__getattribute__("imag")

  def __add__(self, x):
      return Vector2d(super().__add__(x))

  def __mul__(self, x):
      if isinstance(x, Vector2d) :
        return self.x*x.x + self.y * x.y
      else:  
        return super().__mul__(x)

  def __neg__(self):
      return Vector2d(super().__neg__())

  def __pow__(self, x):
      return abs(self)**x

  def __sub__(self, x):
      return Vector2d(super().__sub__(x))

  def __radd__(self, x):
      return Vector2d(super().__radd__(x))

  def __rmul__(self, x):
      if isinstance(x, Vector2d):
        return self.x*x.x + self.y * x.y
      else:  
        return super().__rmul__(x)

  def __rsub__(self, x):
      return Vector2d(super().__rsub__(x))

  def __truediv__(self, x):
      return Vector2d(super().__truediv__(x))

  def __rtruediv__(self, x):
      print("test")
      return Vector2d(super().__rtruediv__(x))

if __name__ == "__main__":
  v = Vector2d(2, 3) * Vector2d(2, 3)
  print(v)
  print(type(v))
  #print(v.x, v.y)