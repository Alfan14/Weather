// javascript

function calculate() {
  var x = document.getElementById("select-value").value;
  x = parseFloat (x);
  var inputOne = document.getElementById("inputOne").value;
  inputOne = parseFloat (inputOne);
  var inputTwo = document.getElementById("inputTwo").value;
  inputTwo = parseFloat (inputTwo);
  var result1 = (inputOne  * inputTwo);
  var result2 = (result1/1000);

  document.getElementById('output').innerText = result2 * x ;
  document.getElementById('output2').innerText = result2 * x *30;
}
calculate()
document.getElementById("calculate").onclick = function(){calculate(); };
//option 2