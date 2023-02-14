# Ros-development
For studying
this is first edit3

- - -

## 2023_02_13

- - -

* first
  * turtlebot3
  * Laptop ubuntu 20.04.01 LTS

* second
  * ROS2 DDS explain

* third

```shell
  * ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 2.0, y: 0.0, z: 1.8}}'
  # I can control turtle1 and turtle2

  * ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5, y: 9, theta: 1.57, name: 'turtle2'}"
  # I can make service2 to control another turtlebot
```

# 개념정리

- .json파일 만들기 : 원하는 폴더 내의 터미널 창에 'touch settings.json'이라고 입력한다.

- 파일 안에는 숨김파일이라는 항목이 존재한다. 체크해주면 .bashrc 등의 파일이 나타난다.

- Terminator 사용법 - Ctrl + shift +
e : 좌우 분할, w : 터미널 닫기, o : 상하 분할, c : 복사, v : 붙여넣기

    Alt + 방향키 : 터미널 이동

- 명령어 힌트 찾기 : ros2 run turtlesim ~~~ ----> Tap키를 두 번 누른다.

- VisualStudio Code, Github와 연동하기 : git config --global user.email "    "

    git config --global user.name"    "

- 수정 개념 : commit(문서 상 수정), push(git으로 전송), pull(git에서 pc로 불러오기)

- cat : cat memoji - 파일 안의 내용 보기

- home 표현 : ~/.

- alias : alias testpub = ros2 run ~~~ // ros2 run 이하의 명령어를 testpub으로 단축

- 노드 이름 바꾸기 : ros2 run turtlesim turtlesim_node --ros -args -remap -node :=이름

    //그냥 실행하면 turtlesim이라는 이름으로 생성. 그러므로 여러대 동작시 이름 변경 필요

- 실행은 run

- 거북이 2마리 따로 조종시 서비스 이름 바꾸기

- rqt 모니터, rqt service caller 등 사용

- 노드 정보 확인 : ros2 node info/이름

- 파라미터 불러오기 및 설정 : ros2 param get /turtlesim background_r
//불러오기

  ros2 param set /turtlesim background_r//설정

  저장 : ros2 param dump /turtlesim ---->.yaml 형태로 저장
  ---->이를 확인하기 위해서는 cat turtlesim.yaml

  저장 파일 불러오기 : ros2 param load /turtlesim ./ turtlesim.yaml // turtlesim에 turtlesim.yaml의 정보를 불러온다.

  저장된 것을 바로 적용하여 실행 : ros2 run turtlesim turtlesim_node --ros-args --params-file ./turtlesim.yaml


- ros의 단위는 m 이다.
- https://github.com/freshmea
- https://freshmea.notion.site/freshmea/ROS2-5a5303ac2160454885498a52dfce26c4
#
#
# 2023.02.14.
# class
- class는 틀이다. class에는 여러 기능적인 함수 뿐만 아니라 변수들 또한 가지게 된다.

  ex) 학생정리 : 각각의 학생에게는 나이와 성격, 성적 등 다양한 것이 있다. 여러 학생들을 전부 선언하기 위하여 여러 변수를 만들게 되면 매우 힘들다. 이에 정해진 틀을 만들어 놓고 적용하기 위해 class를 사용한다.

    ob=Test(), ob2=Test()


# pkg
- pkg에는 노드, yaml 등이 있고 launch를 통해 이들을 조작한다.
- src 파일 안에서 pkg를 만든다. --> "ros2 pkg create --build-type ament_python my_package"

  빌드타입, 사용하는 파이썬, 패키지 이름

- 빌드는 'colcon build'라고 쓴다.

# pkg 파일 생성
- robot_ws에서 src에 다음과 같은 명령어를 입력한다. 'ros2 pkg create --build-type ament_python my_package'

# class
- class M_turtle(Node): #상속을 받기위해 가로 안에 부모 class를 작성한다.
  def __init__(self): #상속을 하기 위해서는 이를 작성해야 한다.
    super().__init__('move_turtle') # mpub는 토픽의 이름을 설정한 것이다.
    self.qos = QoSProfile(depth = 10)
    self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', self.qos) #message는 통신하는 토픽의 이름으로 pub과 sub의 내용이 동일하다.


# Publisher와 Subscriber
- 노드 등록 하는 방법 설명 : setup.py 수정 'mp = my_package.mpub:main'
- mpub.py, msub.py
- mpub.py 이용하여 터틀심 조종하기
- Publisher : class 이름 설정, topic 이름 설정, 통신하는 message 이름 설정, 내용을 publish로 설정
- Subscriber : 주고 받을 message 이름 동일화 그리고 내용을 subscribe로 설정

# 기타 수정사항
- 코드가 주고 받는 내용의 변수명을 꼭 제대로 확인한다.
- 파일을 실행시킬 때는 저장 후 사용한다.
