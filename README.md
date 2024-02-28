# toy-project

> 좋아하는 게임으로 코딩에 재미를 붙여보자!

## 🎉 Introduction

안녕하세요!😎

제일 처음 project는 좋아하는 취미인 게임을 생각하여 코딩에 대한 재미를 붙여보고자 시작하였습니다.

게임은 어릴 때부터 해보기만 해봤지, 만드는 건 상상도 못했는데요!🧐
어떤 식으로 만들었는지 지금부터 소개드리겠습니다.✋

## 🦝 Member 🦦

### Raccoon is..

- 프로젝트 계획 관리 및 기술 소개

### Otter is..

- 프로젝트 개발

<details>
<summary> 🕹️ Game 1 : 숫자 야구(bulls and cows)</summary>

## ⚡ Software Used

| Tech Stack |                                                                                                                                     Used                                                                                                                                     | version |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
|  Language  |                                                                                                                                    Python                                                                                                                                    |  3.11   |
|   Module   |                                                                                                                                    Curses                                                                                                                                    |         |
|  Package   | [pyinstaller](https://otterbit.tistory.com/entry/PyInstaller-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B0%9C%EB%B0%9C%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EC%9D%84-%EC%8B%A4%ED%96%89-%ED%8C%8C%EC%9D%BCexe%EB%A1%9C-%EB%A7%8C%EB%93%9C%EB%A0%A4%EB%A9%B4) |         |

📌`Life is short, you need Python.`
이라는 `python`의 철학으로 문법이 단순하고 배우기 쉬워 초보자에게 적합한 프로그래밍 언어로 `python`을 채택하였습니다.

## 실행 방법

1. 저장하고 싶은 local 저장소에 `git clone https://github.com/SanGyuk-Raccoon/toy-project.git` 명령어 실행
2. `bulls-and-cows/dist/main.exe` 실행

## 게임 방법

[⚾️ 시연 영상](https://youtu.be/ZKMumNB1sl8?feature=shared&t=43)

1. `enter your name :` 닉네임 작성 📍3자리 영문자만 작성 가능
2. 3자리 중복 없는 숫자 작성
3. 오른쪽에 출력되는 결과값으로 정답 예측(아래 `규칙-용어 정의` 참고)

## 🔈 규칙

### 요구 사항

[📄 Bulls and Cows Reference Document](https://en.wikipedia.org/wiki/Bulls_and_Cows)
위의 레퍼런스 문서를 참고하여 "숫자 야구" 게임 룰로 규칙을 정의하였습니다.

- 사용자는 숫자 야구 게임을 실행시킬 수 있으며, 일정 횟수 안에 정답을 맞춰야 한다.
- 정답 최대 제출 횟수: 10회
- 맞춰야하는 숫자는 0~9로 이루어진 3자리 순열이다.
  - 사용자는 단순히 키보드 입력으로 정답을 제출할 수 있다.
  - 맞춰야하는 숫자는 0~9로 이루어진 3자리 순열이다.(중복을 허용하지 않고, 순서가 유의하다.)
  - 유저가 잘못된 input을 입력하더라도 프로그램이 종료되면 안 된다.

### 용어 정의

- Strike : 위치와 숫자가 동일한 경우
- Ball : 위치는 다르지만, 해당 숫자가 있는 경우
- Out : 제출한 숫자가 포함되어 있지 않은 경우
  - Strike out! : 제출한 숫자가 3자리 숫자에 한 군데도 포함되어 있지 않은 경우

### Manual

- input 형태 : 연속된 세자리 숫자(0~9). 중복 허용 하지 않음. ex) 123, 013 등
- 만약, 잘못된 input을 입력 시, game_count는 세아리지 않음

</details>

## 👀 Contact Us

- 🦝 Raccoon E-mail: sangyukraccoon@gmail.com
- 🦦 Otter E-mail: hoonixox@gmail.com
