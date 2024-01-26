//Todo:이거해라
//Fixme:이거 고쳐라
//주석

let abc = [1,2,3,4,5,6];
let evenSum = abc.filter(x => x % 2 == 0).reduce( (s, v ) => s +v , 0);
console.log(evenSum);