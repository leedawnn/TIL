### ✔️ 변수와 상수

기본적으로 **변수**란 **바뀔 수 있는 값**, **상수**는 **바뀌지 않는 값**입니다. 

**let** 구문은 블록 유효 범위를 갖는 **지역 변수**를 선언하며, 선언과 동시에 임의의 값으로 초기화할 수도 
있습니다.

```jsx
let value = 1;
let value = 2;
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d864542-5f58-424b-90a9-8f0ae2d61fef/스크린샷_2021-07-26_오후_1.32.41.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d864542-5f58-424b-90a9-8f0ae2d61fef/스크린샷_2021-07-26_오후_1.32.41.png)

**const** 선언은 블록 범위의 **상수**를 선언합니다. 상수의 값은 재할당할 수 없으며 다시 선언할 수도 없습니다.

```jsx
const a = 1;
a = 2; // 상수값 바꾸기 시도! >> 실패 💩
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f17ef3a3-cd8f-40d3-b081-a334baf57ca2/스크린샷_2021-07-26_오후_1.49.15.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f17ef3a3-cd8f-40d3-b081-a334baf57ca2/스크린샷_2021-07-26_오후_1.49.15.png)

```jsx
const a = 1;
const a = 2;
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eef0f510-5206-41d3-acfe-9222e86bdcd1/스크린샷_2021-07-26_오후_1.53.59.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eef0f510-5206-41d3-acfe-9222e86bdcd1/스크린샷_2021-07-26_오후_1.53.59.png)

**그러나, 상수와 변수 모두 다른 블록 범위에서는 같은 이름으로 중복 선언이 가능합니다.** 

```jsx
const a = 1;
if (a + 1 === 2) {
	const a = 2;
	console.log('if문 안의 a값은 ' + a); // if문 안의 a값은 2
}
console.log('if문 밖의 a값은 ' + a); // if문 안의 a값은 1
```

위와 같은 코드에서 var을 사용한다면 어떻게 될까요? 👀

```jsx
var a = 1;
if (a + 1 === 2) {
	var a = 2;
	console.log('if문 안의 a값은 ' + a); // if문 안의 a값은 2
}
console.log('if문 밖의 a값은 ' + a); // if문 안의 a값은 2
```

### ES6로 넘어오면서 권장하지 않지만, 알아 두어야하는 var

```jsx
var a = 1;
var a = 2;
```

### ✔️ 데이터 타입

🕹 **문자열**

```jsx
let text = 'hello';
let name = "헬로우 자바스크립트"; 
```

🕹 **Boolean**

```jsx
let good = true;
let loading = false;
```

🕹 **Null, Undefiend**

```jsx
let friend = null;
let criminal;
console.log(criminal);
```

### ✔️ 산술 연산자

```jsx
let a = 1;
console.log(a++); // 1
console.log(a);   // 2
console.log(++a); // 3
```

### ✔️ 논리 연산자

- NOT 연산자(!)

```jsx
const a = !true;
console.log(a); // false
```

- AND 연산자(&&)

```jsx
const a = true && true;
console.log(a); // true

const b = false && true;
console.log(a); // false
```

- OR 연산자(||)

```jsx
const a = false || false;
console.log(a);
```

**논리연산자는 사칙연산과 비슷하게 아래와 같이 계산되는 우선순위가 있습니다.** 

🎯 **NOT > AND > OR**

```jsx
const value = !(true && false || true && false || !false);
// !(true && false || true && false || true)
// !(false || false || true)
// !(true)
cossole.log(value);
// false
```

### ✔️ 비교 연산자

```jsx
const a = 1;
const b = 1;
const equals = a === b; 
console.log(equals); // true
```

**== 와 === 의 차이점은 무엇일까요 ?** == 이렇게 equal sign을 두개만 입력했을 경우에는 데이터 타입을 

검사하지 않습니다. 그렇기 때문에 === 보다는 정확성이 확실히 떨어집니다. 

```jsx
// 숫자와 문자 비교 
const a = 1;
const b = '1';
const equals = a == b; 
console.log(equals); // true

// null과 undefined 비교 
const a = null;
const b = undefined;
const equals = a == b; 
console.log(equals); // true
```

```jsx
const a = 'a';
const b = 'b';
const notEquals = a !== b;
console.log(notEquals); // true
```

```jsx
const a = a;
const b = 'b';
const notEquals = a != b;
console.log(notEquals); // false
```

아까와 마찬가지로 **!=와 !==는 차이가 있습니다.** !=는 데이터 타입을 검사하지 않습니다. 그래서 실제 개발을 할 때는 !==를 주로 사용합니다. 

### ✔️ 문자열 붙이기

```jsx
const a = '안녕';
const b = '하세요';
console.log(a + b); // 안녕하세요
```

### ✔️ 조건문

### 🎯 if문

```jsx
const a = 1;
if (a + 1 === 2) { // 조건식  
	console.log('a + 1이 2입니다.'); // 실행할 구문 
}
// 실행결과 : a + 1이 2입니다.
```

### 🎯 if else문

```jsx
const a = 10;

if (a > 15) {
	console.log('a가 15보다 큽니다.');
} else {
	console.log('a가 15보다 크지 않습니다.');
}
// 실행 결과: a가 15보다 크지 않습니다.
```

### 🎯 else if문

```jsx
const a = 10;

if (a === 5) {
	console.log('5 입니다!');
} else if (a === 10) {
	console.log('10 입니다!');
} else {
	console.log('5도 아니고 10도 아닙니다.');
}
// 실행 결과: 10 입니다!
```

### 🎯 switch case문

특정값이 무엇이냐에 따라 다를 때 switch case문을 씁니다. 

```jsx
const device = 'macbook';

switch (device) {
	case 'iphone':
		console.log('아이폰!');
		break;
	case 'ipad':
		console.log('아이패드!');
		break;
	case 'galaxy note':
		console.log('갤럭시 노트!');
		break;
	default:
		console.log('모르겠네요..');
}
```
