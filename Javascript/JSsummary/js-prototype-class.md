### ✔️ 객체 생성자

프로토타입과 클래스에 대해서 알아보기 전에 우선 객체 생성자라는 것을 알아봅시다. 객체 생성자는 함수를 통해서 새로운 객체를 만들고 그 안에 넣고 싶은 값 혹은 함수들을 구현 할 수 있게 해줍니다.

```jsx
function Animal(type, name, sound) {
    this.type = type;
    this.name = name;
    this.sound = sound;
    this.say = function() { // 익명 함수
      console.log(this.sound);
    }
}

const dog = new Animal('개', '멍멍이', '멍멍');
const cat = new Animal('고양이', '야옹이', '야옹');

dog.say(); // 멍멍
cat.say(); // 야옹
```

객체 생성자를 사용 할 때는 보통 함수의 이름을 대문자로 시작하고, 새로운 객체를 만들 때에는 `new` 키워드를 앞에 붙여주어야 합니다.

지금 위 코드를 보시면, dog가 가지고 있는 say 함수와 cat이 가지고 있는 수행하는 코드가 똑같음에도 불구하고 객체가 생성 될 때 마다 함수도 새로 만들어져서 this.say 로 설정이 되고 있습니다. 

같은 객체 생성자 함수를 사용하는 경우, 특정 함수 또는 값을 재사용 할 수 있는데 바로 프로토타입입니다.

### ✔️ 프로토타입

```jsx
function Animal(type, name, sound) {
    this.type = type;
    this.name = name;
    this.sound = sound;
}

Animal.prototype.say = function() {
  console.log(this.sound);
}

Animal.prototype.sharedValue = 1;

const dog = new Animal('개', '멍멍이', '멍멍');
const cat = new Animal('고양이', '야옹이', '야옹');

dog.say(); // 멍멍
cat.say(); // 야옹

console.log(dog.sharedValue); // 1
console.log(cat.sharedValue); // 1
```

프로토타입의 역할은 우리가 객체 생성자로 무언가를 만들었을 때, 객체들끼리 공유할 수 있는 어떤 값이나 함수를 설정하는 것 입니다. 

### ✔️ 객체 생성자 상속받기

만약에 우리가 Animal 함수를 상속받지 않는다면 이렇게 구현해야합니다. 

```jsx
function Dog(name, sound) {
  this.type = '개'
  this.name = name;
  this. sound = sound;
}

function Cat(name, sound) {
  this.type = '고양이';
  this.name = name;
  this.sound = sound;
}

Dog.prototype.say = function() {
  console.log(this.sound);
}

Cat.prototype.say = function() {
  console.log(this.sound);
}

const dog = new Animal('개', '멍멍이', '멍멍');
const cat = new Animal('고양이', '야옹이', '야옹');

dog.say();
cat.say();
```

위의 코드에서는 Dog와 Cat 두 개가 비슷한 구조인데 객체 생성자를 각각 만들어줘야하는 것이 상당히 불편하죠? 이럴 때 상속을 해주면 편합니다. 

```jsx
function Animal(type, name, sound) { // Animal 객체 생성자
    this.type = type;
    this.name = name;
    this.sound = sound;
}

Animal.prototype.say = function() { // 객체 생성자에 prototype.say 함수 넣기
  console.log(this.sound);
}

function Dog(name, sound) { // Dog 객체 생성자 
  Animal.call(this, '개', name, sound);
}

function Cat(name, sound) { // Cat 객체 생성자
  Animal.call(this, '고양이', name, sound);
}

Dog.prototype = Animal.prototype;
Cat.prototype = Animal.prototype;

const dog = new Dog('멍멍이', '멍멍');
const cat = new Cat('야옹이', '야옹');

dog.say(); // 멍멍
cat.say(); // 야옹
```

새로 만든 Dog 와 Cat 함수에서 `Animal.call` 을 호출해주고 있는데요, 여기서 첫번째 인자에는 this 를 넣어주어야 하고, 그 이후에는 Animal 객체 생성자 함수에서 필요로 하는 파라미터를 넣어주어야 합니다.

추가적으로 prototype 을 공유해야 하기 때문에 상속받은 객체 생성자 함수를 만들고 나서 prototype 값을 Animal.prototype 으로 설정해주었습니다.

### ✔️ 클래스

클래스라는 기능은 C++, Java, C#, PHP 등의 다른 프로그래밍 언어에는 있는 기능인데 예전 자바스크립트(ES5) 에서는 클래스 문법이 따로 없었기 때문에 위에서 작성한 코드처럼 객체 생성자 함수를 사용하여 비슷한 작업을 구현해왔습니다.

ES6 에서부터는 `class` 라는 문법이 추가되었는데요, 우리가 객체 생성자로 구현했던 코드를 조금 더 명확하고, 깔끔하게 구현 할 수 있게 해줍니다. 

```jsx
class Animal {
    constructor(type, name, sound) {
    this.type = type;
    this.name = name;
    this.sound = sound;
    }
    say() {
        consoe.log(this.sound);
    }
}

const dog = new Animal('개', '멍멍이', '멍멍');
const cat = new Animal('고양이', '야옹이', '야옹');

dog.say();
cat.say();
```

그리고 class에는 객체 생성자와 비슷한 개념이 있는데 construtor라고 부릅니다. 이는 생성자라는 의미를 가지고 있습니다. 또한 class 내부에 say() 함수를 만들어주었는데, 함수를 만들게 되면 자동으로 프로토타입으로 등록이 됩니다. 

추가적으로 상속도 훨씬 쉽게 해줄 수 있습니다.

```jsx
class Animal {
    constructor(type, name, sound) {
        this.type = type;
        this.name = name;
        this.sound = sound;
    }
    say() {
        console.log(this.sound);
    }
}

class Dog extends Animal {
    constructor(name, sound) {
        super('개', name, sound);    
    }
}

class Cat extends Animal {
    constructor(name, sound) {
        super('고양이', name, sound);
    }
}

const dog = new Dog('멍멍이', '멍멍');
const cat = new Cat('야옹이', '야옹');
const cat2 = new Cat('야오오옹이', '야오오오오옹');

dog.say(); // 멍멍
cat.say(); // 야옹
cat2.say() // 야오오오오옹
```

### ✔️ 클래스 예제 - Food class 만들기

```jsx
class Food {
  constructor(name) {
    this.name = name;
    this.brands = [];
  }
  addBrand(brand) { // 주로 클래스 내부에 구현하는 함수들을 메서드라고 부릅니다. 
    this.brands.push(brand);
}
print() {
  console.log(`${this.name} 을 파는 음식점들:`);
  console.log(this.brands.join(', '));
  }
}

const pizza = new Food('피자');
pizza.addBrand('피자헛');
pizza.addBrand('도미노 피자');

const chicken = new Food('치킨');
chicken.addBrand('굽네치킨');
chicken.addBrand('BBQ');

pizza.print();
chicken.print();
// 피자 을 파는 음식점들:
// 피자헛, 도미노 피자
// 치킨 을 파는 음식점들:
// 굽네치킨, BBQ
```

constructor로 지정한 파라미터 name으로 객체 생성할 때 넣어준 Food 이름(피자, 치킨)을 받아옵니다. 그래서 this.name에 저장되고 새 객체를 생성할 때 this.brands라는 배열이 만들어지게 됩니다. addBrand 메서드는 브랜드 이름을 가져와서 brand 배열에 넣어주게 됩니다. print()라는 함수를 만들어서 결과값을 보여주게 만들었습니다.
