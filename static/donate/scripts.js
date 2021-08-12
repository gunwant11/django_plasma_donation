fetch("https://api.rootnet.in/covid19-in/stats/latest")
  .then((res) => res.json())
  .then((data) => {
    console.log(data)
    
    const deaths = data.data.summary.deaths;
    document.getElementById("box-3").innerHTML = deaths;
    const recovered = data.data.summary.discharged;
    document.getElementById("box-2").innerHTML = recovered;
    const total = data.data.summary.total;
    document.getElementById("box-4").innerHTML = total;
    const active = total-(deaths+recovered)
    document.getElementById("box-1").innerHTML = active;
  });

  document.addEventListener('DOMContentLoaded', () => {
    let btn = document.getElementsByClassName('offButton');
    btn[0].addEventListener('click', (e) => { console.log(e)});
  });

  const disable = document.getElementsByClassName("offButton");
  
