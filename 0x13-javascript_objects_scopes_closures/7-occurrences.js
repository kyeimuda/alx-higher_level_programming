#!/usr/bin/node
// a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      times++;
    }
  }
  return (aux);
};
