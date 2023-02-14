class Test: #class는 항상 대문자
  def __init__(self):
    pass

  def aa(self):
    print('aaaaaa')

def main():
  a = 10 #중괄호를 사용하지 않기 때문에 띄어쓰기 중요.
  a = 'hello'
  ob = Test()
  ob.aa()
  ob.aa()

  print(a)

if __name__ == "__main__": #__  __는 내부변수라는 뜻
  main() #내부함수

