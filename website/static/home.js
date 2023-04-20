let startDate = document.getElementById('startDate')

startDate.addEventListener('change',(e)=>{
  let startDateVal = e.target.value
  document.getElementById('startDateSelected').innerText = startDateVal
})