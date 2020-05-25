// ************************************************* 1 *************************************************
// create a function that takes an array and prints two sorted arrays,
// one that contains all the numbers and one that contains all the string characters
const stringsAndNumbers = ['d', '0', [6], 'c', 8, 4, ['b', [1, 'p']]];

function distinct(array) {
  let numberArray = [];
  let stringArray = [];
  array.forEach(function (item, _index) {
    if (typeof item == 'number'){
      numberArray.push(item);
    }
    if (typeof item == 'string') {
      stringArray.push(item);
    }
  });
  stringArray.sort();
  numberArray.sort();
  console.log('String Array: ', stringArray);
  console.log('Number Array: ', numberArray);
}

distinct(stringsAndNumbers);


// ************************************************* 2 *************************************************
// create a function that takes an array and returns a filtered array from the words that include any form of the word 'student'
const labels = ['student', 'istuedent', 'studenTTT', '15', 'STUDENT', 'hello', 'world', null];

function removeLabels(array) {
  console.log(array.filter(function (el) {return typeof el == 'string' && el.toLowerCase().includes('student')}));
}

removeLabels(labels);


// ************************************************* 3 *************************************************
// Create a function that takes an array of objects like { ... , notes: [3, 5, 4]} and returns an array of objects like { ..., topNote: 5 }.
// If student has no notes then let's assume topNote: 0.
const students = [
  { name: 'john', lastName: 'papas', notes: [1, 9, 5] },
  { name: 'alex', notes: [] },
  { name: 'stef', lastName: 'k' },
  { lastName: 'krkx', notes: [8, 12] }
];

function transformNotes(array) {
  array.forEach(function (item, _index) {
    let topNote = ('notes' in item && item['notes'].length > 0) ? Math.max(...item['notes']) : 0;
    delete item['notes'];
    item['topNote'] = topNote;
  });
  console.log(array);
}

transformNotes(students);


// ************************************************* 4 *************************************************
// create a function that takes a string and returns an object that has the letters from the given word as keys,
// and the total count of each letter as value, for example the word 'school' must return { s:1, c:1, h:1, o:2, l:1 }
const word = 'student';

function groupLetters(string) {
  let counter  = string.split('').reduce((total, letter) => {
      total[letter] ? total[letter]++ : total[letter] = 1;
      return total;
    }, {});

  console.log(counter);
}

groupLetters(word);

// ************************************************* BONUS *************************************************
// create a function that takes an array of date objects and return the "longest streak" (i.e. number of consecutive days in a row, for the same month of the same year).
const dates = [
  "18-09-2019",
  "20-09-2020",
  "26-09-2019",
  "27-10-2020",
  "30-09-2019",
  "19-09-2019",
];

function findLongestStreak(array) {

}

findLongestStreak(dates);
