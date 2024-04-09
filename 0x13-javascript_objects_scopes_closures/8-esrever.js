#!/usr/bin/node

exports.esrever = function (list) {
  const S = [];
  for (let i = list.length - 1; i >= 0; i--) {
    S.push(list[i]);
  }
  return (S);
};
