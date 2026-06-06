/*  Project Standards:
  - Logging standards
  - Naming standards:
        function, method, variable => camelCase
        class => PascalCase
        folder => kebab-case
        css => snake_case
   - Error handling
 */

// TASK Q
function hasProperty(obj: Record<string, any>, objKey: string): boolean {
  for (const key in obj) {
    if (key === objKey) {
      console.log(`object has -> ${objKey} <- property`);
      return true;
    }
  }
  console.log(`object does not have -> ${objKey} <- property`);
  return false;
}

const car = {
  name: "BMW",
  year: 2004,
};

console.log(hasProperty(car, "name"));
console.log(hasProperty(car, "origin"));
console.log(hasProperty(car, "year"));


//TASK P
// function objectToArray(obj: Record<string, any>): [string, any][] {
//   const result: [string, any][] = [];
//   for (const key in obj) {
//     result.push([key, obj[key]]);
//   }
//   return result;
// }

// console.log(objectToArray({ name: "Alex", age: 22, c: 30 }));




// task O
// function calculateSumOfNumbers(arr: any[]): number {
//   let total = 0;

//   for (const item of arr) {
//     if (typeof item === "number") {
//       total += item;
//     }
//   }

//   return total;
// }

// console.log(calculateSumOfNumbers([1, "10", { son: 10 }, true, 60, 29]));











//Task N
// function findPalindrom(str: String): boolean {
//     const str1: string = str.toLowerCase().split('').reverse().join('');
//     return str == str1;
// }
// const result1: boolean = findPalindrom("typescript")
// const result2: boolean = findPalindrom("daaad")
// console.log(result1)
// console.log(result2)




//task M
// function numberSquare(n: number[]) {
//     const result = n.map((num) => ({
//         number: num,
//         square: num ** 2,
//     }));
//     return result;
// }

// const numbers = [1, 2, 3, 4, 5, 6];

// console.log(numberSquare(numbers));