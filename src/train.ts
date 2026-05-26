//task M
function numberSquare(n: number[]) {
    const result = n.map((num) => ({
        number: num,
        square: num ** 2,
    }));
    return result;
}

const numbers = [1, 2, 3, 4, 5, 6];

console.log(numberSquare(numbers));