// app.test.js
const holaMundo = require('./app');

test('Debe retornar "Hola, mundo!"', () => {
  expect(holaMundo()).toBe('Hola, mundo!');
});