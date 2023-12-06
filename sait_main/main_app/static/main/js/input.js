function showResult() {
    var el = document.getElementById('userInput');
    var val = el.value;
    if (!val) {
      window.alert("No value was entered");
    } else {
        document.getElementById("work").innerHTML = val;
    }
  }
