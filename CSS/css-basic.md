# ✔️ CSS

### 태그에 직접 작성하기(인라인)

```html
<div style="color: red;">태그에 직접 작성1</div> <!-- red -->
```

### HTML에 포함하기(내장)

```html
head>
  <style>
    div {
      color: red;
    }
  </style>  
</head>
<body>
  <div>HTML에 포함1</div> <!-- red -->
  <div>HTML에 포함2</div> <!-- red -->
  <div>HTML에 포함3</div> <!-- red -->
</body>
```

### HTML 외부에서 불러오기

```html
<!-- HTML -->
<head>
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  <div>HTML에 외부에서 불러오기1</div> <!-- red -->
</body>
```

## 여백

### # margin(요소의 바깥 여백)

요소의 바깥 여백을 지정합니다. 바깥 여백은 요소와 요소 사이의 여백(거리, 공간)을 생성할 때 사용합니다. 

```css
div {
  margin: 20px;
  요소바깥여백: 여백값;
}
```

```css
div {
  margin-top: 20px;
  margin-right: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
  요소바깥여백-위쪽: 여백값;
  요소바깥여백-오른쪽: 여백값;
  요소바깥여백-아래쪽: 여백값;
  요소바깥여백-왼쪽: 여백값;
}
```

### # padding(요소의 내부 여백)

요소의 내부 여백을 지정합니다. 내부 여백은 자식 요소를 감싸는 여백을 의미합니다. 

```css
div {
  padding: 20px;
  요소내부여백: 여백값;
}
```

```css
div {
  padding-top: 20px;
  padding-right: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
  요소내부여백-위쪽: 여백값;
  요소내부여백-오른쪽: 여백값;
  요소내부여백-아래쪽: 여백값;
  요소내부여백-왼쪽: 여백값;
}
```

### 수평 중앙 정렬

```css
margin: auto;
```

### 수직 중앙 정렬

```css
padding: 8px;
```

## 색상

### # color(글자 색상)

요소 내용(Text)의 글자 색상을 지정합니다.정말 많은 입문자가 **`font-color`**, **`text-color`**로 실수를 합니다만 그런 속성은 없습니다.

```css
div {
  color: red;
  글자색상: 빨강;
}
```
