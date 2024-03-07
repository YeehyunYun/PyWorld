## 개발환경
### Vue-CLI 
vue 개발 환경을 설정해주는 도구
```
# 설치
npm install -g @vue/cli

# 생성
vue create (이름)

cd (이름)

# 실행
npm run serve
```

## 프로젝트 구조
### src/
- assets/ : 이미지 등 어플리케이션에서 사용되는 파일들이 모여 있는 디렉토리
- components/ : Vue 컴포넌트들이 모여 있는 디렉토리
- router/ : vue-router 설정을 하는 디렉토리
- App.vue : 가장 최상위 컴포넌트
- main.js : 가장 먼저 실행되는 javascript 파일, Vue 인스턴스를 생성하는 역할
