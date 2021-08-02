### ✔️ 콜백 함수(Call Back function)

**콜백 함수는 코드를 통해 명시적으로 호출하는 함수가 아니라, 개발자는 단지 함수를 동록하기만 하고, 어떤 이벤트가 발생했거나 특정 시점에 도달했을 때 시스템에서 호출하는 함수를 말합니다.**
 즉, 콜백함수는 콜백함수라는 유니크한 문법적 특징을 가지고 있는 것이 아니라, 호출방식에 의한 구분입니다. 아래의 코드와 같이 대표적인 콜백 함수의 사용 예로는 자바스크립트에서 이벤트 핸들러 처리입니다. 

```html
<button id="button1" onclick="button1_click();">버튼1</button>
<script>
function button1_click() {
	alert("버튼1을 누르셨습니다.");
}
</script>
```

Html에 onclick에 button1_click함수는 브라우저의 javascript API에서 DOM 이벤트 핸들러에 전달(등록)되고, 해당 버튼에 클릭이벤트가 발생했을 이벤트 핸들러가 콜백함수를 호출합니다.

### ✔️ 배열 내장함수 - map()

map 함수는 callbackFunction을 실행한 결과를 가지고 새로운 배열을 만들 때 사용합니다.

```jsx
const array =[1, 2, 3, 4, 5, 6, 7, 8];

const squared = [];
for (let i = 0; i < array.length; i++) {
    squared.push(array[i] * array[i]);
}

console.log(squared); // [1, 4, 9, 16, 25, 36, 49, 64]
```

아래와 같이 for문은 forEach문으로 바꿔 작성할 수도 있습니다. 

```jsx
const array =[1, 2, 3, 4, 5, 6, 7, 8];

const squared = [];
array.forEach(n => {
  squared.push(n * n);
});

console.log(squared); // [1, 4, 9, 16, 25, 36, 49, 64]
```

이번엔 map함수로 구현해보겠습니다. 

```jsx
const array =[1, 2, 3, 4, 5, 6, 7, 8];

const square = n => n * n;
const squared = array.map(square);

console.log(squared); // [1, 4, 9, 16, 25, 36, 49, 64]
```

square 라는 함수를 만들어서 n을 파라미터로 갖고 n * n을 반환하게 합니다. 위에서는 빈 배열을 만들어서 값들을 push했는데, 이번에는 그럴 필요없이 map() 안에 square 함수를 넣어줍니다. 

위의 함수를 더 간결하게 만들 수도 있습니다. 

```jsx
const array =[1, 2, 3, 4, 5, 6, 7, 8];

const squared = array.map(n => n * n);

console.log(squared); // [1, 4, 9, 16, 25, 36, 49, 64]
```

또 다른 예시를 들어보겠습니다. 객체 배열들을 텍스트로만 이루어진 문자열 배열로 바꾸고 싶다면 어떻게 해야할 수 있을까요? 

```jsx
const items = [
    {
      id: 1,
      text: 'hello'
    },
    {
      id: 2,
      text: 'bye'
    }
];

const texts = items.map(item => item.text);
console.log(texts); // ["hello", "bye"]
```

### ✔️ indexOf()

이번에는 배열에서 원하는 항목들이 어디에 있는지 알려주는 함수들에 대해서 알아보겠습니다. 

```jsx
const superheroes = ['아이언맨', '캡틴 아메리카', '토르', '닥터 스트레인지'];

const index = superheroes.indexOf('토르');
console.log(index); // 2
```

이런 식으로 특정 항목이 배열에서 몇 번째 원소인지 알고 싶다면 배열명.indexOf()라는 배열 내장함수를 사용하면 됩니다. 이와 비슷한 내장함수가 하나 더 있는데 아래에서 더 자세하게 알아보겠습니다. 

### ✔️ indexOf()

배열 안의 원소들이 boolean이거나 문자열 혹은 숫자라면 배열에서 몇 번째 원소인지 indexOf()로 충분히 찾을 수 있습니다. 하지만 배열 안의 원소들이 객체이거나 특정 조건으로 찾는다면 indexOf()로는 찾기 어렵습니다. 

```jsx
const todos = [
    {
        id: 1,
        text: '자바스크립트 입문',
        done: true
    },
    {
        id: 2,
        text: '함수 배우기',
        done: true
    },
    {
        id: 3,
        text: '객체와 배열 배우기',
        done: true
    },
    {
        id: 4,
        text: '배열 내장함수 배우기',
        done: false
    }
];

const index = todos.indexOf(3);
console.log(index); // -1
```

indexOf 함수를 썼을 때 결과값이 -1이 나온 이유는 일치하는 것이 없다는 뜻입니다. 이럴 때엔 findIndex 함수를 써야합니다. 

### ✔️ findIndex()

```jsx
const todos = [
    {
        id: 1,
        text: '자바스크립트 입문',
        done: true
    },
    {
        id: 2,
        text: '함수 배우기',
        done: true
    },
    {
        id: 3,
        text: '객체와 배열 배우기',
        done: true
    },
    {
        id: 4,
        text: '배열 내장함수 배우기',
        done: false
    }
];

const index = todos.findIndex(todo => todo.id === 3);
console.log(index); // 2
```

findIndex 함수는 특정 조건을 확인하여 조건이 일치하면 일치하는 원소가 몇 번째인지 알려주는 함수입니다. 위의 예시는 단순하게 숫자인 id값을 확인했지만, 배열 안의 원소들이 객체이거나 특정 조건(예를 들면 3으로 나눈 값이 0인 원소)으로 찾는다면 이 함수를 쓰는 것이 효율적입니다. 

### ✔️ find()

위의 코드에서 findIndex() 대신 find()를 사용한다면 특정 조건에 맞는 값을 출력합니다.

```jsx
const todos = [
    {
        id: 1,
        text: '자바스크립트 입문',
        done: true
    },
    {
        id: 2,
        text: '함수 배우기',
        done: true
    },
    {
        id: 3,
        text: '객체와 배열 배우기',
        done: true
    },
    {
        id: 4,
        text: '배열 내장함수 배우기',
        done: false
    }
];

const todo = todos.find(todo => todo.id === 3); // 반환하는 값은 todo객체 
console.log(index); // 2 
```

위의 세가지 함수(indexOf(), findIndex(), find())는 가장 첫번째로 찾은 항목을 알려주게 됩니다.

```jsx
const numbers = [10, 20, 30, 40];

const value = numbers.shift();
console.log(value); // 10 
console.log(numbers); // [20, 30, 40]
```

shift()는 첫번째 원소를 배열에서 추출합니다. 원래 배열의 값이 변하지 않고 그대로 있습니다. 

### ✔️ pop()

```jsx
const numbers = [10, 20, 30, 40];

const value = numbers.pop();
console.log(value); // 40
console.log(numbers); // [10, 20, 30]
```

pop()은 마지막 원소를 배열에서 추출합니다. 원래 배열의 값이 변하지 않고 그대로 있습니다.
