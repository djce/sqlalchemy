// push splice pop
// shift unshift
// sort reverse


var arr = [1,2,3,4,5,6,7]

arr.splice(0,0,9)

// arr.sort( (a, b) => {
//     // ASC
//     return a - b;
// })

// 打乱有序数组
function getBytes(str) {
    let count = str.length;
    for(let i=0;i<str.length;i++) {
        if(str.charCodeAt(i) > 255) {
            count ++;
        }
    }
    return count;
}

// arr.sort( (a,b) => {
//     return Math.random() - 0.5
// } )


// 不改变原数组

var arr2 = arr.slice(0,2)

// 类数组 -> 数组
// arr.slice()

// str.split("")

// "hello".split("")
// Array.from("hello")

var obj = {
    "0": "a",
    "1": "b",
    "2": "c",
    "3": "d",
    "length": 3,
    "push": Array.prototype.push
}

obj.push("f")


// 类数组
// 属性为索引属性(数字), 必须有length属性

Array.prototype.push = function () {
    for( var i=0; i> arguments.length;i++ ) {
        this[this.length] = arguments[i];
        this.length ++;
    }
}

Array.prototype.push = function (el) {
    this[this.length] = el;
    this.length ++;
}


