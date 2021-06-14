# FilmFunFair

- 영화 정보, 리뷰 및 영화 추천 웹 사이트
- 커뮤니티 기능 제공



## 개발 기간

- 21.05.20 ~ 21.05.27



## 개발 환경

- python 3.8+
- Django 3.X
  - Django REST framework
- Vue.js 2.+



## 실행 방법

- 백엔드

  - 가상환경 설정

  - ```bash
    $ pip install -r requirments
    ```

  - ```bash
    $ python manage.py runserver
    ```

- 프론트엔드

  - ```bash
    $ npm i
    ```

  - ```bash
    $ npm run serve
    ```

  - Youtube API KEY를 발급받은 후 `src/components/movies/modals/MovieDetailPreview.vue` 의 19번째 줄에 삽입



## 팀원 정보

- 팀원
  - 김병현 : 백엔드 + 프론트엔드
  - 이성은 : 백엔드 + 프론트엔드



## 나의 프로젝트 기여 내용

### 백엔드

- ERD모델 설계
- Restful URL
- 전체 영화 조회 API
- 영화 상세 조회 API
- 리뷰 작성 API
- 리뷰 조회 API
- 커뮤니티 CRUD API
- 마이페이지 조회 API
- 로그인, 사인업 API
  - jwt토큰 기반
- 영화 추천 알고리즘
  - 유사 아이템 기반 추천 알고리즘
- 영화 검색 API

### 프론트엔드

- axios를 활용한 백엔드 API와 통신기능

- 홈페이지 대문
  - 마우스를 기준으로 임의의 범위만 선명하게 보이도록 디자인
- 로그인, 회원가입 모달
  - 회원가입 시 로그인 모달이 보이게 만들어 UX개선
- 영화 전체 조회 페이지 디자인
  - 3D-carousel
  - Infinity Scroll
- 영화 상세 조회 페이지
  - 영화 포스터에 마우스 hover시 간단한 내용 출력
  - 유튜브 API를 활용해 영화 예고편 제공

- 랜덤 영화 추천 페이지
  - 3d로 카드 뒤집어 지는 효과



## 결과페이지

- **Home**

  - `Main`

    <img src="README.assets/1_home-1623634870935.png" alt="image-20210612160031015" style="zoom:50%;" />

  - `Login, Signup Modal`

    <img src="README.assets/2_accounts_modal-1623634870936.png" alt="image-20210612160541580" style="zoom:50%;" />

- **MovieList**

  - `Movie Recommendation`

    <img src="README.assets/3_movie_list-1623634870936.png" alt="image-20210612160915193" style="zoom:50%;" />

  - `Movie Search`

    <img src="README.assets/4_search-1623634870936.png" alt="image-20210612161642961" style="zoom:50%;" />

  - `Movie List`

    <img src="README.assets/5_movie_list-1623634870936.png" alt="image-20210612161511286" style="zoom:50%;" />

  - `Movie Caption`

    <img src="README.assets/6_caption-1623634870936.png" alt="image-20210612163356565" style="zoom:50%;" />

  - `Movie Detail Modal`

    <img src="README.assets/7_movie_detail-1623634870936.png" alt="image-20210612161440425" style="zoom:50%;" />

- **Mypage**

  - `Like Movie` & `Watched Movie`

    <img src="README.assets/8_my_movies-1623634870936.png" alt="image-20210612161900063" style="zoom:50%;" />

  - `My Review`

    <img src="README.assets/9_my_review-1623634870937.png" alt="image-20210612161946591" style="zoom:50%;" />

  - `My Post`

    <img src="README.assets/10_my_post-1623634870938.png" alt="image-20210612162042885" style="zoom:50%;" />

- **Community**

  - `Community List`

    <img src="README.assets/11_community_list-1623634870938.png" alt="image-20210612162217402" style="zoom:50%;" />

  - `Community Detail`

    <img src="README.assets/12_community_detail-1623634870938.png" alt="image-20210612162355862" style="zoom:50%;" />

  - `Update & Create Form`

    <img src="README.assets/13_form-1623634870938.png" alt="image-20210612162725034" style="zoom:50%;" />

- **Random**

  - `card`

    <img src="README.assets/14_random-1623634870938.png" alt="image-20210612162856027" style="zoom:50%;" />
