# rasp_pj

Raspberry Pi 4B
os: Raspberry Pi OS(64-bit) / release: 2023-12-05

환경 설정 및 버전
)업데이트
$sudo apt-get update

) 파이썬 
버전: 3.11.2

) 아두이노 설치
$sudo apt-get install arduino

) 가상환경 venv 설정
$python3 -m venv [가상환경 이름] //환경 설치
$source [가상환경 이름]/bin/activate //활성화
$deactivate //비활성화

) 라이브러리 설치(버전)
- opencv(==4.8.1.78)
$pip3 install opencv-python

- dlib(==19.24.2)
$pip3 install dlib

- scipy(==1.11.4)
$pip3 install scipy

- pyserial(==3.5)
$pip3 install pyserial

) dat 파일 설치(학습된 얼굴 렌드마크 데이터)
$wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 
$bunzip2 shape_predictor_68_face_landmarks.dat.bz2 
$datFile="shape_predictor_68_face_landmarks.dat"

) 아두이노 라이브러리 설치
- servo
Arduino 접속 > Sketch > Library Manager > 'Servo' 설치
'arduino_code.ino'에 코드 추가
#include<Servo.h>

코드 파일 설명
- raspberrypi_code.py
웹캠으로부터 받는 눈 깜빡임을 눈깜빡임 감지 알고리즘을 통해 command로 전환하여 아두이노에게 전달
양쪽 눈을 모두 깜빡이면 command==1
왼쪽 눈만 깜빡이면 command==2
오른쪽 눈만 깜빡이면 command==3

- arduino_code.ino
아두이노 코드로 라즈베리 파이로부터 입력받는 command에 따라 GPIO 컨트롤
command==1을 받으면 LED 제어
command==2를 받으면 active buzzer 제어, 스위치 입력으로 buzzer 끄기
command==3을 받으면 servo motor 제어
