### ✔️ filter()

배열에서 특정 조건에 만족하는 원소들만 추출하여 배열을 만들 때 사용하는 함수입니다. 

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

const tasksNotDone = todos.filter(todo => todo.done === false);
console.log(tasksNotDone);
// 0:
// done: false
// id: 4
// text: "배열 내장함수 배우기"
```

### ✔️ splice(), slice()

splice()는 배열에서 특정 항목을 제거할 때 사용하는 함수입니다. 함수를 사용할 때는 제거하는 과정에서 해당 원소가 몇 번째인지 명시해줘야 합니다. 

```jsx
const numbers = [10, 20, 30, 40];
const index = numbers.indexOf(30);
numbers.splice(index, 1);
console.log(numbers); // [10, 20, 40]
```

index에 해당하는 원소(30)이 사라진 것을 볼 수 있습니다. 만약 numbers.splice(index, 2)를 실행한다면 index에 해당하는 원소부터 2개 지우겠다는 뜻이 됩니다. 그럼 결과값으로 [10,20]가 나오겠죠 ?

```jsx
const numbers = [10, 20, 30, 40];

const sliced = numbers.slice(0, 2); // index 0부터 2까지 슬라이스 
console.log(sliced); // [10, 20]
console.log(numbers); // [10, 20, 30, 40]
```

slice()는 start 파라미터와 end 파라미터가 필요합니다. start 파라미터는 어떤 인덱스부터 슬라이스할 지를 의미하고, end 파라미터는 어디까지 슬라이스할 지를 의미합니다. 유의할 점은 end 파라미터는 해당 인덱스 전까지 슬라이스합니다. 또한 splice()와 다르게 slice()는 원래 배열의 값이 변하지 않고 그대로 있습니다. 

### ✔️ shift()

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

### ✔️ unshift()

```jsx
const numbers = [10, 20, 30, 40];
numbers.unshift(50);
console.log(numbers); // [10, 20, 30, 40, 50]
```

unshift()는 맨 앞에 원소를 추가합니다. 

### ✔️ push()와 pop()은 한 쌍

```jsx
const numbers = [10, 20, 30, 40];
numbers.push(50);
const value = numbers.pop();
console.log(value); // 50
console.log(numbers); // [10, 20, 30, 40]
```

push()로 맨 뒤에 원소를 넣고, pop()으로 맨 뒤에 원소를 추출합니다. 코드에서 보듯 같은 위치의 원소를 넣고 추출하기 때문에 push()와 pop()은 한 쌍이라고 보면 됩니다. 

### ✔️ shift()와 unshift()은 한 쌍

```jsx
const numbers = [10, 20, 30, 40];
numbers.unshift(0);
console.log(numbers); // [0, 10, 20, 30, 40]
const value = numbers.shift();
console.log(numbers); // [10, 20, 30, 40]
```

shift()로 맨 앞에 원소를 넣고, unshift()로 맨 앞의 원소를 추출합니다. 이것도 마찬가지로 같은 위치의 원소를 넣고 추출하기 때문에 shift()와 unshift()는 한 쌍이라고 보면 외우기 쉽습니다. 

참고로 push()와 pop(), shift()와 unshift()은 모두 배열 자체를 바꾼다는 것을 알아두세요. 

### ✔️ concat()

```jsx
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const concated = arr1.concat(arr2);
console.log(concated); // [1, 2, 3, 4, 5, 6]
```

concat() 메서드는 인자로 주어진 배열이나 값들을 기존 배열에 합쳐서 새 배열을 반환합니다. concat()은 기존의 배열을 수정하지 않고, 새 배열을 반환합니다. 

### ✔️ join()

```jsx
const array = [1, 2, 3, 4, 5];
console.log(array.join()); // 1,2,3,4,5
console.log(array.join(' ')); // 1 2 3 4 5
```

join() 메서드는 배열의 모든 요소를 연결해 하나의 문자열로 만듭니다. join() 메서드 안에 파라미터로 seperator를 넣어줄 수 있습니다. seperator은 배열의 각 요소를 구분할 문자열을 지정합니다. 이 구분자는 필요한 경우 문자열로 변환됩니다. 생략하면 배열의 요소들이 쉼표로 구분됩니다. separator가 빈 문자열이면 모든 요소들이 사이에 아무 문자도 없이 연결됩니다.

### ✔️ reduce()

```jsx
const numbers = [1, 2, 3, 4, 5];

let sum = 0;
numbers.forEach(n => {
  sum += n;
});

console.log(sum); // 15
```

reduce() 메서드를 사용하면 위의 코드를 한 줄로 작성할 수 있습니다. 

```jsx
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum); // 15
```

reduce() 메서드는 배열의 각 요소에 대해 주어진 reducer 함수를 실행하고, 하나의 결과값을 반환합니다. reduce 메서드는 네 개의 인자를 가집니다. 위의 코드에서는 2가지만 받아왔네요? 꼭 모든 파라미터를 입력하지 않아도 된다는 점을 알아두세요. 

1. accumulator
2. currentValue(현재 값)
3. currentIndex(현재 인덱스)
4. array(reduce()를 호출한 배열)

reduce 함수의 반환 값은 accumulator에 할당되고, accumulator는 순회 중 유지되므로 결국 최종 결과는 하나의 값이 됩니다. 위의 코드의 작동방식에 대해 설명하면 0은 accumulator의 초기값입니다. accumulator은 누적값이 됩니다. 초기값 0이 accumulator이 되고, current는 각 원소를 가리키는데 처음에는 1이 되겠죠? 그럼 accumulator = 0, current = 1이 되어 '0 + 1'이 됩니다. 그럼 accumulator은 누적값이라고 했으니 1이 됩니다. 다시 current 값은 다음 원소인 2가 됩니다. accumulator = 1, current = 2가 되어 '1 + 2'이 되겠죠? 그럼 3이 accumulator이 되고 이런 식으로 반복되어 결과값 15를 반환합니다. 

```jsx
const numbers = [1, 2, 3, 4, 5];

const avg = numbers.reduce((accumulator, current, index, array) => {
  if (index === array.length - 1) { // index가 마지막 원소일 때
    return (accumulator + current) / array.length;
  }
  return accumulator + current;
}, 0);
console.log(avg); // 3
```

위에서는 reduce() 메서드를 이용하여 배열의 총합을 구해봤습니다. 이제 배열의 평균을 구해보도록 하겠습니다. 위 코드의 작동방식은 일단 0을 초기값 설정했으니 accumulator은 0이 됩니다. current는 현재 가리키는 원소이고 index는 현재 가리키는 원소의 인덱스 값, array는 자기 자신(배열)이 되겠죠? if문안의 조건은 index가 마지막 원소일 때이니까 조건을 충족하지 않으므로 반복문을 나가서 accumulator + current를 합한 값을 리턴합니다. 계속 누적하여 값을 더하다가 index가 마지막 원소일 때 평균값을 계산하여 결과값 3을 반환합니다. 

### ✔️ reduce()의 다른 예시

```jsx
const alphabets = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'e'];
const counts = alphabets.reduce((acc, current) => {
  if (acc[current]) {
    acc[current] += 1;
  } else {
    acc[current] = 1;    
  }
  return acc;
}, {})

console.log(counts); // {a: 3, b: 1, c: 2, d: 1, e: 1}
```

배열 안에 각 알파벳들이 몇 개씩 있는지 확인해서 객체에 결과를 넣어줄 것입니다. 위에서는 초기값을 0으로 넣어줬지만 여기에서는 빈 객체를 넣어주도록 하겠습니다. 위의 코드의 작동방식을 보면 초기값이 빈 객체이기 때문에 acc에 객체가 오게 됩니다. 그리고 current는 'a'겠죠? 그리고 나서 비어있는 객체에 'a'가 있는지 확인을 합니다. 'a'가 없으니 else문으로 넘어가서 a는 1로 설정됩니다. 다음 루프를 돌아서 acc에는 a: 1이라고 넣어져 있겠죠? 다음 current는 'a'이기 때문에 1이 더해져서 a가 2가 됩니다. 이러한 반복을 통해서 배열 안의 각 원소들 갯수를 카운트한 결과값이 객체가 만들어지게 됩니다.
