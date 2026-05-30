
//Task N
function findPalindrom(str: String): boolean {
    const str1: string = str.toLowerCase().split('').reverse().join('');
    return str == str1;
}
const result1: boolean = findPalindrom("typescript")
const result2: boolean = findPalindrom("daaad")
console.log(result1)
console.log(result2)




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