```jsx
const numbers = {
  a: 1,
  b: 2,
  sum: 3,
  get sum() {
    console.log("sum"); // 조회할 때마다 sum 메시지 호출
    return this.a + this.b;
  }
};

console.log(numbers.sum);
numbers.a = 5;
numbers.b = 7;
console.log(numbers.sum);
// 실행결과 :
// sum 
// 3
// sum 
// 12
```

이렇게 get 함수를 하나만 받는다면 조회할 때마다 sum을 구할 수 있게 되어서 위의 코드보다 상당히 효율적입니다.
